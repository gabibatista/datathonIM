import config
import time
import os
from common.locators import Locator
from common.navigate.nav import NavigatePage
from browser.setup.browser_setup import BrowserSetup

def run():
    print("========Starting Crawler======\n")
    driver = BrowserSetup()
    driver.setup()
    try:
        locators = Locator("linkedin")
        nav = NavigatePage(driver.browser)
        el1 = nav.navigate(locators.url).access(locators['button_login'])
        print("COLETA DE OBJ: ", el1)
    except Exception as e:
        print(e)
        pass

    driver.tear_down()
    print("\n========Finished Crawler======")

if __name__ == "__main__":
    run()
