from pages.base_page import BasePage  # Импортируем базовый класс страницы
from locators import LoginPageLocators  # Импортируем локаторы страницы входа

class LoginPage(BasePage):  # Класс страницы входа
    def enter_email(self, email):
        self.find_element(LoginPageLocators.EMAIL_FIELD).send_keys(email)  # Вводим электронную почту

    def enter_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)  # Вводим пароль

    def click_login_button(self):
        button = self.find_element(LoginPageLocators.LOGIN_BUTTON)  # Находим кнопку входа

        if self.driver.capabilities["browserName"] == "firefox":
            self.driver.execute_script("arguments[0].click();", button)  # Нажимаем кнопку через JavaScript в Firefox
        else:
            self.click_element(LoginPageLocators.LOGIN_BUTTON)  # Нажимаем обычным способом в Chrome

    def login(self, email, password):
        self.enter_email(email)  # Вводим электронную почту
        self.enter_password(password)  # Вводим пароль
        self.click_login_button()  # Нажимаем кнопку входа
