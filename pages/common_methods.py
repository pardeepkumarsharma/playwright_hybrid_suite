import os
from datetime import datetime

import pytest
from playwright.sync_api import Page

from utils.config_reader import Config_Reader
from utils.logger import Logger


class Common_Methods:
    def __init__(self, browser: Page):
        self.browser = browser
        self.logger = Logger().create_logger()
        self.config = Config_Reader()

    def navigate_to(self, url):
        self.browser.goto(url)
        self.logger.info(f"Navigated to {url}")

    def click(self, locator):
        self.browser.click(locator)
        self.logger.info(f"Clicked on {locator}")

    def type(self, locator, string):
        self.browser.type(locator, text=string)
        self.logger.info(f"Entered {string} into {locator}")

    def capture_screenshot(self):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshot = os.path.join(current_dir, self.config.get("screenshot_path"), f"{timestamp}.png")
        self.browser.screenshot(path=str(screenshot))
        pytest.extra_screenshot = screenshot
        return screenshot
