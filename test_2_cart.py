import pytest
from selenium.webdriver.support import expected_conditions as ec
from data import URLs
from locators import InventoryPage, CartPage, ItemPage


@pytest.mark.positive
# case 2.1
def test_add_to_cart(browser, imp_wait, standard_auth):
    # pick item text:
    item_title = browser.find_elements(*InventoryPage.item_names)[3].text

    # add item to cart:
    browser.find_elements(*InventoryPage.add_btns)[3].click()

    # check if cart quantity tag is equal to 1 now:
    tag = browser.find_element(*CartPage.cart_tag).text
    assert int(tag) == 1, 'Wrong items quantity in cart'

    # go to cart:
    browser.find_element(*CartPage.cart_btn).click()

    # check if item picked is the same item in cart:
    cart_item_title = browser.find_element(*InventoryPage.item_names).text
    assert item_title == cart_item_title, 'Different item picked'

    # remove item from cart:
    browser.find_element(*CartPage.cart_remove_btn).click()

    # check if cart is empty:
    items_in_cart = browser.find_elements(*InventoryPage.item_names)
    assert len(items_in_cart) == 0, 'Cart is not empty'


@pytest.mark.positive
# case 2.2
def test_remove_from_cart(browser, wait, standard_auth):
    # pick 3 items and add to cart:
    browser.find_elements(*InventoryPage.add_btns)[5].click()
    browser.find_elements(*InventoryPage.add_btns)[1].click()
    browser.find_elements(*InventoryPage.add_btns)[3].click()

    # check if cart quantity tag is equal to 3:
    tag = browser.find_element(*CartPage.cart_tag)
    assert int(tag.text) == 3, 'Cart is empty'

    # go to cart:
    browser.find_element(*CartPage.cart_btn).click()

    items_in_cart = browser.find_elements(*InventoryPage.item_names)
    assert len(items_in_cart) == 3, 'Cart is empty'

    # remove all items from cart:
    cart_remove_btns = browser.find_elements(*CartPage.cart_remove_btn)
    for btn in cart_remove_btns:
        btn.click()

    # check if cart is empty:
    items_in_cart = browser.find_elements(*InventoryPage.item_names)
    assert len(items_in_cart) == 0, 'Cart is not empty'

    tag_invisibility = wait.until(ec.invisibility_of_element_located(CartPage.cart_tag))
    # tag_invisibility = wait.until(ec.invisibility_of_element(tag))
    assert tag_invisibility, 'Tag is visible, cart is not empty'


@pytest.mark.positive
# case 2.3
def test_add_item_from_item_card(browser, imp_wait, standard_auth):
    # pick item title click it and go to item card:
    item_title = browser.find_elements(*InventoryPage.item_names)[3].text
    browser.find_elements(*InventoryPage.item_names)[3].click()

    # check if item title is the same item title:
    card_item_title = browser.find_element(*ItemPage.card_name).text
    assert item_title == card_item_title, 'Wrong item'

    # add item to cart from item page:
    browser.find_element(*ItemPage.card_add_btn).click()

    # go to cart:
    browser.find_element(*CartPage.cart_btn).click()

    # check if item title is the same item title and url is cart url:
    cart_item_title = browser.find_element(*InventoryPage.item_names).text
    assert cart_item_title == card_item_title and browser.current_url == URLs.cart_url, 'Wrong url or different item'

    # remove item from cart:
    browser.find_element(*CartPage.cart_remove_btn).click()


@pytest.mark.positive
# case 2.4
def test_remove_item_from_item_card(browser, wait, standard_auth):
    # pick item text and add item to cart:
    item_title_before = browser.find_elements(*InventoryPage.item_names)[2].text
    browser.find_elements(*InventoryPage.add_btns)[2].click()

    # check if items quantity in cart is equal to 1:
    tag = browser.find_element(*CartPage.cart_tag)
    assert int(tag.text) == 1, 'Wrong quantity of items'

    # go to item card:
    browser.find_elements(*InventoryPage.item_names)[2].click()

    # check item title in card:
    item_title_after = browser.find_element(*ItemPage.card_name).text
    assert item_title_before == item_title_after, 'Wrong item title'

    # click remove button:
    browser.find_element(*ItemPage.card_remove_btn).click()

    # check the button changed:
    btn_txt = browser.find_element(*ItemPage.card_add_btn).text
    assert btn_txt == 'ADD TO CART', 'Button is not changed'

    # check if cart is empty:
    items_in_cart = browser.find_elements(*InventoryPage.item_names)
    assert len(items_in_cart) == 0, 'Cart is not empty'

    tag_invisibility = wait.until(ec.invisibility_of_element_located(CartPage.cart_tag))
    # tag_invisibility = wait.until(ec.invisibility_of_element(tag))
    assert tag_invisibility, 'Tag is visible, cart is not empty'
