def test_inventory(log_to_application):
    cuip_page = log_to_application
    assert len(cuip_page.get_inventory_items()) == 6
