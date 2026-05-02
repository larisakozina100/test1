import pytest
from playwright.sync_api import Page
from utils.auth import login

@pytest.fixture
def logged_in_page(page: Page, base_url: str) -> Page:
    login(page, base_url)
    return page