from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_IMAGE = (By.CLASS_NAME, "inventory_item_img")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    FOOTER = (By.CLASS_NAME, "footer_copy")
    BURGER_MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    MENU_CLOSE_BTN = (By.ID, "react-burger-cross-btn")

    # XPath Locators
    XPATH_TITLE = (By.XPATH, "//*[contains(@class, 'title')]")
    XPATH_INVENTORY_ITEMS = (By.XPATH, "//*[contains(@class, 'inventory_item')]")
    XPATH_ITEM_NAME = (By.XPATH, "//*[contains(@class, 'inventory_item_name')]")
    XPATH_ITEM_PRICE = (By.XPATH, "//*[contains(@class, 'inventory_item_price')]")
    XPATH_ITEM_IMAGE = (By.XPATH, "//*[contains(@class, 'inventory_item_img')]")
    XPATH_SORT_DROPDOWN = (By.XPATH, "//*[contains(@class, 'product_sort_container')]")
    XPATH_CART_ICON = (By.XPATH, "//*[contains(@class, 'shopping_cart_link')]")
    XPATH_CART_BADGE = (By.XPATH, "//*[contains(@class, 'shopping_cart_badge')]")
    XPATH_FOOTER = (By.XPATH, "//*[contains(@class, 'footer_copy')]")
    XPATH_BURGER_MENU_BTN = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    XPATH_MENU_CLOSE_BTN = (By.XPATH, "//button[@id='react-burger-cross-btn']")
    XPATH_LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")
    XPATH_LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_inventory_page(self):
        self.wait_for_element_visible(self.TITLE)

    def get_current_url(self):
        return self.driver.current_url

    def get_title_text(self):
        self.wait_for_inventory_page()
        return self.wait_for_element_visible(self.TITLE).text

    def get_inventory_item_count(self):
        return self.get_number_of_elements(self.INVENTORY_ITEMS)

    def get_all_product_names(self):
        elements = self.driver.find_elements(*self.ITEM_NAME)
        return [el.text.strip() for el in elements]

    def get_all_product_prices(self):
        elements = self.driver.find_elements(*self.ITEM_PRICE)
        return [float(el.text.replace("$", "")) for el in elements]

    def select_sort_option(self, option_text):
        dropdown = Select(self.wait_for_element_visible(self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(option_text)

    def add_first_item_to_cart(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if buttons:
            buttons[0].click()

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def is_footer_displayed(self):
        return self.verify_element_present(self.FOOTER)

    def is_item_image_displayed(self):
        return self.verify_element_present(self.ITEM_IMAGE)

    def open_menu(self):
        self.click(self.BURGER_MENU_BTN)

    def is_logout_visible(self):
        return self.verify_element_present(self.LOGOUT_LINK)

    def close_menu(self):
        self.click(self.MENU_CLOSE_BTN)

    def logout(self):
        self.open_menu()
        self.click(self.LOGOUT_LINK)
        self.wait.until(lambda d: "inventory.html" not in d.current_url)
