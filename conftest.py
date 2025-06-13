import pytest
from selenium import webdriver
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions();
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
@pytest.fixture
def inventory(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    return InventoryPage(driver)

@pytest.fixture
def cart(driver):
    return CartPage(driver)

@pytest.fixture
def checkout(driver):
    return CheckoutPage(driver)