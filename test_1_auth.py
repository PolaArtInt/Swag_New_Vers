import pytest
from locators import *
from data import *


# case 1.1
# standard auth:
@pytest.mark.positive
def test_standart_login(browser):
    browser.get(url)
    browser.find_element(*input_user).send_keys(user)
    browser.find_element(*input_pass).send_keys(pass_word)
    browser.find_element(*login_btn).click()

    assert browser.current_url == inventory_url, 'Wrong url'
    assert prod_header, 'Wrong page header'


# case 1.2
@pytest.mark.positive
def test_auth_positive_locked_out_user(browser):
    browser.get(url)
    browser.find_element(*input_user).send_keys(locked_user)
    browser.find_element(*input_pass).send_keys(pass_word)
    browser.find_element(*login_btn).click()

    assert locked_msg, 'Login error'
    assert browser.current_url == url, 'Wrong url'


# case 1.3
@pytest.mark.positive
def test_auth_positive_problem_user(browser):
    browser.get(url)

    browser.find_element(*input_user).send_keys(problem_user)
    browser.find_element(*input_pass).send_keys(pass_word)
    browser.find_element(*login_btn).click()

    assert browser.current_url == inventory_url, 'Wrong url'


# case 1.4
@pytest.mark.slow
def test_auth_positive_performance_glitch_user(browser):
    browser.get(url)

    browser.find_element(*input_user).send_keys(glitch_user)
    browser.find_element(*input_pass).send_keys(pass_word)
    browser.find_element(*login_btn).click()

    assert browser.current_url == inventory_url, 'Wrong url'


# case 1.5
@pytest.mark.negative
def test_auth_negative_wrong_login(browser):
    browser.get(url)
    browser.find_element(*input_user).send_keys('user')
    browser.find_element(*input_pass).send_keys('user')
    browser.find_element(*login_btn).click()

    assert login_err_msg, 'Wrong login'
    assert browser.current_url == url, 'Wrong url'
