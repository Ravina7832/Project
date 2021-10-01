from Configuration.Context import TestData
from Pages.AddUsersPage import AddUsers
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.SmartWindowsPage import SmartWindows
from Tests.Test_conf import BaseTest


class Test_SmartWindows(BaseTest):
    def test_smartwindows(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        # self.click_user = HomePage(self.driver)
        # self.click_user.sel_users()
        # self.add_Users = AddUsers(self.driver)
        # self.add_Users.add_users(TestData.FIRSTNAME, TestData.LASTNAME, TestData.EMAIL, TestData.PHONE, TestData.PASSWORD1, TestData.CONFIRMPASSWORD, TestData.DATE)
        # self.search = AddUsers(self.driver)
        # self.search.search_users(TestData.SEARCH)
        self.smart_windows = SmartWindows(self.driver)
        self.smart_windows.smart_windows(TestData.SCHEDULE_NAME, TestData.STARTTIME, TestData.ENDTIME, TestData.SEARCHSCHEDULES, TestData.FROMDATE, TestData.TODATE)
