from playwright.sync_api import expect
from utils.locators import CART_BADGE, ADD_BACKPACK_BUTTON
from utils.routes import INVENTORY_PATH

def test_add_item_to_cart(logged_in_page, base_url: str) -> None:
    page = logged_in_page

    expect(page).to_have_url(base_url + INVENTORY_PATH)

    page.locator(ADD_BACKPACK_BUTTON).click()

    expect(page.locator(CART_BADGE)).to_have_text("1")