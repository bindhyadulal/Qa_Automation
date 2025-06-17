import json
import os
import pytest
from pages.login_page import LoginPage

def load_valid_login_data():
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, '..', 'TestData', 'valid_login_data.json')
    with open(data_path, 'r') as f:
        return [(entry["username"], entry["password"]) for entry in json.load(f)]

class TestLoginPage:

    def test_login_page_contents(self, driver):
        login = LoginPage(driver)
        login.load()
        assert "Swag Labs" in driver.title, "Title does not contain 'Swag Labs'"

    def test_username_required(self, driver):
        login = LoginPage(driver)
        login.load()
        login.login("", "secret_sauce")
        assert login.validate_text(LoginPage.ERROR_TEXT, "Epic sadface: Username is required")

    def test_password_required(self, driver):
        login = LoginPage(driver)
        login.load()
        login.login("standard_user", "")
        assert login.validate_text(LoginPage.ERROR_TEXT, "Epic sadface: Password is required")

    def test_invalid_credentials(self, driver):
        login = LoginPage(driver)
        login.load()
        login.login("invalid_user", "invalid_pass")
        assert login.validate_text(LoginPage.ERROR_TEXT, "Epic sadface: Username and password do not match any user in this service")

    def test_locked_out_user(self, driver):
        login = LoginPage(driver)
        login.load()
        login.login("locked_out_user", "secret_sauce")
        assert login.validate_text(LoginPage.ERROR_TEXT, "Epic sadface: Sorry, this user has been locked out.")

    def test_username_placeholder(self, driver):
        login = LoginPage(driver)
        login.load()
        assert login.get_username_placeholder() == "Username"

    def test_password_placeholder(self, driver):
        login = LoginPage(driver)
        login.load()
        assert login.get_password_placeholder() == "Password"

    def test_login_button_text(self, driver):
        login = LoginPage(driver)
        login.load()
        assert login.get_login_button_text() == "Login"

    @pytest.mark.smoke
    @pytest.mark.parametrize("username,password", load_valid_login_data())
    def test_valid_login(self, driver, username, password):
        login = LoginPage(driver)
        login.load()
        login.login(username, password)
        assert "inventory.html" in driver.current_url