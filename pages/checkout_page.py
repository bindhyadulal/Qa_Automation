from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    CANCEL_BTN = (By.ID, "cancel")
    FINISH_BTN = (By.ID, "finish")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.send_keys(self.LAST_NAME_INPUT, last_name)

    def enter_zip_postal_code(self, zip_code):
        self.send_keys(self.ZIP_POSTAL_CODE_INPUT, zip_code)

    def click_continue(self, timeout=10):
        self.click(self.CONTINUE_BTN)
        # Wait until URL contains 'checkout-step-two.html' to confirm navigation
        WebDriverWait(self.driver, timeout).until(
            ec.url_contains("checkout-step-two.html")
        )

    def click_cancel(self):
        self.click(self.CANCEL_BTN)

    def click_finish(self, timeout=10):
        # Wait until Finish button is clickable before clicking
        WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable(self.FINISH_BTN)
        ).click()

    def get_current_url(self):
        return self.driver.current_url
