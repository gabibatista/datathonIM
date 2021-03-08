import os

from config import HEADLESS, PATH_BROWSER
from pyvirtualdisplay import Display
from selenium import webdriver


class BrowserSetup:
    
    def __init__(self):
        self.browser = None
        self.display = None
        self.shutdown = False

    def setup(self):
        '''
            Docstring
        '''
        #profile = webdriver.FirefoxProfile(os.path.join(os.environ.get("HOME"), "profile", "db"))
        profile = webdriver.FirefoxProfile(os.path.join(".profile", "db"))
        profile.set_preference("security.default_personal_cert", "Select Automatically")
        profile.accept_untrusted_certs = True

        # https://stackoverflow.com/questions/25251583/downloading-file-to-specified-location-with-selenium-and-python
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.panel.shown", False)
        # profile.set_preference("browser.download.dir", self.get_path_pdf())
        profile.set_preference("browser.helperApps.neverAsk.openFile", "application/pdf")
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        profile.set_preference("pdfjs.disabled", True)
        profile.set_preference("service_log_path", os.path.join(".profile", "db"))

        # use proxy - https://stackoverflow.com/questions/17082425/running-selenium-webdriver-with-a-proxy-in-python
        # proxy_host = '189.126.67.230'
        # proxy_port = 33499
        ## proxy_type = 1  # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
        # profile.set_preference("network.proxy.type", proxy_type)
        # profile.set_preference("network.proxy.http", proxy_host)
        # profile.set_preference("network.proxy.http_port", int(proxy_port))
        # profile.set_preference("network.proxy.https", proxy_host)
        # profile.set_preference("network.proxy.https_port", int(proxy_port))
        # profile.set_preference("network.proxy.ssl", proxy_host)
        # profile.set_preference("network.proxy.ssl_port", int(proxy_port))
        # profile.set_preference("network.proxy.ftp", proxy_host)
        # profile.set_preference("network.proxy.ftp_port", int(proxy_port))
        # profile.set_preference("network.proxy.socks", proxy_host)
        # profile.set_preference("network.proxy.socks_port", int(proxy_port))
        #  Use this to disable Acrobat plugin
        # for previewing PDFs in Firefox( if you have Adobe reader installed on your computer)
        profile.set_preference("plugin.scan.Acrobat", "99.0")
        profile.set_preference("plugin.scan.plid.all", False)
        profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")

        if HEADLESS:
            print("Browser Invisivel")
            # https://github.com/dimmg/dockselpy
            self.display = Display(visible=0, size=(1024, 768))
            self.display.start()
            self.browser = webdriver.Firefox(firefox_profile=profile)
        else:
            print("Browser visivel")
            firefox_binary = PATH_BROWSER
            self.browser = webdriver.Firefox(firefox_profile=profile, firefox_binary=firefox_binary)

    def tear_down(self):
        print("Finaliza browser")
        self.browser.close()
        self.browser.quit()
        if HEADLESS:
            self.display.stop()
            print("Display Xvfb finalizado!")
        print("Browser finalizado!")
