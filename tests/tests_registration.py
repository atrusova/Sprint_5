from conftest import driver, user_email, user_password
from data import name
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestRegistration:

    def test_registration_full_data_success_registration(self, driver, user_email, user_password):
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_LINK_REGISTRATION).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_REGISTRATION_NAME).send_keys(name)
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(user_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASS).send_keys(user_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_BUTTON_LOG_IN))

    def test_registration_password_less_than_6_show_text_incorrect_password(self, driver, user_email):
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_LINK_REGISTRATION).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_REGISTRATION_NAME).send_keys(name)
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(user_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASS).send_keys('009')
        driver.find_element(*TestLocators.SEARCH_BUTTON_REGISTRATION).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_TEXT_INCORRECT_PASSWORD))

