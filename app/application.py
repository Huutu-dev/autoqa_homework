from selenium.webdriver.remote.webdriver import WebDriver
from pages.main_page import MainPage, Header
from pages.sign_in_page import SignInPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.fashion_header import FashionHeader


class Application:
    def __init__(self, driver: WebDriver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.sign_in_page = SignInPage(driver)
        self.cart_page = CartPage(driver)
        self.product_page = ProductPage(driver)
        self.fashion_header = FashionHeader(driver)
