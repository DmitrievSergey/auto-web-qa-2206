from src.page_objects.ItemPage import ItemPage


def test_search(browser):
    ItemPage(browser) \
        .open_item_page() \
        .verify_delivery_date_input_presence() \
        .verify_price_in_reward_points_presence() \
        .verify_product_name_presence() \
        .verify_product_price_presence() \
        .verify_product_tax_presence()
