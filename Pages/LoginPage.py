import time

import allure
from selenium.webdriver.common.by import By

from Configuration.Context import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    LOGO = (By.XPATH, "//img[@alt='logo']")
    EMAIL_ADDRESS = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CLASS_NAME, "MuiButton-label")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    @allure.severity(allure.severity_level.CRITICAL)
    def do_login(self, username, password):
        status = self.is_visible(self.LOGO)
        if status:
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type="AttachmentType.PNG")
            self.driver.close()
            assert False

        self.do_send_keys(self.EMAIL_ADDRESS, username)
        self.do_click(self.SUBMIT_BUTTON)
        self.do_send_keys(self.PASSWORD, password)
        time.sleep(2)
        self.do_click(self.SUBMIT_BUTTON)
