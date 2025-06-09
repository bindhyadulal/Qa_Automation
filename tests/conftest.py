import time
import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# WebDriver fixture
@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    time.sleep(3)  # optional: to visually confirm the page loaded

    yield driver

    time.sleep(3)  # optional: to visually confirm the last state before quit
    driver.quit()

# Inventory fixture
@pytest.fixture(scope="session")
def inventory(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.wait_for_inventory_page()

    return inventory_page
@pytest.fixture
def cart(driver):
    return CartPage(driver)
@pytest.fixture
def checkout(driver):
    return CheckoutPage(driver)

