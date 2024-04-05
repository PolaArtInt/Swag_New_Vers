import pytest
from data import URLs, TestAuth
from locators import InventoryPage, AuthPage


# case 1.1
# standard auth:
@pytest.mark.positive
def test_standart_login(browser, standard_auth):
    inventory_header = browser.find_element(*InventoryPage.prod_header).text
    inventory_cards = browser.find_elements(*InventoryPage.item_cards)

    assert browser.current_url == URLs.inventory_url, 'Wrong url'
    assert inventory_header == 'Products', 'Wrong page header'
    assert len(inventory_cards) > 0, 'There are no items on the inventory page'


# case 1.2
@pytest.mark.positive
def test_auth_positive_locked_out_user(browser, locked_out_auth):
    assert AuthPage.locked_msg, 'Login error'
    assert browser.current_url == URLs.url, 'Wrong url'


# case 1.3
@pytest.mark.positive
def test_auth_positive_problem_user(browser, problem_auth):
    assert browser.current_url == URLs.inventory_url, 'Wrong url'
    assert InventoryPage.prod_header, 'Wrong page header'


# case 1.4
@pytest.mark.slow
def test_auth_positive_performance_glitch_user(browser, glitch_auth):
    assert browser.current_url == URLs.inventory_url, 'Wrong url'
    assert InventoryPage.prod_header, 'Wrong page header'


# case 1.5
@pytest.mark.negative
def test_auth_negative_wrong_login(browser):
    browser.get(URLs.url)
    browser.find_element(*AuthPage.input_user).send_keys(TestAuth.wrong_user)
    browser.find_element(*AuthPage.input_pass).send_keys(TestAuth.wrong_password)
    browser.find_element(*AuthPage.login_btn).click()

    assert AuthPage.login_err_msg, 'Wrong login'
    assert browser.current_url == URLs.url, 'Wrong url'
    print(f'\nWrong login user...')
