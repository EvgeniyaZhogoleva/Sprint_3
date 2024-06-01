from conftest import driver
from locators import Locators

class Test_Constructor:

    def test_bread(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_SAUCE).click()
        driver.find_element(*Locators.BUTTON_BREAD).click()
        assert driver.find_element(*Locators.BREAD_LIST).is_displayed()

    def test_sauce(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_SAUCE).click()
        assert driver.find_element(*Locators.SAUCE_LIST).is_displayed()


    def test_filling(self, driver):  # переход к разделу "Начинки"
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Locators.BUTTON_FILLING).click()
        assert driver.find_element(*Locators.FILLING_LIST).is_displayed()