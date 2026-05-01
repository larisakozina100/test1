from playwright.sync_api import Page
from utils.auth import login

import pytest

@pytest.fixture
def logged_in_page(page: Page) -> Page:
    login(page)
    return page