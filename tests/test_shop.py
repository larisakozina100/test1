from playwright.sync_api import Page, expect

def test_add_item_to_cart(page: Page) -> None:
    page.goto('https://www.saucedemo.com/')

    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret_sauce')
    page.get_by_role('button', name='Login').click()

    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
    expect(page.get_by_text('Products')).to_be_visible()

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    
    expect(page.locator('.shopping_cart_badge')).to_have_text('1')

