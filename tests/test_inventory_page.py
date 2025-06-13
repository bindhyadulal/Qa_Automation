from pages.inventory_page import InventoryPage
import pytest

pytest_mark = [pytest.mark.inventory]
class TestInventoryPage:

    @pytest.mark.smoke
    def test_inventory_url(self, inventory: InventoryPage):
        assert "inventory.html" in inventory.get_current_url()

    @pytest.mark.smoke
    def test_inventory_title(self, inventory: InventoryPage):
        assert inventory.get_title_text() == "Products"

    @pytest.mark.smoke
    def test_inventory_item_count(self, inventory: InventoryPage):
        assert inventory.get_inventory_item_count() == 6

    # Product Listing
    @pytest.mark.regression
    def test_all_product_names_displayed(self, inventory: InventoryPage):
        names = inventory.get_all_product_names()
        assert all(name.strip() != "" for name in names)

    # Sorting
    @pytest.mark.regression
    def test_product_sort_dropdown_present(self, inventory: InventoryPage):
        inventory.select_sort_option("Name (A to Z)")

    @pytest.mark.regression
    def test_sort_a_to_z(self, inventory: InventoryPage):
        inventory.select_sort_option("Name (A to Z)")
        names = inventory.get_all_product_names()
        assert names == sorted(names)

    @pytest.mark.regression
    def test_sort_price_low_to_high(self, inventory: InventoryPage):
        inventory.select_sort_option("Price (low to high)")
        prices = inventory.get_all_product_prices()
        assert prices == sorted(prices)

    # UI Elements & Menu
    @pytest.mark.regression
    def test_burger_menu_open(self, inventory: InventoryPage):
        inventory.open_menu()
        assert inventory.is_logout_visible()
        inventory.close_menu()

    @pytest.mark.smoke
    def test_footer_displayed(self, inventory: InventoryPage):
        assert inventory.is_footer_displayed()

    @pytest.mark.smoke
    def test_item_image_is_displayed(self, inventory: InventoryPage):
        assert inventory.is_item_image_displayed()

    # Logout
    @pytest.mark.smoke
    def test_logout(self, inventory: InventoryPage):
        inventory.logout()
        assert "inventory.html" not in inventory.get_current_url()
