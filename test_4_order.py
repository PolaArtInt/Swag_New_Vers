import pytest
from locators import *
from data import *
from auth import standard_auth


@pytest.mark.positive
# case 4.1
def test_positive_order(browser, standard_auth):
    # pick item and add it to cart:
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[1]').click()

    # go to cart:
    browser.find_element('xpath', cart_btn).click()

    # go to checkout:
    browser.find_element('xpath', checkout_btn).click()

    # fill a form:
    browser.find_element('xpath', input_fname).send_keys(fake_user_fname)
    browser.find_element('xpath', input_lname).send_keys(fake_user_lname)
    browser.find_element('xpath', input_zipcode).send_keys(fake_zip)

    # click 'continue' button:
    browser.find_element('xpath', continue_btn).click()

    # click 'finish' button:
    browser.find_element('xpath', finish_btn).click()

    # check url and success message:
    curr_url = browser.current_url
    assert curr_url == checkout_url and complete_msg, 'Wrong url'

    # check if cart is empty:
    assert cart_tag not in browser.page_source, 'Shopping cart is not empty'


@pytest.mark.xfail
@pytest.mark.negative
# case 4.2
def test_negative_empty_order(browser, standard_auth):
    # go to cart:
    browser.find_element('xpath', cart_btn).click()

    # go to checkout:
    browser.find_element('xpath', checkout_btn).click()

    # fill a form:
    browser.find_element('xpath', input_fname).send_keys(fake_user_fname)
    browser.find_element('xpath', input_lname).send_keys(fake_user_lname)
    browser.find_element('xpath', input_zipcode).send_keys(fake_zip)

    # click 'continue' button:
    browser.find_element('xpath', continue_btn).click()

    # click 'finish' button:
    browser.find_element('xpath', finish_btn).click()

    # check url and success message:
    curr_url = browser.current_url
    assert not curr_url == checkout_url and not complete_msg, 'Shopping cart is empty, wrong checkout'
