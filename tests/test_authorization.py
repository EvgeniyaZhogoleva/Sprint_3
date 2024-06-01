from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

class Test_Authorization:

    def test_login_methods1(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_LOG_IN_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys("zhogoleva_6123@ya.ru")
        driver.find_element(*Locators.NEW_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER), "Оформить заказ")

    def test_login_methods2(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys("zhogoleva_6123@ya.ru")
        driver.find_element(*Locators.NEW_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER),"Оформить заказ")


    def test_login_methods3(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_REGIST).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN)).click()
        driver.find_element(*Locators.EMAIL).send_keys("zhogoleva_6123@ya.ru")
        driver.find_element(*Locators.NEW_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER),"Оформить заказ")


    def test_login_methods4(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_LOG_IN_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_RECOVER_PASSWORD)).click()
        driver.find_element(*Locators.FORGOTTEN_EMAIL).send_keys("zhogoleva_6123@ya.ru")
        driver.find_element(*Locators.BUTTON_RECOVER).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(Locators.BUTTON_LOGIN)).click()
        driver.find_element(*Locators.EMAIL).send_keys("zhogoleva_6123@ya.ru")
        driver.find_element(*Locators.NEW_PASSWORD).send_keys("123456")
        driver.find_element(*Locators.BUTTON_IN).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER),"Оформить заказ")