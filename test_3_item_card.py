import pytest
from data import URLs
from locators import InventoryPage, ItemPage


@pytest.mark.positive
# case 3.1
def test_click_on_item_img(browser, imp_wait, standard_auth):
    # pick item description:
    item_desc = browser.find_elements(*InventoryPage.item_descs)[2].text

    # pick item image and click:
    browser.find_elements(*InventoryPage.item_imgs)[2].click()

    # check if url changed and we can get the same item:
    item_card_desc = browser.find_element(*ItemPage.card_desc).text
    assert browser.current_url != URLs.inventory_url and \
           item_desc == item_card_desc, 'Different item description or wrong url'


@pytest.mark.positive
# case 3.2
def test_click_on_item_title(browser, imp_wait, standard_auth):
    # pick item description:
    item_desc = browser.find_elements(*InventoryPage.item_descs)[3].text

    # pick item title and click:
    browser.find_elements(*InventoryPage.item_names)[3].click()

    # check if url changed and we can get the same item:
    item_card_desc = browser.find_element(*ItemPage.card_desc).text
    assert item_desc == item_card_desc and browser.current_url != URLs.url, 'Different item description or wrong url'
