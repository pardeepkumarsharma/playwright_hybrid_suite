
from playwright.sync_api import sync_playwright, Playwright

def test_run(playwright:Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    # create two isolated browser contexts
    user_context = browser.new_context()
    page = user_context.new_page()
    page.goto("https://www.google.com/")
    assert False
