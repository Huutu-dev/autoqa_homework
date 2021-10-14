from selenium.webdriver.common.by import By
from .base_page import Page


class SignInPage(Page):
    @classmethod
    def get_sub_url(cls):
        return 'ap/signin'
