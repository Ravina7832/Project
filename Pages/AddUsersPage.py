import time

import allure
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage, take_screenshot_on_failure


class AddUsers(BasePage):
    """add users"""
    USERS = (By.LINK_TEXT, "Users")
    ALL_USERS = (By.XPATH, "//*[@id='root']/div/section[2]/div/div[2]/div[3]/table")
    ADD_USERS = (By.XPATH, "//*[@id='root']/div/section[2]/div/div[2]/div[1]/button")
    USER_PAGE = (By.XPATH, "//div[@role='dialog']")
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
        By.XPATH, "//*[@id='root']/div/section[2]/div/div[1]/div[2]/div[2]/div/div[2]/label/span[1]")
    CSM_S = (By.XPATH, "//*[@id='root']/div/section[2]/div/div[1]/div[2]/div[2]/div/div[3]/label/span[1]")
    OCCUPANTS = (By.XPATH, "//*[@id='root']/div/section[2]/div/div[1]/div[2]/div[2]/div/div[4]/label/span[1]")

    """EDIT USER"""
    EDIT_USER = (By.XPATH, "(//button[@title='Edit'])[1]")
    EDIT_SAVE = (By.XPATH, "(//span[@class='MuiButton-label'])[5]")

    """DELETE USER"""
    DEL_USER = (By.XPATH, "(//button[@title='Remove'])[1]")
    DEL_POPUP = (By.XPATH, "//div[@role='dialog']")
    YES = (By.XPATH, "(//span[@class='MuiButton-label'])[4]")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Verify Users")
    @take_screenshot_on_failure
    def users(self):
        self.do_click(self.USERS)

    @allure.step("Click AddUser")
    @take_screenshot_on_failure
    def add_users(self):
        time.sleep(3)
        self.do_click(self.ADD_USERS)

    @allure.step("Enter FirstName")
    @take_screenshot_on_failure
    def firstname(self, firstname):
        self.wait_for_element(self.USER_PAGE)
        self.do_send_keys(self.FIRST_NAME, firstname)

    @allure.step("Enter LastName")
    @take_screenshot_on_failure
    def lastname(self, lastname):
        self.do_send_keys(self.LAST_NAME, lastname)

    @allure.step("Enter Email")
    @take_screenshot_on_failure
    def email(self, email):
        self.do_send_keys(self.EMAIL, email)

    @allure.step("Enter Phone No.")
    @take_screenshot_on_failure
    def phone(self, phone):
        self.do_send_keys(self.PHONE, phone)

    @allure.step("Enter Password")
    @take_screenshot_on_failure
    def password(self, password):
        self.do_send_keys(self.PASSWORD, password)

    @allure.step("Confirm Password")
    @take_screenshot_on_failure
    def conf_password(self, confirm_password):
        self.do_send_keys(self.CONFIRM_PASSWORD, confirm_password)

    @allure.step("Select person")
    @take_screenshot_on_failure
    def select_person(self):
        self.do_click(self.SELECT_PERSON)
        self.do_click(self.SEL_OCCUPANT)

    @allure.step("Click Next")
    @take_screenshot_on_failure
    def next(self):
        self.do_click(self.NEXT)

    @allure.step("select time checkbox")
    @take_screenshot_on_failure
    def time(self):
        self.do_click(self.TIMELIMITATION)

    @allure.step("Enter Date")
    @take_screenshot_on_failure
    def sel_date(self, date):
        self.do_send_keys(self.DATE, date)

    @allure.step("select Zone")
    @take_screenshot_on_failure
    def zone(self):
        time.sleep(2)
        self.do_click(self.ZONE)
        self.do_click(self.SAVE)

    @allure.step("Click Save")
    @take_screenshot_on_failure
    def save(self):
        self.do_click(self.SAVE)
        page_source = self.driver.page_source
        assert page_source.__contains__('8799665455')

    @allure.step("Verify Search feature")
    @allure.step("Select Field by name and Search")
    @take_screenshot_on_failure
    def search_users(self):
        self.wait_for_element(self.ALL_USERS)
        time.sleep(3)
        self.do_click(self.FIELDS)

    @allure.step("Select Field by Name and Search")
    @take_screenshot_on_failure
    def search_name(self, Search_name):
        self.do_click(self.IN_NAME)
        self.do_send_keys(self.SEARCH_USERS, Search_name)
        self.do_click(self.SEARCH_CLICK)

    @allure.step("Select Field by Email and Search")
    @take_screenshot_on_failure
    def search_email(self, Search_email):
        self.wait_for_element(self.ALL_USERS)
        time.sleep(3)
        self.do_click(self.FIELDS)
        self.do_click(self.IN_EMAIL)
        self.do_send_keys(self.SEARCH_USERS, Search_email)
        self.do_click(self.SEARCH_CLICK)

    @allure.step("Select Field by Phone and Search")
    @take_screenshot_on_failure
    def search_phone(self, Search_phone):
        self.wait_for_element(self.ALL_USERS)
        time.sleep(2)
        self.do_click(self.FIELDS)
        self.do_click(self.IN_PHONE)
        self.do_send_keys(self.SEARCH_USERS, Search_phone)
        time.sleep(2)
        self.do_click(self.SEARCH_CLICK)

    @allure.step("Verify Edit Feature")
    @allure.step("Click Edit")
    @take_screenshot_on_failure
    def edit_user(self):
        time.sleep(2)
        self.do_click(self.EDIT_USER)

    @allure.step("Clear and Enter FirstName")
    @take_screenshot_on_failure
    def edit_fname(self, firstname):
        self.back_space(self.FIRST_NAME)
        self.do_send_keys(self.FIRST_NAME, firstname)

    @allure.step("Clear and Enter LastName")
    @take_screenshot_on_failure
    def edit_lname(self, lastname):
        self.back_space(self.LAST_NAME)
        self.do_send_keys(self.LAST_NAME, lastname)

    @allure.step("Clear and Enter Email")
    @take_screenshot_on_failure
    def edit_email(self, email):
        self.back_space(self.EMAIL)
        self.do_send_keys(self.EMAIL, email)

    @allure.step("Clear and Enter Phone")
    @take_screenshot_on_failure
    def edit_phone(self, phone):
        self.back_space(self.PHONE)
        self.do_send_keys(self.PHONE, phone)

    @allure.step("Click Next and Save")
    @take_screenshot_on_failure
    def edit_save(self):
        self.do_click(self.NEXT)
        self.do_click(self.EDIT_SAVE)

        page_source = self.driver.page_source
        assert page_source.__contains__('7894561239')

    def del_search(self, Search_phone):
        self.wait_for_element(self.ALL_USERS)
        time.sleep(2)
        self.do_click(self.FIELDS)
        self.do_click(self.IN_PHONE)
        self.do_send_keys(self.SEARCH_USERS, Search_phone)
        self.do_click(self.SEARCH_CLICK)

    def delete_user(self):
        self.wait_for_element(self.ALL_USERS)
        time.sleep(2)
        self.do_click(self.DEL_USER)
        self.wait_for_element(self.DEL_POPUP)
        self.do_click(self.YES)

    @allure.step("select checkbox")
    @take_screenshot_on_failure
    def person_as(self):
        self.do_click(self.BUILDING_MANAGERS)
        self.do_click(self.BUILDING_MANAGERS)
        self.do_click(self.CSM_S)
        self.do_click(self.CSM_S)
        self.do_click(self.OCCUPANTS)
        self.do_click(self.OCCUPANTS)
