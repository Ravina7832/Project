import time

import allure
from selenium.webdriver.common.by import By

from Project.Pages.BasePage import BasePage, take_screenshot_on_failure


class HomePage(BasePage):
    DROP_DOWN = (By.XPATH, "//button[contains(@class,'DropDown')]")
    OPTION = (By.XPATH, "//span[@title='Net5']")
    IMAGE = (By.XPATH, "//*[@id='root']/div/section[2]/div/div/div[1]/div[1]/div/img")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Verify Dropdown Feature")
    @take_screenshot_on_failure
    def sel_users(self):
        self.wait_for_element(self.IMAGE)

    @allure.step("Click DropDown")
    @take_screenshot_on_failure
    def dropdown(self):
        self.do_click(self.DROP_DOWN)

    @allure.step("Select Net5")
    @take_screenshot_on_failure
    def select(self):
        time.sleep(2)
        self.do_click(self.OPTION)

