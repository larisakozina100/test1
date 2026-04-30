from playwright.sync_api import Page, expect
from utils.auth import login

def test_add_item_to_cart(page: Page) -> None:
    login(page)

    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    
    expect(page.locator('.shopping_cart_badge')).to_have_text('1')

