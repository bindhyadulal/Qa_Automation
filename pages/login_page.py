from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_TEXT = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_username_placeholder(self):
        return self.get_element_attribute(self.USERNAME_INPUT, "placeholder")

    def get_password_placeholder(self):
        return self.get_element_attribute(self.PASSWORD_INPUT, "placeholder")

    def get_login_button_text(self):
        return self.get_element_attribute(self.LOGIN_BUTTON, "value")

    def get_error_text(self):
        return self.wait_for_element_visible(self.ERROR_TEXT).text

    def is_error_displayed(self):
        return self.verify_element_present(self.ERROR_TEXT)

    def load(self):
        self.driver.get("https://www.saucedemo.com/")
