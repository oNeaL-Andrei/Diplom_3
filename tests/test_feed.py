import allure  # Импортируем Allure
from pages.feed_page import FeedPage  # Импортируем класс ленты заказов
from helpers.urls import BASE_URL  # Импортируем адрес сайта

@allure.title("Проверка перехода в ленту заказов")
def test_open_feed(driver):
    feed_page = FeedPage(driver)  # Создаём объект страницы ленты заказов
    feed_page.open_page(BASE_URL)  # Открываем главную страницу
    feed_page.open_feed()  # Переходим в ленту заказов

    assert feed_page.get_current_url() == BASE_URL + "feed"  # Проверяем переход в ленту заказов