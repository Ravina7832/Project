import allure

from Configuration.Context import TestData
from Pages.AddUsersPage import AddUsers
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.SmartWindowsPage import SmartWindows
from Tests.Test_conf import BaseTest


@allure.title("TEST SUITE 3")
@allure.feature("Smart Windows Module")
class Test_SmartWindows(BaseTest):
    @allure.title("Add Schedule")
    @allure.severity(allure.severity_level.NORMAL)
    def test_smartWindows(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.click_users = HomePage(self.driver)
        self.click_users.sel_users()
        self.smart_windows = SmartWindows(self.driver)
        self.smart_windows.smart_windows()
        self.smart_windows.add_schedule(TestData.SCHEDULE_NAME, TestData.STARTTIME, TestData.ENDTIME)
        self.smart_windows.search_schedule(TestData.SEARCHSCHEDULES)
        self.smart_windows.add_filter(TestData.FROMDATE, TestData.TODATE)
