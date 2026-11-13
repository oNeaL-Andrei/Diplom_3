from selenium.webdriver.support.ui import WebDriverWait  # Импортируем ожидание
from selenium.webdriver.support import expected_conditions as EC  # Импортируем условия ожидания

class BasePage:  # Базовый класс страницы
    def __init__(self, driver):  # Инициализация класса
        self.driver = driver  # Сохраняем браузер
        self.wait = WebDriverWait(driver, 10)  # Ждём до 10 секунд

    def open_page(self, url):
        self.driver.get(url)  # Открываем страницу

    def get_current_url(self):
        return self.driver.current_url  # Получаем адрес страницы

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))  # Ждём видимости элемента

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))  # Ждём кликабельности элемента

        if self.driver.capabilities["browserName"] == "firefox":
            self.driver.execute_script("arguments[0].click();", element)  # Используем JavaScript для клика в Firefox
        else:
            element.click()  # Обычный клик в Chrome

    def get_element_text(self, locator):
        return self.find_element(locator).text  # Получаем текст элемента
