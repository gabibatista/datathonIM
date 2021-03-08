import config
import time
import os
from common.locators import Locator
from common.navigate.nav import NavigatePage
from browser.browser_setup import BrowserSetup

def load_companies_names():
    return ['Dextra', 'Apple', 'Amazon']

def open_login():

    try:
        locators = Locator("linkedin_jobs")
        print('print locator',locators['username'])
    except:
        print('error locator')

    driver = BrowserSetup()
    driver.setup()

    nav = NavigatePage(driver.browser)
    nav.navigate('https://www.linkedin.com/uas/login')

    username_field = nav.get_classname(locators['username'])
    password_field = nav.get_classname(locators['password'])

    username_field.send_keys('zeipf1@gmail.com')
    password_field.send_keys('zeipf1@gmail.com')



def get_jobs_for(company, limit: int = 10000):

    print("========Starting Crawler======\n")
    driver = BrowserSetup()
    driver.setup()

    jobs_list = []
    try:
        locators = Locator("linkedin_jobs")
        nav = NavigatePage(driver.browser)
        carousel = nav.navigate(locators.url).access(locators['pages_carousel'])
        jobs_list = nav.navigate(locators.url).access(locators['jobs_list'])
        print("COLETA DE OBJ: ", carousel)
        print("COLETA DE OBJ: ", jobs_list)
    except Exception as e:
        print(e)
        pass
    
    for li in jobs_list:
        print('Item: ',li)

    #driver.tear_down()
    #print("\n========Finished Crawler======")

if __name__ == "__main__":
    open_login()
