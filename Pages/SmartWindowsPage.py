import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class SmartWindows(BasePage):
    DROP_DOWN = (By.XPATH, "//button[contains(@class,'DropDown')]")
    OPTION = (By.XPATH, "//span[@title='Net5']")
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

    START_TIME_PICKER = (By.XPATH, "(//button[@type='button'])[6]")
    SELECT_START_HOUR = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div/div/span[12]")
    CLICK_ON_START_MINUTES = (By.XPATH, "(//button[@type='button'])[11]")
    SELECT_START_MINUTES = (By.XPATH, "(//span[contains(@class, 'MuiPickersClockNumber')])[7]")
    CLICK_ON_PM1 = (By.XPATH, "(//button[@type='button'])[13]")
    CLICK_OK3 = (By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/button[3]")

    END_TIME_PICKER = (By.XPATH, "(//button[@type='button'])[8]")
    SELECT_END_HOUR = (By.XPATH, "(//span[contains(@class, 'MuiPickersClockNumber')])[2]")
    CLICK_ON_END_MINUTES = (By.XPATH, "(//button[@type='button'])[11]")
    SELECT_END_MINUTES = (By.XPATH, "(//span[contains(@class, 'MuiPickersClockNumber')])[7]")
    CLICK_ON_PM2 = (By.XPATH, "(//button[@type='button'])[13]")
    CLICK_OK4 = (By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/button[3]")

    ALL_NUMBERS = (By.XPATH, "//span[contains(@class,'MuiPickersClockNumber')]")

    # START_DATE = (By.NAME, "startDate")
    START_TIME = (By.XPATH, "(//input[@name='totime'])[1]")
    # END_DATE = (By.XPATH, "//input[@name='endDate']")
    END_TIME = (By.XPATH, "(//input[@name='totime'])[2]")
    REPEAT = (By.XPATH,
              "(//span[@class='MuiIconButton-label'])[25]")
    SUNDAY = (By.XPATH, "(//div[@class = 'schedule-form_dayIcon__8wig6'])[1]")
    MONDAY = (By.XPATH, "(//div[@class = 'schedule-form_dayIcon__8wig6'])[2]")
    THURSDAY = (By.XPATH, "(//div[@class = 'schedule-form_dayIcon__8wig6'])[5]")
    ZONE_GROUPS = (By.XPATH, "(//span[@class='MuiIconButton-label'])[27]")
    SAVE = (By.XPATH, "//button[@type='submit']")
    SEARCH_ZONES = (By.XPATH, "(//input[@type='text'])[4]")
    SEARCH_CLICK = (By.XPATH, "(//span[@class='MuiIconButton-label'])[20]")
    SEARCH_SCHEDULES = By.XPATH, "(//input[@type='text'])[1]"
    CLICK_SEARCH = (By.XPATH, "(//button[@type='button'])[4]")
    SELECT_OPTION = (By.XPATH, "")

    '''filter'''
    FILTER_SCHEDULES = (By.XPATH, "//span[@class='MuiSwitch-root']")
    FROM_DATE = (By.XPATH, "//input[@placeholder='From Date']")
    TO_DATE = (By.XPATH, "//input[@placeholder='To Date']")
    APPLY = (By.XPATH, "(//button[contains(@class,'MuiButtonBase')])[6]")

    def __init__(self, driver):
        super().__init__(driver)

    def smart_windows(self, name, starttime, endtime, search_schedules, from_date, to_date):
        IMAGE = (By.XPATH, "//*[@id='root']/div/section[2]/div/div/div[1]/div[1]/div/img")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(IMAGE))
        self.do_click(self.DROP_DOWN)
        self.do_click(self.OPTION)
        time.sleep(2)
        self.do_click(self.SMART_WINDOWS)
        time.sleep(2)
        self.do_click(self.SCHEDULES)

        SAVED_SCHEDULE = (By.XPATH, "(//div[contains(@class,'MuiCollapse')])[1]")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SAVED_SCHEDULE))
        self.do_click(self.ADD_SCHEDULE)
        time.sleep(2)
        self.do_send_keys(self.NAME, name)
        self.do_click(self.SELECT_TINT)
        time.sleep(2)

        # selected_year_string = "September 2021"
        # target_year_string = "December 2022"
        # previous_button_xpath = "(//button[@type='button'])[12]"
        # next_button_xpath = "(//button[@type='button'])[13]"
        # if target_year_string > selected_year_string:
        #     next_click = self.driver.find_element_by_xpath(next_button_xpath)
        #     next_click.click()
        # else:
        #     previous_click = self.driver.find_element_by_xpath(previous_button_xpath)
        #     previous_click.click()
        self.do_click(self.START_DATE_PICKER)
        self.do_click(self.SELECT_START_MONTH)
        self.do_click(self.SELECT_START_DATE)
        self.do_click(self.CLICK_OK1)

        self.do_click(self.END_DATE_PICKER)
        self.do_click(self.SELECT_END_MONTH)
        self.do_click(self.SELECT_END_DATE)
        self.do_click(self.CLICK_OK2)
        time.sleep(2)

        self.do_send_keys(self.START_TIME, starttime)

        self.do_send_keys(self.END_TIME, endtime)
        time.sleep(2)
        self.do_click(self.REPEAT)
        time.sleep(2)
        self.do_click(self.SUNDAY)
        self.do_click(self.MONDAY)
        self.do_click(self.THURSDAY)
        time.sleep(2)
        self.do_click(self.ZONE_GROUPS)
        time.sleep(2)
        self.do_click(self.SAVE)
        time.sleep(6)

        '''search Zones & Schedules'''

        self.do_send_keys(self.SEARCH_SCHEDULES, search_schedules)
        time.sleep(1)
        self.do_send_keys(self.SEARCH_SCHEDULES, Keys.ARROW_DOWN)
        self.do_send_keys(self.SEARCH_SCHEDULES, Keys.RETURN)
        time.sleep(1)
        self.do_click(self.CLICK_SEARCH)
        time.sleep(5)

        # self.do_click(self.SEARCH_ZONES)
        # time.sleep(1)
        # self.do_send_keys(self.SEARCH_ZONES, Keys.ARROW_DOWN)
        # self.do_send_keys(self.SEARCH_ZONES, Keys.RETURN)
        # time.sleep(1)
        # self.do_click(self.SEARCH_CLICK)

        """filter"""
        self.do_click(self.FILTER_SCHEDULES)
        self.do_send_keys(self.FROM_DATE, from_date)
        self.do_send_keys(self.TO_DATE, to_date)
        self.do_click(self.APPLY)

        # Data = (By.XPATH, "(//div[contains(@class,'MuiPaper-root')])[1]")
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Data))
        # action = ActionChains(self.driver)
        # action.move_to_element(self.SEARCH_SCHEDULES).click().perform()
