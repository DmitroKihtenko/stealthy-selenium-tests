from dataclasses import dataclass
from typing import Optional

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


@dataclass
class DriverManager:
    base_url: str
    chrome_location: str
    __driver: Optional[WebDriver] = None

    def __init__(self, base_url: str, chrome_location: str):
        self.base_url = base_url
        self.chrome_location = chrome_location
        self.__driver = None

    def get(self) -> WebDriver:
        if self.__driver is None:
            options = Options()
            options.binary_location = self.chrome_location
            self.__driver = webdriver.Chrome(options)
        return self.__driver

    def close(self):
        if self.__driver:
            self.__driver.close()
