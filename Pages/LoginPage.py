import time

import allure
from pytest_steps import test_steps
from selenium.webdriver.common.by import By

from Configuration.Context import TestData
from Pages.BasePage import BasePage, take_screenshot_on_failure
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    LOGO = (By.XPATH, "//img[@alt='logo']")
    EMAIL_ADDRESS = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CLASS_NAME, "MuiButton-label")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    @take_screenshot_on_failure
    def do_login(self, username, password):
        self.wait_for_element(self.LOGO)
        self.do_send_keys(self.EMAIL_ADDRESS, username)
        self.do_click(self.SUBMIT_BUTTON)
        self.do_send_keys(self.PASSWORD, password)
        time.sleep(2)
        self.do_click(self.SUBMIT_BUTTON)
