import time
from selenium.webdriver.common.by import By

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
    SAVE = (By.XPATH, "(//button[@type='button'])[34]")

    """filter"""
    FIELDS = (By.XPATH, "//div[@role='button']")
    IN_NAME = (By.XPATH, '//li[@data-value="firstName,lastName"]')
    IN_EMAIL = (By.XPATH, "//li[@data-value='email']")
    IN_PHONE = (By.XPATH, "//li[@data-value='mobilePhone']")

    """Search users"""

    SEARCH_USERS = (By.XPATH, "//input[@placeholder='Search users']")
    SEARCH_CLICK = (By.XPATH, "//*[@id='root']/div/section[2]/div/div[2]/div[1]/div/div/div/div[1]/button")

    """Checkbox"""
    BUILDING_MANAGERS = (
        By.XPATH, "//*[@id='root']/div/section[2]/div/div[1]/div[2]/div[2]/div/div[2]/label/span[1]/span[1]")
    CSM_S = (By.XPATH, "//*[@id='root']/div/section[2]/div/div[1]/div[2]/div[2]/div/div[3]/label/span[1]")
    OCCUPANTS = (By.XPATH, "//*[@id='root']/div/section[2]/div/div[1]/div[2]/div[2]/div/div[4]/label/span[1]")

    """EDIT USER"""
    EDIT_USER = (By.XPATH, "(//button[@title='Edit'])[1]")
    EDIT_SAVE = (By.XPATH, "(//span[@class='MuiButton-label'])[5]")

    def __init__(self, driver):
        super().__init__(driver)

    @take_screenshot_on_failure
    def users(self):
        self.do_click(self.USERS)
        self.wait_for_element(self.ALL_USERS)
        time.sleep(2)

    @take_screenshot_on_failure
    def add_users(self, firstname, lastname, email, phone, password, confirm_password, date):
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
        time.sleep(4)
        page_source = self.driver.page_source
        assert page_source.__contains__('8799665455')

    @take_screenshot_on_failure
    def search_users(self, Search_name, Search_email, Search_phone):
        self.wait_for_element(self.ALL_USERS)
        self.do_click(self.FIELDS)
        time.sleep(2)
        self.do_click(self.IN_NAME)
        self.do_click(self.BUILDING_MANAGERS)
        time.sleep(1)
        self.do_send_keys(self.SEARCH_USERS, Search_name)
        self.do_click(self.SEARCH_CLICK)
        time.sleep(2)
        self.do_click(self.BUILDING_MANAGERS)
        self.wait_for_element(self.ALL_USERS)

        time.sleep(3)
        self.do_click(self.FIELDS)
        time.sleep(2)
        self.do_click(self.IN_EMAIL)
        time.sleep(3)
        self.do_click(self.CSM_S)
        time.sleep(1)
        self.do_send_keys(self.SEARCH_USERS, Search_email)
        self.do_click(self.SEARCH_CLICK)
        time.sleep(2)
        self.do_click(self.CSM_S)

        time.sleep(4)
        self.do_click(self.FIELDS)
        time.sleep(2)
        self.do_click(self.IN_PHONE)
        time.sleep(3)
        self.do_click(self.OCCUPANTS)
        time.sleep(1)
        self.do_send_keys(self.SEARCH_USERS, Search_phone)
        time.sleep(2)
        self.do_click(self.SEARCH_CLICK)
        time.sleep(2)
        self.do_click(self.OCCUPANTS)
        time.sleep(2)

    def edit_user(self, firstname, lastname, email, phone):
        self.do_click(self.EDIT_USER)
        self.back_space(self.FIRST_NAME)
        self.do_send_keys(self.FIRST_NAME, firstname)
        self.back_space(self.LAST_NAME)
        self.do_send_keys(self.LAST_NAME, lastname)
        self.back_space(self.EMAIL)
        self.do_send_keys(self.EMAIL, email)
        self.back_space(self.PHONE)
        self.do_send_keys(self.PHONE, phone)
        self.do_click(self.NEXT)
        self.do_click(self.EDIT_SAVE)

        page_source = self.driver.page_source
        assert page_source.__contains__('7894561239')



