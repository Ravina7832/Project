from faker import Faker


class TestData:
    fake = Faker()
    BASE_URL = "https://cloud-qa.view.com/overview"
    USERNAME = "qa@view.com"
    PASSWORD = "viewnet195!"

    """ADD USERS"""
    FIRSTNAME = fake.first_name()
    LASTNAME = fake.last_name()
    PHONE = "8799665455"
    PASSWORD1 = "123456789"
    CONFIRMPASSWORD = "123456789"
    DATE = fake.date()
    EMAIL = fake.email()

    """SEARCH USERS"""
    SEARCH_NAME = fake.name()
    SEARCH_EMAIL = fake.email()

    """EDIT USER"""
    EDIT_FNAME = fake.first_name()
    EDIT_LNAME = fake.last_name()
    EDIT_EMAIL = "test0123@view.com"
    EDIT_PHONE = "7894561239"

    """DELETE USER"""
    DEL_SEARCH = "7894561239"

    """ADD SCHEDULE"""
    SCHEDULE_NAME = "Automatic"
    STARTTIME = "0930A"
    ENDTIME = "1030P"

    """SEARCH ZONES"""
    SEARCHZONES = "galaxy_test"
    SEARCHSCHEDULES = "Automatic"

    """Filter"""
    FROMDATE = "10062021"
    TODATE = "10302021"

    """EDIT SCHEDULE"""
    EDIT_NAME = "Automatic Edit"
    EDIT_START_TIME = "1250P"
    EDIT_END_TIME = "0805A"
