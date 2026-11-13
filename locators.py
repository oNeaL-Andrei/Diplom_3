from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, ".AppHeader_header__link__3D_hX[href='/']")  # Кнопка перехода в конструктор
    BURGER_INGREDIENT = (By.CSS_SELECTOR, "a[class^='BurgerIngredient_ingredient']")  # Карточки ингредиентов
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p[class^='counter_counter__num']")  # Счётчик ингредиента
    INGREDIENT_MODAL_TITLE = (By.CSS_SELECTOR, "h2[class^='Modal_modal__title']")  # Заголовок окна с деталями ингредиента
    ORDER_NUMBER = (By.CSS_SELECTOR, "h2[class^='Modal_modal__title_shadow']")  # Номер заказа в окне подтверждения
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, "section[class^='Modal_modal_opened'] button[class*='Modal_modal__close__']")  # Кнопка закрытия окна
    BUN_TOP = (By.XPATH, "//span[@class='constructor-element__text' and contains(text(), 'верх')]")  # Верхняя зона конструктора
    BUN_BOTTOM = (By.XPATH, "//span[@class='constructor-element__text' and contains(text(), 'низ')]")  # Нижняя зона конструктора
    ORDER_BUTTON = (By.CSS_SELECTOR, "button[class^='button_button__'][class*='type_primary']")  # Кнопка оформления заказа

class FeedPageLocators:
    FEED_BUTTON = (By.CSS_SELECTOR, "a[href='/feed']")  # Кнопка перехода в ленту заказов
    TOTAL_ORDERS_COUNT = (By.CSS_SELECTOR, "div[class^='OrderFeed_ordersData'] > div:nth-of-type(2) p[class^='OrderFeed_number']")  # Выполнено за всё время
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")  # Выполнено за сегодня
    IN_PROGRESS_ORDER = (By.CSS_SELECTOR, "div[class^='OrderFeed_orderStatusBox'] ul[class^='OrderFeed_orderListReady'] li.text_type_digits-default")  # Номер заказа в работе

class LoginPageLocators:
    EMAIL_FIELD = (By.NAME, "name")  # Поле электронной почты
    PASSWORD_FIELD = (By.NAME, "Пароль")  # Поле пароля
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class*='button_button_type_primary']")  # Кнопка входа
