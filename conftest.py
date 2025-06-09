import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # or use Firefox, Edge etc.
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
