import pytest
from data import TestAuth, URLs
from locators import InventoryPage, CartPage, CheckoutPage


@pytest.mark.positive
# case 4.1
def test_positive_order(browser, standard_auth):
    # pick items and add it to cart:
    browser.find_elements(*InventoryPage.add_btns)[5].click()
    browser.find_elements(*InventoryPage.add_btns)[0].click()

    # go to cart:
    browser.find_element(*CartPage.cart_btn).click()

    # go to checkout:
    browser.find_element(*CheckoutPage.checkout_btn).click()

    # fill a form:
    browser.find_element(*CheckoutPage.input_fname).send_keys(TestAuth.fake_user_fname)
    browser.find_element(*CheckoutPage.input_lname).send_keys(TestAuth.fake_user_lname)
    browser.find_element(*CheckoutPage.input_zipcode).send_keys(TestAuth.fake_zip)

    # click 'continue' button:
    browser.find_element(*CheckoutPage.continue_btn).click()

    # click 'finish' button:
    browser.find_element(*CheckoutPage.finish_btn).click()

    # check url and success message:
    curr_url = browser.current_url
    assert curr_url == URLs.checkout_url and CheckoutPage.complete_msg, 'Wrong url'

    # check if cart is empty:
    items_in_cart = browser.find_elements(*InventoryPage.item_names)
    assert len(items_in_cart) == 0, 'Cart is not empty'


@pytest.mark.defect
@pytest.mark.xfail
@pytest.mark.negative
# case 4.2
def test_negative_empty_order(browser, standard_auth):
    # go to cart:
    browser.find_element(*CartPage.cart_btn).click()

    # check if cart is empty:
    items_in_cart = browser.find_elements(*InventoryPage.item_names)
    assert len(items_in_cart) == 0, 'Cart is not empty'

    # go to checkout:
    browser.find_element(*CheckoutPage.checkout_btn).click()

    # fill a form:
    browser.find_element(*CheckoutPage.input_fname).send_keys(TestAuth.fake_user_fname)
    browser.find_element(*CheckoutPage.input_lname).send_keys(TestAuth.fake_user_lname)
    browser.find_element(*CheckoutPage.input_zipcode).send_keys(TestAuth.fake_zip)

    # click 'continue' button:
    browser.find_element(*CheckoutPage.continue_btn).click()

    # click 'finish' button:
    browser.find_element(*CheckoutPage.finish_btn).click()

    # check url and success message:
    curr_url = browser.current_url
    assert not curr_url == URLs.checkout_url and not CheckoutPage.complete_msg, 'Shopping cart is empty, wrong checkout'
