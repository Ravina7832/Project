import allure

from Configuration.Context import TestData
from Pages.AddUsersPage import AddUsers
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.SmartWindowsPage import SmartWindows
from Tests.test_conf import BaseTest


@allure.title("TEST SUITE 3")
@allure.feature("Smart Windows Module")
class Test_SmartWindows(BaseTest):
    @allure.title("Add Schedule")
    @allure.severity(allure.severity_level.NORMAL)
    def test_smartWindows(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login()
        self.loginPage.username(TestData.USERNAME)
        self.loginPage.submit()
        self.loginPage.password(TestData.PASSWORD)
        self.loginPage.login()
        self.select_user = HomePage(self.driver)
        self.select_user.sel_users()
        self.select_user.dropdown()
        self.select_user.select()
        self.smart_windows = SmartWindows(self.driver)
        self.smart_windows.smart_windows()
        self.smart_windows.add_schedule()
        self.smart_windows.schedule_name(TestData.SEARCH_NAME)
        self.smart_windows.sel_tint()
        self.smart_windows.startdate()
        self.smart_windows.enddate()
        self.smart_windows.starttime(TestData.STARTTIME)
        self.smart_windows.endtime(TestData.ENDTIME)
        self.smart_windows.sel_days()
        self.smart_windows.schedule_save()
        self.smart_windows.search_schedule(TestData.SEARCHSCHEDULES)
        self.smart_windows.add_filter(TestData.FROMDATE, TestData.TODATE)
        self.smart_windows.edit_schedule(TestData.EDIT_NAME, TestData.EDIT_START_TIME, TestData.EDIT_END_TIME)
