import base64

import playwright
import pytest
import os
from datetime import datetime

import pytest_html
from pytest_html import extras
from playwright.sync_api import Playwright
from utils.config_reader import Config_Reader

config = Config_Reader()


@pytest.fixture(scope="session")
def launch(playwright:Playwright):
    browser_name=config.get("browser")
    browser= getattr(playwright,browser_name).launch(headless=config.get("headless"),args=["--start-maximized"])
    #chromium = playwright.chromium
    #browser = chromium.launch(headless=False)
    user_context = browser.new_context(no_viewport=True)
    page = user_context.new_page()
    yield page
    user_context.close()
    page.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if call.when == "call":
        screenshot = getattr(pytest, "extra_screenshot", None)
        if screenshot and os.path.exists(screenshot):
            if not hasattr(report, "extra"):
                report.extra = []
            with open(screenshot, "rb") as f:
                encoded = base64.b64encode(f.read()).decode("utf-8")
                html_img = f"<img src='data:image/png;base64, {encoded}' />"
                report.extra.append(extras.html(html_img))
            pytest.extra_screenshot = None