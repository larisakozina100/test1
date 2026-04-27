from playwright.sync_api import Page, expect

def test_login_with_wrong_paasword_shows_error(page: Page) -> None:
    page.goto('https://www.saucedemo.com/')

    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('wrong_password')
    page.get_by_role('button', name='Login').click()

    expect(page.locator('[data-test="error"]')).to_be_visible()
    expect(page.locator('[data-test="error"]')).to_contain_text('Username and password do not match'
    )
    