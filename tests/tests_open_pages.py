from data import main_email, main_password
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestOpenPages:

    def test_open_profile_visible_button_logout(self, driver):
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(main_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASS).send_keys(main_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_BUTTON_ORDER))
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        assert WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_BUTTON_LOGOUT))

    def test_open_constructor_from_profile_click_constructor_visible_button_order(self, driver):
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(main_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASS).send_keys(main_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_PROFILE))
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_PAGE_CONSTRUCTOR))
        driver.find_element(*TestLocators.SEARCH_PAGE_CONSTRUCTOR).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_BUTTON_ORDER))
        assert driver.find_element(*TestLocators.SEARCH_BUTTON_ORDER).text == "Оформить заказ"

    def test_open_constructor_from_profile_click_logo_visible_button_order(self, driver):
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_EMAIL).send_keys(main_email)
        driver.find_element(*TestLocators.SEARCH_INPUT_PASS).send_keys(main_password)
        driver.find_element(*TestLocators.SEARCH_BUTTON_LOG_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_PROFILE))
        driver.find_element(*TestLocators.SEARCH_PROFILE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_PAGE_CONSTRUCTOR))
        driver.find_element(*TestLocators.SEARCH_LOGO).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_BUTTON_ORDER))
        assert driver.find_element(*TestLocators.SEARCH_BUTTON_ORDER).text == "Оформить заказ"

    def test_switch_between_section_filling(self, driver):
        driver.find_element(*TestLocators.SEARCH_SECTION_FILLING).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_CURRENT_SECTION_FILLING))

    def test_switch_between_section_sauce(self, driver):
        driver.find_element(*TestLocators.SEARCH_SECTION_SAUCE).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_CURRENT_SECTION_SAUCE))

    def test_switch_between_section_bakery(self, driver):
        driver.find_element(*TestLocators.SEARCH_SECTION_FILLING).click()
        driver.find_element(*TestLocators.SEARCH_SECTION_BAKERY).click()
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SEARCH_CURRENT_SECTION_BAKERY))
