from playwright.sync_api import Page

def login(page: Page, base_url: str) -> None:
    page.goto(base_url)
    page.get_by_placeholder('Username').fill('standard_user')
    page.get_by_placeholder('Password').fill('secret_sauce')
    page.get_by_role('button', name='Login').click()