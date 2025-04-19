import time

from pages.common_methods import Common_Methods
from pages.locators import *
from utils.config_reader import Config_Reader

class Login_Page(Common_Methods):

    def __init__(self,browser):
        super().__init__(browser)
        self.config = Config_Reader()

    def login(self):
        self.navigate_to(self.config.get("url"))
        self.click(login_link)
        self.type(username,self.config.get("username"))
        self.type(password,self.config.get("password"))
        self.browser.screenshot(path="reports/1.png")
        self.click(login_button)

