from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import email, password

class TestPersonalAccount:

    def test_go_to_account(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.NEW_PASSWORD).send_keys(password)
        assert WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_IN))


    def test_go_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.NEW_PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_IN).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_CONSTRUCTOR))
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER),"Оформить заказ")


    def test_go_to_logo(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.NEW_PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_IN).click()
        driver.find_element(*Locators.LOGO_BURGER).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER),"Оформить заказ")


    def test_logout(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.NEW_PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_IN).click()
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGOUT))
        assert WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Locators.LOGO_BURGER))