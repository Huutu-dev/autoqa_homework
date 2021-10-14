from selenium.webdriver.common.by import By
from .base_page import Page


class MainPage(Page):
    @classmethod
    def get_sub_url(cls):
        return NotImplemented

    def open_me(self):
        self.open_page()


class Header(MainPage):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, "nav-search-submit-button")
    AMAZON_ICON = (By.ID, "nav-logo-sprites")
    NAV_ORDER = (By.CSS_SELECTOR, 'a#nav-orders')
    NAV_CART = (By.CSS_SELECTOR, "div#nav-tools a#nav-cart.nav-a")

    def __init__(self, driver):
        super().__init__(driver)
        self._amazon_icon_element = None

    @property
    def amazon_icon_element(self):
        if not self._amazon_icon_element:
            self._amazon_icon_element = self.find_element(*self.AMAZON_ICON)
        return self._amazon_icon_element

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def go_return_n_order(self):
        self.wait_for_element_click(self.NAV_ORDER)

    def checkin_cart(self, page_obj=None):
        if page_obj is None:
            self.wait_for_element_click(self.NAV_CART)
        else:
            assert isinstance(page_obj, Page)
            page_obj.click_wait_page_opened(self.NAV_CART)
