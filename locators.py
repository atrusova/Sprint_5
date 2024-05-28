from selenium.webdriver.common.by import By


class TestLocators:
    SEARCH_PROFILE = By.XPATH, ".//*[@href = '/account']/p[text()='Личный Кабинет']" # Кнопка "Личный кабинет"

    SEARCH_LINK_REGISTRATION = By.XPATH, ".//a[@href = '/register']" # Ссылка "Зрегистрироваться" на форме входа
    SEARCH_LINK_LOG_IN = By.XPATH, ".//a[@href = '/login']" # Ссылка "Войти" на форме регистрации
    SEARCH_LINK_FORGOT_PASSWORD = By.XPATH, ".//a[@href = '/forgot-password']" # Ссылка "Восстановить пароль" на форме входа

    SEARCH_INPUT_REGISTRATION_NAME = By.XPATH, ".//*[text()='Имя']/following-sibling::input" # Поле "Имя" на форме входа
    SEARCH_INPUT_EMAIL = By.XPATH, ".//*[text()='Email']/following-sibling::input" # Поле "Email" на форме входа
    SEARCH_INPUT_PASS = By.XPATH, ".//*[text()='Пароль']/following-sibling::input" # Поле "Пароль" на форме входа
    SEARCH_SECTION_BAKERY = By.XPATH, ".//span[text()='Булки']" # Вкладка "Булки" на главной
    SEARCH_SECTION_SAUCE = By.XPATH, ".//span[text()='Соусы']" # Вкладка "Соусы" на главной
    SEARCH_SECTION_FILLING = By.XPATH, ".//span[text()='Начинки']" # Вкладка "Начинки" на главной
    SEARCH_CURRENT_SECTION_BAKERY = By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]/*[text()='Булки']" # Активная вкладка "Булки" на главной
    SEARCH_CURRENT_SECTION_SAUCE = By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]/*[text()='Соусы']" # Активная вкладка "Соусы" на главной
    SEARCH_CURRENT_SECTION_FILLING = By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]/*[text()='Начинки']" # Активная вкладка "Начинки" на главной

    SEARCH_BUTTON_LOG_IN_MAIN_PAGE = By.XPATH, ".//button[text()='Войти в аккаунт']" # Кнопка "Войти" на главной
    SEARCH_BUTTON_LOG_IN = By.XPATH, ".//button[text()='Войти']" # Кнопка "Войти" на форме входа
    SEARCH_BUTTON_REGISTRATION = By.XPATH, ".//button[text()='Зарегистрироваться']" # Кнопка "Зарегистрироваться"
    SEARCH_BUTTON_ORDER = By.XPATH, ".//button[text()='Оформить заказ']" # Кнопка "Оформить заказ" на главной
    SEARCH_BUTTON_LOGOUT = By.XPATH, ".//button[text()='Выход']" # Кнопка "Выход"

    SEARCH_PAGE_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']" # Раздел "Конструктор"
    SEARCH_LOGO = By.XPATH, ".//*[@xmlns='http://www.w3.org/2000/svg']" # Логотип
    SEARCH_MAIN_HEAD = By.XPATH, ".//h1[text()='Соберите бургер']" # Заголовок на главной
    SEARCH_TEXT_INCORRECT_PASSWORD = By.XPATH, ".//p[text()='Некорректный пароль']" # Текст валидации о неверном пароле

