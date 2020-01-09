from funcs.resize_driver_to_propper_height import resize_driver_to_propper_height

from drivers.windows_chrome_driver import WindowsChromeDriver

# Consts
url = 'http://dev.azati.ai/portfolio/customer-profile-scraping/'
xpath = '//div[@id="page"]'

# Create new driver instance
driver = WindowsChromeDriver()

# Init driver
driver.driver_init()

# Get required page
driver.get_url(url)

# Select the biggest element on the page
biggest_element = driver.select_element(xpath)

# Resize driver to cover all page
resize_driver_to_propper_height(
    driver.get_driver(), biggest_element)

driver.make_screenshot(biggest_element, './test.png')

# Close driver after all
driver.driver_close()


# # Find the element with longest height on page
# element = driver.find_element("xpath", '//div[@id="page"]')

# # Get element height and resize windows to this height
# total_height = element.size["height"]
# driver.set_window_size(settings['windowWidth'], total_height)

# element.screenshot('big-body.png')

# # # Replace window to the longest avaliable height, wait for JS recalculation
# # driver.set_window_size(12000, 12000)
# # # driver.set_window_size(settings['windowWidth'], total_height)
# # time.sleep(settings["waitTimeout"])

# # # Take screenshot
# # element.screenshot('new_body.png')

# # print(driver.get_window_size())

# # Close driver
# driver.close()
