import pytest
from locators import *
from data import *
from auth import standard_auth
import time


@pytest.mark.positive
# case 2.1
def test_add_to_cart(browser, standard_auth):
    # pick item text:
    item_inventory = browser.find_element('xpath', '(//div[@class="inventory_item_name"])[3]').text

    # add item to cart:
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[3]').click()

    # go to cart:
    browser.find_element('xpath', cart_btn).click()

    # check if item picked is the same item in cart:
    item_in_cart = browser.find_element('xpath', '//div[@class="inventory_item_name"]').text

    assert item_inventory == item_in_cart, 'Different item picked'

    # remove item from cart:
    browser.find_element('xpath', cart_remove_btn).click()


@pytest.mark.positive
# case 2.2
def test_remove_from_cart(browser, standard_auth):
    # pick two items and add to cart:
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[2]').click()
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[4]').click()

    # pick cart quantity tag:
    cart_tag_span2 = '<span class="fa-layers-counter shopping_cart_badge"></span>'

    # go to cart:
    browser.find_element('xpath', cart_btn).click()

    # remove items from cart:
    cart_remove_btns = browser.find_elements('xpath', cart_remove_btn)
    for btn in cart_remove_btns:
        btn.click()

    # check if cart quantity tag is missing on page:
    assert cart_tag_span2 not in browser.page_source, 'Items are not removed from cart'


@pytest.mark.positive
# case 2.3
def test_add_item_from_item_card(browser, standard_auth):
    # pick item title:
    item_title3 = browser.find_element('xpath', '(//div[@class="inventory_item_name"])[3]').text

    # find item link and click it:
    browser.find_element('xpath', '(//div[@class="inventory_item_name"])[3]').click()

    # check if item title is the same item title:
    card_item_title3 = browser.find_element('xpath', '//div[@class="inventory_details_name"]').text
    assert item_title3 == card_item_title3, 'Wrong item'

    # add to cart:
    browser.find_element('xpath', '//button[@class="btn_primary btn_inventory"]').click()

    # go to cart:
    browser.find_element('xpath', cart_btn).click()

    # check if item title is the same item title and url is cart url:
    cart_item_title3 = browser.find_element('xpath', '//div[@class="inventory_item_name"]').text
    assert cart_item_title3 == card_item_title3 and browser.current_url == cart_url, 'Wrong url or different item'

    # remove item from cart:
    browser.find_element('xpath', cart_remove_btn).click()


@pytest.mark.positive
# case 2.4
def test_remove_item_from_item_card(browser, standard_auth):
    # pick item text:
    item_title4 = browser.find_element('xpath', '(//div[@class="inventory_item_name"])[2]').text

    # add item to cart:
    browser.find_element('xpath', '(//button[@class="btn_primary btn_inventory"])[2]').click()

    # items quantity in cart:
    cart_tag_before4 = browser.find_element('xpath', cart_tag).text
    assert cart_tag_before4 == '1', 'Wrong quantity of items'

    # go to item card:
    browser.find_element('xpath', '(//div[@class="inventory_item_name"])[2]').click()
    assert item_title4 == 'Sauce Labs Bike Light', 'Wrong item title'

    # click remove button:
    browser.find_element('xpath', card_remove_btn).click()

    # check the button changed:
    btn_txt4 = browser.find_element('xpath', card_add_btn).text
    assert btn_txt4 == 'ADD TO CART', 'Button didn\'t change'
