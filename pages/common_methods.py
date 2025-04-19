from playwright.sync_api import Page
from utils.logger import Logger

class Common_Methods:
    def __init__(self,browser:Page):
        self.browser = browser
        self.logger = Logger().create_logger()

    def navigate_to(self,url):
        self.browser.goto(url)
        self.logger.info(f"Navigated to {url}")

    def click(self,locator):
        self.browser.click(locator)
        self.logger.info(f"Clicked on {locator}")

    def type(self,locator,string):
        self.browser.type(locator, text=string)
        self.logger.info(f"Entered {string} into {locator}")

