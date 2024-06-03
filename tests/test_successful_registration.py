from faker import Faker
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import email


def generate_random_email():
    dummy = Faker()
    return dummy.email()


class TestRegistration:
    def test_successful_registration(self, driver):
        email_address = generate_random_email()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_REGIST).click()
        driver.find_element(*Locators.NEW_NAME).send_keys("Евгения")
        driver.find_element(*Locators.NEW_EMAIL).send_keys(email_address)
        driver.find_element(*Locators.NEW_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.BUTTON_REGIST1).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_IN), "Войти")


    def test_invalid_password_error(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_LOG_IN_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.NEW_PASSWORD).send_keys("12345")
        driver.find_element(*Locators.BUTTON_IN).click()
        assert driver.find_element(*Locators.ERROR_PASSWORD).is_displayed()