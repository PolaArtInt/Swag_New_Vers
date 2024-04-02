import pytest
from locators import *
from data import *


# case 1.1
# standard auth:
@pytest.mark.positive
def test_standart_login(browser):
    browser.get(URLs.url)
    browser.find_element(*input_user).send_keys(Auth.user)
    browser.find_element(*input_pass).send_keys(Auth.pass_word)
    browser.find_element(*login_btn).click()

    assert browser.current_url == URLs.inventory_url, 'Wrong url'
    assert prod_header, 'Wrong page header'


# case 1.2
@pytest.mark.positive
def test_auth_positive_locked_out_user(browser):
    browser.get(URLs.url)
    browser.find_element(*input_user).send_keys(Auth.locked_user)
    browser.find_element(*input_pass).send_keys(Auth.pass_word)
    browser.find_element(*login_btn).click()

    assert locked_msg, 'Login error'
    assert browser.current_url == URLs.url, 'Wrong url'


# case 1.3
@pytest.mark.positive
def test_auth_positive_problem_user(browser):
    browser.get(URLs.url)
    browser.find_element(*input_user).send_keys(Auth.problem_user)
    browser.find_element(*input_pass).send_keys(Auth.pass_word)
    browser.find_element(*login_btn).click()

    assert browser.current_url == URLs.inventory_url, 'Wrong url'


# case 1.4
@pytest.mark.slow
def test_auth_positive_performance_glitch_user(browser):
    browser.get(URLs.url)
    browser.find_element(*input_user).send_keys(Auth.glitch_user)
    browser.find_element(*input_pass).send_keys(Auth.pass_word)
    browser.find_element(*login_btn).click()

    assert browser.current_url == URLs.inventory_url, 'Wrong url'


# case 1.5
@pytest.mark.negative
def test_auth_negative_wrong_login(browser):
    browser.get(URLs.url)
    browser.find_element(*input_user).send_keys('user')
    browser.find_element(*input_pass).send_keys('user')
    browser.find_element(*login_btn).click()

    assert login_err_msg, 'Wrong login'
    assert browser.current_url == URLs.url, 'Wrong url'
