import time
from Pages.login_page import LoginPage
from Pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(3)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()