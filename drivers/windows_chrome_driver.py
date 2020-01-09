import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WindowsChromeDriver(object):

    def __init__(self):
        self.__defaultDriverWidth = 1680
        self.__defaultDriverHeight = 1050
        self.__driverPath = './data/drivers/windows/chromedriver.exe'
        self.__jsLoadTimeOut = 5

    def driver_init(self):
        # Init driver with custom options
        options = Options()

        options.add_argument(
            "--window-size=%s,%s" % (self.__defaultDriverWidth, self.__defaultDriverHeight))
        options.add_argument("--headless")

        self.driver = webdriver.Chrome(
            executable_path=self.__driverPath, options=options)

        self.driver.set_window_position(0, 0)

    def get_default_width(self):
        return self.__defaultDriverWidth

    def get_default_height(self):
        return self.__defaultDriverHeight

    def get_driver(self):
        return self

    def get_url(self, url):
        self.driver.get(url)
        # Add small timeout to await JS execution
        time.sleep(self.__jsLoadTimeOut)

    def select_element(self, xpath):
        return self.driver.find_element("xpath", xpath)

    def make_screenshot(self, element, path):
        element.screenshot(path)

    def set_driver_size(self, width, height):
        self.driver.set_window_size(width, height)
        # Add small timeout to await JS re-execution
        time.sleep(self.__jsLoadTimeOut)

    def driver_close(self):
        self.driver.close()
