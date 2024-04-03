import pytest
from data import *
from locators import *


@pytest.mark.positive
# case 6.1
def test_positive_logout(browser, standard_auth):
    # find and click burger menu:
    browser.find_element(*Menu.menu_btn).click()

    # find and click 'logout' button:
    browser.find_element(*Menu.logout_btn).click()

    # check if we are on login page and 'Login' button appears:
    assert browser.current_url == URLs.login_url, 'Wrong url'

    log_btn_text = browser.find_element(*AuthPage.login_btn).get_attribute('value')
    assert log_btn_text == 'LOGIN', 'Login button not found'


@pytest.mark.positive
# case 6.2
def test_positive_about_btn(browser, standard_auth):
    # find and click burger menu:
    browser.find_element(*Menu.menu_btn).click()

    # find and click 'about' button:
    browser.find_element(*Menu.about_btn).click()

    # check expected url and title:
    curr_title = browser.title
    assert browser.current_url == URLs.about_url and \
           curr_title == AboutPage.exp_title, 'Wrong page url or title'


@pytest.mark.positive
# case 6.3
def test_reset_app_state_positive(browser, standard_auth):
    # add two items to cart:
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[4]').click()
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[5]').click()

    # find and click burger menu:
    browser.find_element(*Menu.menu_btn).click()

    # find and click 'reset app state' button:
    browser.find_element(*Menu.reset_btn).click()

    # check if cart is empty:
    assert CartPage.cart_quantity_tag not in browser.page_source, 'Shopping cart is not empty'

    browser.refresh()


@pytest.mark.xfail
@pytest.mark.negative
# case 6.4
def test_reset_app_state_negative(browser, standard_auth):
    # check 'add to cart' buttons quantity before:
    add_btns_before = browser.find_elements('xpath', InventoryPage.add_btns)
    print(f'\n{len(add_btns_before)}')

    # add two items to cart:
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[2]').click()
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[1]').click()

    # find and click burger menu:
    browser.find_element(*Menu.menu_btn).click()

    # find and click 'reset app state' button:
    browser.find_element(*Menu.reset_btn).click()

    # check if cart is empty:
    assert CartPage.cart_quantity_tag not in browser.page_source, 'Shopping cart is not empty'

    # check all 'add to cart' buttons are unpressed by its quantity before and after:
    add_btns_after = browser.find_elements('xpath', InventoryPage.add_btns)
    print(f'\n{len(add_btns_after)}')
    assert len(add_btns_before) != len(add_btns_after), 'Buttons are not unpressed after reset the app'

    browser.refresh()
