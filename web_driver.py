from functools import partial
from selenium import common, webdriver

chromedriver_path = r"D:\Careerist\AutomaticQA\bin\chromedriver.exe"
chrome_driver = partial(webdriver.Chrome, executable_path=chromedriver_path)

__all__ = ["chrome_driver"]
