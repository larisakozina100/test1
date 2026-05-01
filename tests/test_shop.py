from playwright.sync_api import expect
from utils.locators import CART_BADGE, ADD_BACKPACK_BUTTON

def test_add_item_to_cart(logged_in_page):
    page = logged_in_page

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.locator(ADD_BACKPACK_BUTTON).click()

    expect(page.locator(CART_BADGE)).to_have_text("1")

