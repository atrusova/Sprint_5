import pytest
import options
import random as r
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    option.add_argument('--window-size=1920,1080')
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()


@pytest.fixture()
def user_email():
    number = r.randint(1, 99999)
    email = f'anastasiia_trusova_9_' + str(number) + '@gmail.com'
    return email


@pytest.fixture()
def user_password():
    number = r.randint(1, 99999)
    password = f'AnastasBurger' + str(number)
    return password



