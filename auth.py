import pytest
import time
from data import *
from locators import *


@pytest.fixture()
def standard_auth(browser):
    browser.get(url)
    browser.find_element('xpath', input_user).send_keys(user)
    browser.find_element('xpath', input_pass).send_keys(pass_word)
    browser.find_element('xpath', login_btn).click()
    time.sleep(2)
    yield standard_auth


@pytest.fixture()
def problem_auth(browser):
    browser.get(url)
    browser.find_element('xpath', input_user).send_keys(problem_user)
    browser.find_element('xpath', input_pass).send_keys(pass_word)
    browser.find_element('xpath', login_btn).click()
    time.sleep(2)
    yield problem_auth

