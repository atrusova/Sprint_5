from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from data import main_email, main_password


class TestAuthentication:

    def test_auth_through_main_page_visible_button_order(self, driver):
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(main_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASS).send_keys(main_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_BUTTON_ORDER))

    def test_auth_through_profile_visible_button_order(self, driver):
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(main_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASS).send_keys(main_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_BUTTON_ORDER))

    def test_auth_through_registration_page_visible_button_order(self, driver):
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_LINK_REGISTRATION).click()
        driver.find_element(*TestLocators.SEARCH_LINK_LOG_IN).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(main_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASS).send_keys(main_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_BUTTON_ORDER))

    def test_auth_through_forgot_password_visible_button_order(self, driver):
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_LINK_FORGOT_PASSWORD).click()
        driver.find_element(*TestLocators.SEARCH_LINK_LOG_IN).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(main_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASS).send_keys(main_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_BUTTON_ORDER))

    def test_logout_through_profile_visible_button_login(self, driver):
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(main_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASS).send_keys(main_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_PROFILE))
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_BUTTON_LOGOUT))
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOGOUT).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_BUTTON_LOG_IN))
