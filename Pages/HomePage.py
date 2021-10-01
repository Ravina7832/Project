from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Configuration.Context import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    DROP_DOWN = (By.XPATH, "//button[contains(@class,'DropDown')]")
    OPTION = (By.XPATH, "//span[@title='Net5']")

    def __init__(self, driver):
        super().__init__(driver)

    def sel_users(self):
        IMAGE = (By.XPATH, "//*[@id='root']/div/section[2]/div/div/div[1]/div[1]/div/img")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IMAGE))
        self.do_click(self.DROP_DOWN)
        self.do_click(self.OPTION)

