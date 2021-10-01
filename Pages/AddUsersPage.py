import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage, take_screenshot_on_failure


class AddUsers(BasePage):
    """add users"""
    USERS = (By.LINK_TEXT, "Users")
    ALL_USERS = (By.XPATH, "//*[@id='root']/div/section[2]/div/div[2]/div[3]/table")
    ADD_USERS = (By.XPATH, "//*[@id='root']/div/section[2]/div/div[2]/div[1]/button")
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    EMAIL = (By.XPATH, "(//input[@name='email'])[2]")
    PHONE = (By.XPATH, "(//input[@name='mobilePhone'])[2]")
    PASSWORD = (By.NAME, "password")
    CONFIRM_PASSWORD = (By.NAME, "confirmPassword")
    SELECT_PERSON = (By.ID, "mui-component-select-roles")
    SEL_OCCUPANT = (By.XPATH, "//li[@data-value='73a11666-7b18-4b3a-be34-d0840126a297']")
    NEXT = (By.XPATH, "//button[@type='submit']")
    TIMELIMITATION = (By.XPATH, "/html/body/div[4]/div[3]/div/div/div[2]/form/div/div[1]/label/span[1]/span[1]")
    DATE = (By.ID, "date")
    ZONE = (By.XPATH, "//*[@id='panel1a-header']/div[1]/label/span[1]/span[1]")
    SAVE = (By.XPATH, "(//button[@type='button'])[33]")
    ERROR_MSG = (By.XPATH, "//*[@id='root']/div[2]/div/div[2]")
    CANCEL = (By.XPATH, "/html/body/div[3]/div[3]/div/div/div[1]/h2/div[1]/button")

    """Search users"""

    SEARCH_USERS = (By.XPATH, "//input[@placeholder='Search users']")
    SEARCH_CLICK = (By.XPATH, "//*[@id='root']/div/section[2]/div/div[2]/div[1]/div/div/div/div[1]/button")

    def __init__(self, driver):
        super().__init__(driver)

    @take_screenshot_on_failure
    def add_users(self, firstname, lastname, email, phone, password, confirm_password, date):
        self.do_click(self.USERS)
        self.wait_for_element(self.ALL_USERS)
        self.do_click(self.ADD_USERS)
        self.do_send_keys(self.FIRST_NAME, firstname)
        self.do_send_keys(self.LAST_NAME, lastname)
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PHONE, phone)
        self.do_send_keys(self.PASSWORD, password)
        self.do_send_keys(self.CONFIRM_PASSWORD, confirm_password)
        self.do_click(self.SELECT_PERSON)
        self.do_click(self.SEL_OCCUPANT)
        self.do_click(self.NEXT)
        self.do_click(self.TIMELIMITATION)
        self.do_send_keys(self.DATE, date)
        self.do_click(self.ZONE)
        self.do_click(self.SAVE)
        time.sleep(6)

    @take_screenshot_on_failure
    def search_users(self, Search_users):
        ALL_USERS = (By.XPATH, "//*[@id='root']/div/section[2]/div/div[2]/div[3]/table")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ALL_USERS))
        # msg = self.get_element_text(self.ERROR_MSG)
        # Actual_msg = "Email already exists"
        # if msg.contentEquals(Actual_msg):
        #     self.do_click(self.CANCEL)
        #     self.do_send_keys(self.SEARCH_USERS, Search_users)
        #     self.do_click(self.SEARCH_CLICK)
        #
        # else:
        self.do_send_keys(self.SEARCH_USERS, Search_users)
        self.do_click(self.SEARCH_CLICK)


