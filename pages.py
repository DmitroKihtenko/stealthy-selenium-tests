from abc import ABC
from dataclasses import dataclass

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver import DriverManager
from fixtures import UserData


@dataclass(init=True)
class PageHeader(ABC):
    manager: DriverManager
    user: UserData
    wait_element_timeout: float

    @property
    def driver(self) -> WebDriver:
        return self.manager.get()

    def navigate(self):
        pass

    def sign_out(self):
        element_present = EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button:has(.fa-sign-out)")
        )
        WebDriverWait(self.driver, self.wait_element_timeout).until(
            element_present
        )
        element = self.driver.find_element(
            By.CSS_SELECTOR, "button:has(.fa-sign-out)"
        )
        self.driver.execute_script(
            "arguments[0].click()", element
        )
        return self

    def assert_sign_out_success(self):
        element_present = EC.invisibility_of_element(
            (By.CSS_SELECTOR, "fa-user-circle")
        )
        WebDriverWait(self.driver, self.wait_element_timeout).until(
            element_present
        )
        return self


@dataclass(init=True)
class UserPage(PageHeader):
    wait_element_timeout: float = 2

    def type_login(self):
        login_input = self.driver.find_element(
            By.CSS_SELECTOR, '[placeholder="Your username"]'
        )
        login_input.send_keys(self.user.username)
        return self

    def type_password(self):
        password_input = self.driver.find_element(
            By.CSS_SELECTOR, '[placeholder="Your password"]'
        )
        password_input.send_keys(self.user.password)
        return self

    def submit(self):
        button = self.driver.find_element(
            By.CSS_SELECTOR, '[type="submit"]'
        )
        self.driver.execute_script(
            "arguments[0].click()", button
        )
        return self


@dataclass(init=True)
class SignUpPage(UserPage):
    def navigate(self):
        self.driver.get(f"{self.manager.base_url}/sign-up")
        return self

    def assert_sign_up_success(self):
        element_present = EC.presence_of_element_located(
            (By.CLASS_NAME, "fa-user-circle")
        )
        WebDriverWait(self.driver, self.wait_element_timeout).until(
            element_present
        )
        return self


@dataclass(init=True)
class SignInPage(UserPage):
    def navigate(self):
        self.driver.get(f"{self.manager.base_url}/sign-in")
        return self

    def assert_sign_in_success(self):
        element_present = EC.presence_of_element_located(
            (By.CLASS_NAME, "fa-user-circle")
        )
        WebDriverWait(self.driver, self.wait_element_timeout).until(
            element_present
        )
        return self


@dataclass
class UserSpacePage(PageHeader):
    wait_element_timeout: float
    file_path: str

    @property
    def driver(self) -> WebDriver:
        return self.manager.get()

    def navigate(self):
        self.driver.get(f"{self.manager.base_url}/space")
        return self

    def type_file(self):
        element_present = EC.presence_of_element_located(
            (By.CLASS_NAME, "custom-file-input")
        )
        WebDriverWait(self.driver, self.wait_element_timeout).until(
            element_present
        )
        element = self.driver.find_element(
            By.CLASS_NAME, "custom-file-input",
        )
        element.send_keys(self.file_path)
        return self

    def upload_file(self):
        button = self.driver.find_element(
            By.CSS_SELECTOR, "button:has(.fa-upload)"
        )
        self.driver.execute_script(
            "arguments[0].click()", button
        )
        return self

    def check_file_uploaded(self):
        element_present = EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button:has(.fa-download)")
        )
        WebDriverWait(self.driver, self.wait_element_timeout).until(
            element_present
        )
        return self

    def download_file(self):
        button = self.driver.find_element(
            By.CSS_SELECTOR, "button:has(.fa-download)"
        )
        self.driver.execute_script(
            "arguments[0].click()", button
        )
        element_present = EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a:has(.fa-download)")
        )
        WebDriverWait(self.driver, self.wait_element_timeout).until(
            element_present
        )
        button = self.driver.find_element(
            By.CSS_SELECTOR, "a:has(.fa-download)"
        )
        self.driver.execute_script(
            "arguments[0].click()", button
        )
        return self

    def check_no_errors_on_page(self):
        element_present = EC.invisibility_of_element(
            (By.CLASS_NAME, "alert")
        )
        WebDriverWait(self.driver, self.wait_element_timeout).until(
            element_present
        )
        return self
