import allure  # Импортируем Allure
from pages.main_page import MainPage  # Импортируем главную страницу
from pages.login_page import LoginPage  # Импортируем страницу входа
from pages.feed_page import FeedPage  # Импортируем страницу ленты заказов
from helpers.urls import BASE_URL  # Импортируем адрес сайта
from data import TestData  # Импортируем тестовые данные

@allure.title("Проверка оформления заказа и обновления статистики")
def test_create_order(driver):  # Тест проверяет оформление заказа и обновление статистики в ленте заказов
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    feed_page = FeedPage(driver)

    feed_page.open_page(BASE_URL + "feed")

    initial_total = int(feed_page.get_total_orders_count())
    initial_today = int(feed_page.get_today_orders_count())

    main_page.open_page(BASE_URL + "login")
    login_page.login(TestData.EMAIL, TestData.PASSWORD)

    initial_counter = int(main_page.get_ingredient_counter())
    main_page.add_bun_to_order()

    updated_counter = int(main_page.get_ingredient_counter())
    assert updated_counter == initial_counter + 2

    main_page.click_order_button()

    order_number = main_page.get_order_number()
    assert order_number

    main_page.close_ingredient_details()
    feed_page.open_feed()

    assert feed_page.wait_for_order_in_progress(order_number)

    feed_page.wait_for_total_orders_count(initial_total + 1)
    feed_page.wait_for_today_orders_count(initial_today + 1)

