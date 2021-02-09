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
        for locator in locators:
            soup = nav.navigate(locators.url).access(locator['value'])
            print("COLETA DE OBJ: ", soup)
    except:
        pass

    time.sleep(5)
    driver.tear_down()
    print("\n========Finished Crawler======")

if __name__ == "__main__":
    run()
