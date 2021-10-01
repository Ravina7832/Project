from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Configuration.Context import TestData
from Pages.BasePage import BasePage, take_screenshot_on_failure


class HomePage(BasePage):
    DROP_DOWN = (By.XPATH, "//button[contains(@class,'DropDown')]")
    OPTION = (By.XPATH, "//span[@title='Net5']")
    IMAGE = (By.XPATH, "//*[@id='root']/div/section[2]/div/div/div[1]/div[1]/div/img")

    def __init__(self, driver):
        super().__init__(driver)

    @take_screenshot_on_failure
    def sel_users(self):
        self.wait_for_element(self.IMAGE)
        self.do_click(self.DROP_DOWN)
        self.do_click(self.OPTION)

