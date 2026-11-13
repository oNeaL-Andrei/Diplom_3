import allure  # Импортируем Allure
from pages.main_page import MainPage  # Импортируем класс главной страницы
from helpers.urls import BASE_URL  # Импортируем адрес сайта

@allure.title("Проверка перехода в конструктор")
def test_open_constructor(driver):
    main_page = MainPage(driver)  # Создаём объект главной страницы
    main_page.open(BASE_URL + "feed")  # Открываем ленту заказов
    main_page.open_constructor()  # Переходим в конструктор

    assert main_page.get_current_url() == BASE_URL  # Проверяем переход в конструктор

@allure.title("Проверка открытия и закрытия окна ингредиента")
def test_open_and_close_ingredient_details(driver):
    main_page = MainPage(driver)  # Создаём объект главной страницы
    main_page.open(BASE_URL)  # Открываем главную страницу

    main_page.open_ingredient_details()  # Открываем окно с деталями ингредиента
    assert main_page.get_ingredient_details_title()  # Проверяем, что заголовок окна отображается

    main_page.close_ingredient_details()  # Закрываем окно с деталями ингредиента
    assert main_page.is_ingredient_modal_closed()  # Проверяем, что окно закрылось
