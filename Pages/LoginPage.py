import allure
from selenium.webdriver.common.by import By

from Project.Configuration.Context import TestData
from Project.Pages.BasePage import BasePage, take_screenshot_on_failure


class LoginPage(BasePage):
    LOGO = (By.XPATH, "//img[@alt='logo']")
    EMAIL_ADDRESS = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CLASS_NAME, "MuiButton-label")
    URL = (By.XPATH, "//div[@class='common_card-container__1xLOw']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    @allure.step("Verify login")
    @take_screenshot_on_failure
    def do_login(self):
        self.wait_for_element(self.URL)
        self.wait_for_element(self.LOGO)

    @allure.step("Enter Username")
    @take_screenshot_on_failure
    def username(self, username):
        self.do_send_keys(self.EMAIL_ADDRESS, username)

    @allure.step("Click Submit")
    @take_screenshot_on_failure
    def submit(self):
        self.do_click(self.SUBMIT_BUTTON)

    @allure.step("Enter Password")
    @take_screenshot_on_failure
    def password(self, password):
        self.do_send_keys(self.PASSWORD, password)

    @allure.step("Click Submit")
    @take_screenshot_on_failure
    def login(self):
        self.do_click(self.SUBMIT_BUTTON)

        if self.driver.title == "ViewSense - Control Center":
            assert True
        else:
            assert False
