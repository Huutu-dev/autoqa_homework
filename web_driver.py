from functools import partial
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chromedriver_path = r"D:\Careerist\AutomaticQA\bin\Chrome95\chromedriver.exe"
chrome_driver = partial(webdriver.Chrome, service=Service(chromedriver_path))

__all__ = ["chrome_driver"]
