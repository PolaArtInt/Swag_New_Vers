import pytest
from data import *
from locators import *


@pytest.fixture()
def standard_auth(browser):
    browser.get(url)
    browser.find_element('xpath', input_user).send_keys(user)
    browser.find_element('xpath', input_pass).send_keys(pass_word)
    browser.find_element('xpath', login_btn).click()
    yield standard_auth


@pytest.fixture()
def problem_auth(browser):
    browser.get(url)
    browser.find_element('xpath', input_user).send_keys(problem_user)
    browser.find_element('xpath', input_pass).send_keys(pass_word)
    browser.find_element('xpath', login_btn).click()
    yield problem_auth


@pytest.fixture()
def locked_out_auth(browser):
    browser.get(url)
    browser.find_element('xpath', input_user).send_keys(locked_user)
    browser.find_element('xpath', input_pass).send_keys(pass_word)
    browser.find_element('xpath', login_btn).click()
    yield locked_out_auth


@pytest.fixture()
def glitch_auth(browser):
    browser.get(url)
    browser.find_element('xpath', input_user).send_keys(glitch_user)
    browser.find_element('xpath', input_pass).send_keys(pass_word)
    browser.find_element('xpath', login_btn).click()
    yield glitch_auth

