import pytest
import json
import os
from pages.login_page import LoginPage

def load_login_data(filename):
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, '..', 'TestData', filename)
    with open(data_path, 'r') as f:
        return json.load(f)

login_test_data = load_login_data('login_users.json')

@pytest.mark.parametrize("username,password,expected_error", [
    (item["username"], item["password"], item.get("expected_error"))
    for item in login_test_data
])
def test_saucedemo_users_login(driver, username, password, expected_error):
    login = LoginPage(driver)
    login.login(username, password)

    if expected_error:
        # Expecting an error message (locked_out_user)
        assert expected_error in login.get_error_text()
    else:
        # Expecting successful login: check URL contains 'inventory'
        assert "inventory" in driver.current_url

    driver.get("https://www.saucedemo.com/")
