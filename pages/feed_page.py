from selenium.webdriver.support.ui import WebDriverWait  # Импортируем ожидание Selenium
from pages.base_page import BasePage  # Импортируем базовый класс страницы
from locators import FeedPageLocators  # Импортируем локаторы ленты заказов

class FeedPage(BasePage):  # Класс страницы ленты заказов
    def open_feed(self):  # Метод для открыиия ленты заказов
        self.click_element(FeedPageLocators.FEED_BUTTON)  # Переходим в ленту заказов

    def get_total_orders_count(self):
        return self.get_element_text(FeedPageLocators.TOTAL_ORDERS_COUNT)  # Получаем количество заказов за всё время

    def get_today_orders_count(self):
        return self.get_element_text(FeedPageLocators.TODAY_ORDERS_COUNT)  # Получаем количество заказов за сегодня

    def get_in_progress_order(self):
        return self.get_element_text(FeedPageLocators.IN_PROGRESS_ORDER)  # Получаем номер заказа в работе

    def wait_for_total_orders_count(self, expected_count):
        self.wait.until(lambda driver: int(self.get_total_orders_count()) == expected_count)  # Ждём обновления количества заказов за всё время
            
    def wait_for_today_orders_count(self, expected_count):
        self.wait.until(lambda driver: int(self.get_today_orders_count()) == expected_count)  # Ждём обновления количества заказов за сегодня

    def wait_for_order_in_progress(self, order_number):
        expected_order_number = str(order_number).strip().zfill(5)  # Подготавливаем номер заказа

        wait = WebDriverWait(self.driver, 10, poll_frequency=0.1)

        return wait.until(lambda driver: expected_order_number in [element.get_attribute("textContent").strip()for element in driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDER)])  # Ждём появления номера заказа в разделе «В работе»


