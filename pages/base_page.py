#from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        elem = self.wait.until(ec.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def wait_for_element_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def wait_for_element_present(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def verify_element_present(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def validate_text(self, locator, expected_text):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        actual_text = element.text.strip()
        return actual_text == expected_text

    def get_element_attribute(self, locator, attribute_name):
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element.get_attribute(attribute_name)

    def get_number_of_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements)

    def hover_mouse(self, locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def send_keys(self, locator, text):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)