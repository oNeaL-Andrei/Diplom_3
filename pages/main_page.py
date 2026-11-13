from selenium.webdriver.common.action_chains import ActionChains  # Импортируем инструмент для перетаскивания элементов
from selenium.webdriver.support import expected_conditions as EC  # Импортируем условия ожидания
from pages.base_page import BasePage  # Импортируем базовый класс страницы
from locators import MainPageLocators  # Импортируем локаторы главной страницы

class MainPage(BasePage):  # Класс главной страницы
    def open(self, url):
        self.open_page(url)  # Открываем страницу

    def open_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)  # Переходим в конструктор

    def open_ingredient_details(self):
        self.click_element(MainPageLocators.BURGER_INGREDIENT)  # Открываем окно с деталями ингредиента

    def close_ingredient_details(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)  # Закрываем окно с деталями ингредиента

    def get_ingredient_details_title(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_MODAL_TITLE)  # Получаем заголовок окна

    def get_order_number(self):
        self.wait.until(lambda driver: self.find_element(MainPageLocators.ORDER_NUMBER).text != "9999")  # Ждём появления настоящего номера заказа

        return self.get_element_text(MainPageLocators.ORDER_NUMBER)  # Получаем номер заказа

    def is_ingredient_modal_closed(self):
        return self.wait.until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_MODAL_TITLE))  # Проверяем, что окно закрылось

    def get_ingredient_counter(self):
        ingredient = self.find_element(MainPageLocators.BURGER_INGREDIENT)  # Находим карточку ингредиента
        counter = ingredient.find_element(*MainPageLocators.INGREDIENT_COUNTER)  # Ищем счётчик внутри карточки
        return counter.text  # Возвращаем значение счётчика

    def add_bun_to_order(self):
        ingredient = self.find_element(MainPageLocators.BURGER_INGREDIENT)  # Находим карточку булочки
        bun_top = self.find_element(MainPageLocators.BUN_TOP)  # Находим верхнюю зону конструктора

        if self.driver.capabilities["browserName"] == "firefox":
            self.driver.execute_script("""
                const ingredient = arguments[0];
                const target = arguments[1];
                const dataTransfer = new DataTransfer();

                ingredient.dispatchEvent(new DragEvent('dragstart', {
                    bubbles: true,
                    dataTransfer: dataTransfer
                }));

                target.dispatchEvent(new DragEvent('dragenter', {
                    bubbles: true,
                    dataTransfer: dataTransfer
                }));

                target.dispatchEvent(new DragEvent('dragover', {
                    bubbles: true,
                    dataTransfer: dataTransfer
                }));

                target.dispatchEvent(new DragEvent('drop', {
                    bubbles: true,
                    dataTransfer: dataTransfer
                }));

                ingredient.dispatchEvent(new DragEvent('dragend', {
                    bubbles: true,
                    dataTransfer: dataTransfer
                }));
            """, ingredient, bun_top)  # Перетаскиваем булочку через JavaScript в Firefox
        else:
            ActionChains(self.driver).drag_and_drop(ingredient, bun_top).perform()  # Перетаскиваем булочку в Chrome

    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)  # Нажимаем кнопку оформления заказа

