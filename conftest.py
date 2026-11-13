import pytest  # Импортируем Pytest
from selenium import webdriver  # Импортируем Selenium для управления браузером

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):  # Фикстура для инициализации драйвера браузера
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()

    driver.maximize_window()
    yield driver

    driver.quit()  # Закрываем браузер после завершения теста