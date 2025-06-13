import json
import os
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest
def load_test_data(filename):
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, '..', 'TestData', filename)
    with open(data_path, 'r') as f:
        return json.load(f)
pytest_mark = [pytest.mark.checkout]
class TestCheckoutPage:
    @pytest.mark.smoke
    def test_checkout_form_submission(self, inventory: InventoryPage, cart: CartPage, checkout: CheckoutPage):
        test_data = load_test_data('checkout_data.json')

        # Adding item in cart
        inventory.add_first_item_to_cart()
        inventory.go_to_cart()
        #checkout
        cart.click_checkout()

        checkout.enter_first_name(test_data["first_name"])
        checkout.enter_last_name(test_data["last_name"])
        checkout.enter_zip_postal_code(test_data["zip_code"])
        checkout.click_continue()

        assert "checkout-step-two.html" in checkout.get_current_url()

    @pytest.mark.regression
    def test_cancel_checkout_goes_back_to_cart(self, inventory: InventoryPage, cart: CartPage, checkout: CheckoutPage):
        test_data = load_test_data('checkout_data.json')

        inventory.add_first_item_to_cart()
        inventory.go_to_cart()
        cart.click_checkout()

        checkout.click_cancel()

        # After cancel, should navigate back to cart page
        assert "cart.html" in checkout.get_current_url()

    @pytest.mark.smoke
    def test_finish_checkout_redirects_to_complete(self, inventory: InventoryPage, cart: CartPage, checkout: CheckoutPage):
        test_data = load_test_data('checkout_data.json')

        inventory.add_first_item_to_cart()
        inventory.go_to_cart()
        cart.click_checkout()

        checkout.enter_first_name(test_data["first_name"])
        checkout.enter_last_name(test_data["last_name"])
        checkout.enter_zip_postal_code(test_data["zip_code"])
        checkout.click_continue()
        checkout.click_finish()

        # Final page should be order complete page
        assert "checkout-complete.html" in checkout.get_current_url()
