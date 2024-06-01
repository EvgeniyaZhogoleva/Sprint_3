from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_REGIST).click()
        driver.find_element(*Locators.NEW_NAME).send_keys("Евгения")
        driver.find_element(*Locators.NEW_EMAIL).send_keys("1997zhogoleva_6@ya.ru")
        driver.find_element(*Locators.NEW_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.BUTTON_REGIST1).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_IN),"Войти")


    def test_invalid_password_error(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_LOG_IN_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys("1995zhogoleva_6@ya.ru")
        driver.find_element(*Locators.NEW_PASSWORD).send_keys("12345")
        driver.find_element(*Locators.BUTTON_IN).click()
        assert driver.find_element(*Locators.ERROR_PASSWORD).is_displayed()