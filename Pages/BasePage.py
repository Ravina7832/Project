import functools
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def take_screenshot_on_failure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            allure.attach(args[0].driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
            raise

    return wrapper


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert element.is_displayed()
        return element

    def do_click(self, by_locator):
        self.wait_for_element(by_locator).click()

    def clear(self, by_locator):
        self.wait_for_element(by_locator).clear()

    def do_send_keys(self, by_locator, text):
        self.wait_for_element(by_locator).send_keys(text)

    def get_element_text(self, by_locator):
        element = self.wait_for_element(by_locator)
        return element.text

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def is_displayed(self,by_locator):
        self.wait_for_element(by_locator)

    def back_space(self, by_locator):
        self.wait_for_element(by_locator).click()
        self.wait_for_element(by_locator).send_keys(Keys.CONTROL + 'a', Keys.DELETE)


