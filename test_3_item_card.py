import pytest
from data import *


@pytest.mark.positive
# case 3.1
def test_click_on_item_img(browser, standard_auth):
    # pick item description:
    item_desc = browser.find_element('xpath', '(//div[@class="inventory_item_desc"])[2]').text

    # pick item image and click:
    browser.find_element('xpath', '(//img[@class="inventory_item_img"])[2]').click()

    # check if url changed and we can get the same item:
    item_card_desc = browser.find_element('xpath', '//div[@class="inventory_details_desc"]').text
    assert browser.current_url != URLs.inventory_url and \
           item_desc == item_card_desc, 'Different item description or wrong url'


@pytest.mark.positive
# case 3.2
def test_click_on_item_title(browser, standard_auth):
    # pick item description:
    item_desc = browser.find_element('xpath', '(//div[@class="inventory_item_desc"])[3]').text

    # pick item title and click:
    browser.find_element('xpath', '(//div[@class="inventory_item_name"])[3]').click()

    # check if url changed and we can get the same item:
    item_card_desc = browser.find_element('xpath', '//div[@class="inventory_details_desc"]').text
    assert item_desc == item_card_desc and browser.current_url != URLs.url, 'Different item description or wrong url'
