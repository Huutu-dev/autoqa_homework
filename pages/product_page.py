from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from .base_page import Page


class ProductPage(Page):
    ADD_TO_CART_BIN = (By.ID, 'add-to-cart-button')
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//h2/a[.//span]")
    _PRODUCT_PRICE_ = (By.XPATH,
                       '//*[@id="search"]//div[@data-component-type="s-search-result"][1]//h2/a[string-length(@href)>0 and ./span]')

    PRODUCT_NAME = (By.ID, 'productTitle')
    COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
    CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
    ACCORDION_ROW = (By.CSS_SELECTOR, "#newAccordionRow i.a-icon-radio-inactive")
    NO_COVERAGE = (By.CSS_SELECTOR, "#attachSiNoCoverage input.a-button-input")

    @classmethod
    def get_sub_url(cls):
        return NotImplemented

    def __init__(self, driver):
        super().__init__(driver)
        self._current_product_name = ''

    @property
    def current_product_name(self):
        if not self._current_product_name:
            self.store_product_name()
        return self._current_product_name

    def store_product_name(self, refresh_required=False):
        if refresh_required:
            self.driver.refresh()
        self._current_product_name = self.find_element(*self.PRODUCT_NAME).text

    def click_first_product(self, refresh_required=False):
        if refresh_required:
            self.driver.refresh()
        self.click(*self.PRODUCT_PRICE)

    def add_to_cart(self):
        try:
            # if Subscribe & Save is appear in the desktop buybox
            e = self.find_element(*self.ACCORDION_ROW)
        except NoSuchElementException:
            pass
        else:
            e.click()
            self.wait_for_element_disappear(self.ACCORDION_ROW)

        self.wait_for_element_click(self.ADD_TO_CART_BIN, 'Can not clickable on Cart button')

        try:
            # Check if there is special plane appear
            desktop_sidesheet = (By.ID, 'attach-desktop-sideSheet')
            self.wait_for_element_appear(desktop_sidesheet)
        except (NoSuchElementException, TimeoutException):
            pass
        else:
            e = self.find_element(*self.NO_COVERAGE)
            e.click()
        self.wait_for_element_disappear(self.ADD_TO_CART_BIN)

    def verify_through_colors(self, expected_colors: list):
        color_elements = self.find_elements(*self.COLOR_OPTIONS)
        for i, color_e in enumerate(color_elements):
            color_e.click()
            self.verify_text(expected_colors[i], *self.CURRENT_COLOR)
