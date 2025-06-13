import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

pytest_mark = [pytest.mark.cart]
class TestCartPage:
    @pytest.mark.smoke
    def test_add_item_to_cart_and_check(self, inventory: InventoryPage, cart: CartPage):
        inventory.add_first_item_to_cart()
        inventory.go_to_cart()
        assert cart.get_cart_item_count() == 1
        cart.click_continue_shopping()

    @pytest.mark.regression
    def test_remove_cart_item_and_check_count(self, inventory: InventoryPage, cart: CartPage):
        inventory.add_first_item_to_cart()
        inventory.go_to_cart()
        cart.remove_item()
        assert cart.get_cart_item_count() == 0
        cart.click_continue_shopping()

    @pytest.mark.smoke
    def test_checkout_button_is_clickable(self, inventory: InventoryPage, cart: CartPage):
        inventory.add_first_item_to_cart()
        inventory.go_to_cart()
        cart.click_checkout()
        assert "checkout-step-one.html" in cart.get_current_url()
