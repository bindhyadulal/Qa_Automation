from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(text(),'Remove')]")
    CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")
    CHECKOUT_BTN = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_item_count(self):
        return self.get_number_of_elements(self.CART_ITEMS)

    def get_cart_quantities(self):
        elements = self.driver.find_elements(*self.CART_QUANTITY)
        return [int(el.text) for el in elements]

    def remove_item(self):
        buttons = self.driver.find_elements(*self.REMOVE_BUTTON)
        if buttons:
            buttons[0].click()

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def get_current_url(self):
        return self.driver.current_url
