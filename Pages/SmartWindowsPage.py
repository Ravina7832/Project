import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.BasePage import BasePage, take_screenshot_on_failure


class SmartWindows(BasePage):
    SAVED_SCHEDULE = (By.XPATH, "(//div[contains(@class,'MuiCollapse')])[1]")
    SMART_WINDOWS = (By.LINK_TEXT, "Smart Windows")
    SCHEDULES = (By.LINK_TEXT, "Schedules")
    ADD_SCHEDULE = (By.XPATH, "//h6[text()='ADD SCHEDULE']")

    """Schedule Details"""
    NAME = (By.XPATH, "//input[@name='name']")
    SELECT_TINT = (By.XPATH, "(//div[@class='schedule-form_tintCircle__1TtfZ']//div)[3]")

    START_DATE_PICKER = (By.XPATH, "(//button[@type='button'])[5]")
    SELECT_START_MONTH = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/button[2]")
    SELECT_START_DATE = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/button")
    CLICK_OK1 = (By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/button[3]")

    END_DATE_PICKER = (By.XPATH, "(//button[@type='button'])[7]")
    SELECT_END_MONTH = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/button[2]")
    SELECT_END_DATE = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[5]/div[3]/button")
    CLICK_OK2 = (By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/button[3]")
    START_TIME = (By.XPATH, "(//input[@name='totime'])[1]")
    END_TIME = (By.XPATH, "(//input[@name='totime'])[2]")
    REPEAT = (By.XPATH,
              "//*[@id='root']/div/section[2]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[3]/div/div["
              "2]/form/div/div[1]/div[5]/label/span[1]/span[1]")
    SUNDAY = (By.XPATH, "(//div[@class = 'schedule-form_dayIcon__8wig6'])[1]")
    MONDAY = (By.XPATH, "(//div[@class = 'schedule-form_dayIcon__8wig6'])[2]")
    TUESDAY = (By.XPATH, "(//div[@class = 'schedule-form_dayIcon__8wig6'])[3]")
    WEDNESDAY = (By.XPATH, "(//div[@class = 'schedule-form_dayIcon__8wig6'])[4]")
    THURSDAY = (By.XPATH, "(//div[@class = 'schedule-form_dayIcon__8wig6'])[5]")
    FRIDAY = (By.XPATH, "(//div[@class = 'schedule-form_dayIcon__8wig6'])[6]")
    SATURDAY = (By.XPATH, "(//div[@class = 'schedule-form_dayIcon__8wig6'])[7]")
    ZONE_GROUPS = (By.XPATH, "//*[@id='root']/div/section[2]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div["
                             "2]/span/span[1]")
    SAVE = (By.XPATH, "//button[@type='submit']")
    VERIFY_ADD = (By.XPATH, "(//div[@class='MuiCollapse-wrapper'])[5]")
    SEARCH_ZONES = (By.XPATH, "(//input[@type='text'])[4]")
    SEARCH_CLICK = (By.XPATH, "(//span[@class='MuiIconButton-label'])[20]")
    SEARCH_SCHEDULES = By.XPATH, "(//input[@type='text'])[1]"
    CLICK_SEARCH = (By.XPATH, "(//button[@type='button'])[4]")

    '''filter'''
    FILTER_SCHEDULES = (By.XPATH, "//span[@class='MuiSwitch-root']")
    FROM_DATE = (By.XPATH, "//input[@placeholder='From Date']")
    TO_DATE = (By.XPATH, "//input[@placeholder='To Date']")
    APPLY = (By.XPATH, "(//button[contains(@class,'MuiButtonBase')])[6]")

    """Edit"""
    EDIT = (By.XPATH, "//span[text()='edit']")
    VERIFY_EDIT = (By.TAG_NAME, "h6")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Verify SmartWindows")
    @allure.step("Go to SmartWindows And click Schedule")
    @take_screenshot_on_failure
    def smart_windows(self):
        self.do_click(self.SMART_WINDOWS)
        time.sleep(2)
        self.do_click(self.SCHEDULES)

    @allure.step("Click Add Schedule")
    @take_screenshot_on_failure
    def add_schedule(self, starttime, endtime):
        self.wait_for_element(self.SAVED_SCHEDULE)
        self.do_click(self.ADD_SCHEDULE)

    @allure.step("Enter Schedule Name")
    @take_screenshot_on_failure
    def schedule_name(self,name):
        self.do_send_keys(self.NAME, name)

    @allure.step("Select Tint")
    @take_screenshot_on_failure
    def sel_tint(self):
        self.do_click(self.SELECT_TINT)

    @allure.step("Select Start Date")
    @take_screenshot_on_failure
    def startdate(self):
        self.do_click(self.START_DATE_PICKER)
        self.do_click(self.SELECT_START_MONTH)
        self.do_click(self.SELECT_START_DATE)
        self.do_click(self.CLICK_OK1)

    @allure.step("Select End Date")
    @take_screenshot_on_failure
    def enddate(self):
        self.do_click(self.END_DATE_PICKER)
        self.do_click(self.SELECT_END_MONTH)
        self.do_click(self.SELECT_END_DATE)
        self.do_click(self.CLICK_OK2)

    @allure.step("Enter Start Time")
    @take_screenshot_on_failure
    def starttime(self, starttime):
        self.do_send_keys(self.START_TIME, starttime)

    @allure.step("Enter End Time")
    @take_screenshot_on_failure
    def endtime(self, endtime):
        self.do_send_keys(self.END_TIME, endtime)

    @allure.step("Select Days")
    @take_screenshot_on_failure
    def sel_days(self):
        self.do_click(self.REPEAT)
        self.do_click(self.SUNDAY)
        self.do_click(self.MONDAY)
        self.do_click(self.TUESDAY)
        self.do_click(self.WEDNESDAY)
        self.do_click(self.THURSDAY)
        self.do_click(self.FRIDAY)
        self.do_click(self.SATURDAY)

    @allure.step("Save")
    @take_screenshot_on_failure
    def schedule_save(self):
        self.do_click(self.ZONE_GROUPS)
        self.do_click(self.SAVE)

        page_source = self.driver.page_source
        assert page_source.__contains__('Automatic')

    @allure.step("Verify Search")
    @take_screenshot_on_failure
    def search_schedule(self, search_schedules):
        self.do_send_keys(self.SEARCH_SCHEDULES, search_schedules)
        self.do_send_keys(self.SEARCH_SCHEDULES, Keys.ARROW_DOWN)
        self.do_send_keys(self.SEARCH_SCHEDULES, Keys.RETURN)
        self.do_click(self.CLICK_SEARCH)

    @allure.step("Verify Filter Feature")
    @take_screenshot_on_failure
    def add_filter(self, from_date, to_date):
        self.do_click(self.FILTER_SCHEDULES)
        self.do_send_keys(self.FROM_DATE, from_date)
        self.do_send_keys(self.TO_DATE, to_date)
        self.do_click(self.APPLY)
        self.do_click(self.FILTER_SCHEDULES)

    @allure.step("Verify Edit Schedule Feature")
    @take_screenshot_on_failure
    def edit_schedule(self, name, starttime, endtime):
        self.do_click(self.EDIT)
        self.back_space(self.NAME)
        self.do_send_keys(self.NAME, name)
        self.do_send_keys(self.START_TIME, starttime)
        self.do_send_keys(self.END_TIME, endtime)
        self.do_click(self.SAVE)
        page_source = self.driver.page_source
        assert page_source.__contains__('Automatic Edit')
