import pytest
from locators import *
from data import *


@pytest.mark.positive
# case 2.1
def test_add_to_cart(browser, standard_auth):
    # pick item text:
    item_title = browser.find_element('xpath', '(//div[@class="inventory_item_name"])[3]').text

    # add item to cart:
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[3]').click()

    # check if cart quantity tag is equal to 1 now:
    tag = browser.find_element(*CartPage.cart_tag).text
    assert tag == '1'

    # go to cart:
    browser.find_element(*CartPage.cart_btn).click()

    # check if item picked is the same item in cart:
    cart_item_title = browser.find_element('xpath', '//div[@class="inventory_item_name"]').text
    assert item_title == cart_item_title, 'Different item picked'

    # remove item from cart:
    browser.find_element(*CartPage.cart_remove_btn).click()

    # check if cart is empty:
    assert CartPage.cart_quantity_tag not in browser.page_source, 'Shopping cart is not empty'


@pytest.mark.positive
# case 2.2
def test_remove_from_cart(browser, standard_auth):
    # pick 3 items and add to cart:
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[2]').click()
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[4]').click()
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[1]').click()

    # check if cart quantity tag is more than zero:
    tag = browser.find_element(*CartPage.cart_tag).text
    assert tag != 0

    # go to cart:
    browser.find_element(*CartPage.cart_btn).click()

    # remove all items from cart:
    cart_remove_btns = browser.find_elements(*CartPage.cart_remove_btn)
    for btn in cart_remove_btns:
        btn.click()

    # check if cart quantity tag is missing on page:
    assert CartPage.cart_quantity_tag not in browser.page_source, 'Shopping cart is not empty'


@pytest.mark.positive
# case 2.3
def test_add_item_from_item_card(browser, standard_auth):
    # pick item title:
    item_title = browser.find_element('xpath', '(//div[@class="inventory_item_name"])[3]').text

    # find item link and click it:
    browser.find_element('xpath', '(//div[@class="inventory_item_name"])[3]').click()

    # check if item title is the same item title:
    card_item_title = browser.find_element('xpath', '//div[@class="inventory_details_name"]').text
    assert item_title == card_item_title, 'Wrong item'

    # add to cart:
    browser.find_element('xpath', '//button[@class="btn_primary btn_inventory"]').click()

    # go to cart:
    browser.find_element(*CartPage.cart_btn).click()

    # check if item title is the same item title and url is cart url:
    cart_item_title = browser.find_element('xpath', '//div[@class="inventory_item_name"]').text
    assert cart_item_title == card_item_title and browser.current_url == URLs.cart_url, 'Wrong url or different item'

    # remove item from cart:
    browser.find_element(*CartPage.cart_remove_btn).click()


@pytest.mark.positive
# case 2.4
def test_remove_item_from_item_card(browser, standard_auth):
    # pick item text:
    item_title = browser.find_element('xpath', '(//div[@class="inventory_item_name"])[2]').text

    # add item to cart:
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[2]').click()

    # items quantity in cart:
    cart_tag_before = browser.find_element(*CartPage.cart_tag).text
    assert cart_tag_before == '1', 'Wrong quantity of items'

    # go to item card:
    browser.find_element('xpath', '(//div[@class="inventory_item_name"])[2]').click()
    assert item_title == 'Sauce Labs Bike Light', 'Wrong item title'

    # click remove button:
    browser.find_element(*ItemPage.card_remove_btn).click()

    # check the button changed:
    btn_txt = browser.find_element(*ItemPage.card_add_btn).text
    assert btn_txt == 'ADD TO CART', 'Button didn\'t change'
