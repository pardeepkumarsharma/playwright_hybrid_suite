
from pages.login_page import Login_Page
from conftest import launch

def test_run(launch):
    Login_Page(launch).login()


