

def resize_driver_to_propper_height(driver, element):
    # Get element height and resize windows to this height
    total_height = element.size["height"]
    driver.set_driver_size(driver.get_default_width(), total_height)
