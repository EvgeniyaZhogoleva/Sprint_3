from selenium.webdriver.common.by import By

class Locators:
    # Локаторы для регистрации
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка "Личный кабинет"
    BUTTON_REGIST = (By.XPATH, '//a[text()="Зарегистрироваться"]')  # кнопка "Зарегистрироваться"
    NEW_NAME = (By.XPATH, "//fieldset[1]/div/div/input")  # поле Имя
    NEW_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")  # поле Почта
    NEW_PASSWORD = (By.NAME, "Пароль")  # поле Пароль
    BUTTON_REGIST1 = (By.XPATH, "//button[text()='Зарегистрироваться']") # кнопка "Зарегестрироваться" после заполнения полей
    BUTTON_LOG_IN_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # кнопка "Войти в аккаунт"
    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")  # поле "Email" на экране логина
    BUTTON_IN = (By.XPATH, '//button[text()="Войти"]')  # кнопка "Войти"
    LABLE_LOGIN = (By.XPATH, "//h2[contains(text(),'Вход')]")  # надпись "Вход" на экране авторизации
    ERROR_PASSWORD = (By.XPATH, "//*[text()='Некорректный пароль']")  # надпись "Некорректный пароль" на экране авторизации
    # Локаторы для авторизации
    BUTTON_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')  # кнопка "Оформить заказ" на главной странице
    BUTTON_LOGIN = (By.XPATH, "//a[@href='/login']") #кнопка "Войти" в "Уже зарегестрированы?"
    BUTTON_RECOVER_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")  #кнопка "Восстановить пароль"
    FORGOTTEN_EMAIL = (By.CSS_SELECTOR, 'input.text.input__textfield.text_type_main-default[name=\'name\']')
    BUTTON_RECOVER = (By.XPATH, '//button[text()="Восстановить"]')  # кнопка "Оформить заказ" на главной странице
    # Локаторы для аккаунта
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка "Конструктор"
    LOGO_BURGER = (By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2')  # кнопка "Stellar Burgers"
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # кнопка "Выйти" в личном кабинете
    # Локаторы для конструктора
    BUTTON_BREAD = (By.XPATH, "//span[text()='Булки']")  # кнопка "Булки" в конструктуре
    BREAD_LIST = (By.XPATH, "//h2[contains(text(),'Булки')]")  # список булок
    BUTTON_SAUCE = (By.XPATH, "//span[text()='Соусы']")  # кнопка "Соусы" в конструктуре
    SAUCE_LIST = (By.XPATH, "//h2[contains(text(),'Соусы')]")  # список соусов
    BUTTON_FILLING = (By.XPATH, "//span[text()='Начинки']")  # кнопка "Начинки" в конструктуре
    FILLING_LIST = (By.XPATH, "//h2[contains(text(),'Начинки')]")  # список начинок