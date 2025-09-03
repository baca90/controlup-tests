def test_cart(log_to_application):
    cuip_page = log_to_application
    cuip_page.click_button_by_text("Add to cart")
    assert cuip_page.get_cart_items_count() == "1"
