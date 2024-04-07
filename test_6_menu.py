import pytest
from selenium.webdriver.support import expected_conditions as ex
from data import URLs
from locators import Menu, AuthPage, AboutPage, InventoryPage, CartPage


@pytest.mark.positive
# case 6.1
def test_positive_logout(browser, imp_wait, standard_auth):
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
def test_positive_about_btn(browser, imp_wait, standard_auth):
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
def test_reset_app_state_positive(browser, exp_wait, standard_auth):
    # add two items to cart:
    browser.find_elements(*InventoryPage.add_btns)[4].click()
    browser.find_elements(*InventoryPage.add_btns)[4].click()

    tag = browser.find_element(*CartPage.cart_tag)
    assert int(tag.text) == 2, 'Wrong items quantity in cart'

    # check if cart quantity tag is 2:
    tag = browser.find_element(*CartPage.cart_tag).text
    assert int(tag) == 2

    # find and click burger menu:
    browser.find_element(*Menu.menu_btn).click()

    # find and click 'reset app state' button:
    reset_btn = browser.find_element(*Menu.reset_btn)
    exp_wait.until(ex.visibility_of(reset_btn))
    reset_btn.click()

    # check if cart is empty:
    items_in_cart = browser.find_elements(*CartPage.cart_tag)
    assert len(items_in_cart) == 0, 'Cart is not empty'

    tag_invisibility = exp_wait.until(ex.invisibility_of_element_located(CartPage.cart_tag))
    assert tag_invisibility, 'Tag is visible, cart is not empty'

    browser.refresh()


@pytest.mark.defect
@pytest.mark.xfail
@pytest.mark.negative
# case 6.4
def test_reset_app_state_negative(browser, exp_wait, standard_auth):
    # check 'add to cart' buttons quantity before:
    add_btns_before = browser.find_elements(*InventoryPage.add_btns)

    # add two items to cart:
    browser.find_elements(*InventoryPage.add_btns)[0].click()
    browser.find_elements(*InventoryPage.add_btns)[1].click()

    tag = browser.find_element(*CartPage.cart_tag)
    assert int(tag.text) == 2, 'Wrong items quantity in cart'

    # find and click burger menu:
    browser.find_element(*Menu.menu_btn).click()

    # find and click 'reset app state' button:
    browser.find_element(*Menu.reset_btn).click()

    # check if cart is empty:
    items_in_cart = browser.find_elements(*InventoryPage.item_names)
    assert len(items_in_cart) == 0, 'Cart is not empty'

    tag_invisibility = exp_wait.until(ex.invisibility_of_element_located(CartPage.cart_tag))
    assert tag_invisibility, 'Tag is visible, cart is not empty'

    # check all 'add to cart' buttons are unpressed by its quantity before and after:
    add_btns_after = browser.find_elements(*InventoryPage.add_btns)
    assert len(add_btns_before) != len(add_btns_after), 'Buttons are not unpressed after reset the app'

    browser.refresh()
