import allure

from Project.Configuration.Context import TestData
from Project.Pages.HomePage import HomePage
from Project.Pages.LoginPage import LoginPage
from Project.Pages.SmartWindowsPage import SmartWindows
from Project.Tests.test_conf import BaseTest


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
        self.smart_windows.schedule_name(TestData.SCHEDULE_NAME)
        self.smart_windows.sel_tint()
        self.smart_windows.startdate()
        self.smart_windows.enddate()
        self.smart_windows.starttime(TestData.STARTTIME)
        self.smart_windows.endtime(TestData.ENDTIME)
        self.smart_windows.sel_days()
        self.smart_windows.sel_sun()
        self.smart_windows.sel_mon()
        self.smart_windows.sel_tues()
        self.smart_windows.sel_wed()
        self.smart_windows.sel_thurs()
        self.smart_windows.sel_fri()
        self.smart_windows.sel_sat()
        self.smart_windows.zone()
        self.smart_windows.schedule_save()
        self.smart_windows.verify_saved_schedule()
        self.smart_windows.search_schedule(TestData.SEARCHSCHEDULES)
        self.smart_windows.select_schedule()
        self.smart_windows.add_filter()
        self.smart_windows.st_date(TestData.FROMDATE)
        self.smart_windows.ed_date(TestData.TODATE)
        self.smart_windows.apply()
        self.smart_windows.edit_schedule()
        self.smart_windows.edit_name(TestData.EDIT_NAME)
        self.smart_windows.edit_starttime(TestData.EDIT_START_TIME)
        self.smart_windows.edit_endtime(TestData.EDIT_END_TIME)
