from drivers.windows_chrome_driver import WindowsChromeDriver

from funcs.resize_driver_to_propper_height import resize_driver_to_propper_height
from funcs.execute_cleanup_scripts import execute_cleanup_scripts
from funcs.convert_image_to_pdf import convert_image_to_pdf

# Consts
# url = 'http://dev.azati.ai/portfolio/customer-profile-scraping/'
url = 'http://dev.azati.ai/advanced-scraping-platform-for-cellular-data-extraction/'
xpath = '//div[@id="page"]'
file_name = 'test'
image_path = './temp/%s.png' % file_name
pdf_path = './temp/%s.pdf' % file_name

# Create new driver instance
driver = WindowsChromeDriver()

# Init driver
driver.driver_init()

# Get required page
driver.get_url(url)

# Execute JavaScript to cleanup unnecessary HTML tags
execute_cleanup_scripts(driver.get_driver())

# Select the biggest element on the page
biggest_element = driver.select_element(xpath)

# Resize driver to cover all page
resize_driver_to_propper_height(
    driver.get_driver(), biggest_element)

# Get Screenshot in Base64
# driver.make_screenshot(biggest_element, image_path)
base64 = driver.get_screenshot_string(biggest_element)
# convert_image_to_pdf(image_path, pdf_path)
convert_image_to_pdf(base64, pdf_path)

# Close driver after all
driver.driver_close()
