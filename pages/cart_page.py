from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from .base_page import Page


class CartPage(Page):
    CART_COUNT = (By.ID, 'nav-cart-count')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#sc-active-cart li a.a-link-normal.sc-product-link')
    SC_EMPTY_CART = (By.CSS_SELECTOR, "#sc-empty-cart-message h2.sc-your-amazon-cart-is-empty")
    SC_ACTIVE_CART = (By.CSS_SELECTOR, "#sc-active-cart div.sc-your-amazon-cart-is-empty")

    @classmethod
    def get_sub_url(cls):
        return 'gp/cart/view.html?ref_=nav_cart'

    def open_me(self):
        self.open_page(self.get_sub_url())

    def cart_is_empty(self, text_present):
        try:
            self.verify_text(text_present, *self.SC_EMPTY_CART)
        except NoSuchElementException:
            self.verify_text(text_present, *self.SC_ACTIVE_CART)
            # print("Exception")
        else:
            # print("First is OK")
            pass

    def count_products(self, expected_count):
        actual_count = self.find_element(*self.CART_COUNT).text
        assert actual_count == expected_count, f'Expected {expected_count} item(s), but got {actual_count} item(s)'

    def verify_product_name(self, current_product_name):
        cart_product_name = self.find_element(*self.PRODUCT_NAME).text
        # print(f'Product name in cart: {cart_product_name}')
        assert cart_product_name == current_product_name, \
            f'Expected "{current_product_name}" product, but got "{cart_product_name}"'