from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
# Core
from config import WAIT_TIME


class NavigatePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)
        return self

    def get_xpath(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=WAIT_TIME)
            res = wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            raise TimeoutException(f'Timeout while wait element: {locator}')

        return res

    def get_classname(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=WAIT_TIME)
            res = wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator)))
        except TimeoutException:
            raise TimeoutException(f'Timeout while wait element: {locator}')

        return res

    def access(self, locator,):
        sel = self.get_classname(locator)
        sel.click()
        return sel