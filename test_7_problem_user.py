import pytest
from data import URLs
from locators import InventoryPage


@pytest.mark.defect
@pytest.mark.xfail
@pytest.mark.negative
def test_auth_positive_problem_user(browser, imp_wait, problem_auth):
    imgs = browser.find_elements(*InventoryPage.item_imgs)
    broken_url_sample = 'WithGarbageOnItToBreakTheUrl'

    for img in imgs:
        assert broken_url_sample in img.get_dom_attribute('src'), 'Image not visible'

    assert browser.current_url == URLs.inventory_url, 'Wrong url'

