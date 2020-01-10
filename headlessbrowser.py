
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import os
import csv
from webscrapper.webdom import PageSource
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class HeadlessBrowser:

    defaultdownloadlocation = os.path.dirname(os.path.dirname(__file__)) + "\\headlessbrowserdownloads"

    def __init__(self, browsertype, browserservicelocation: str):
        if browsertype == "Chrome":
            self.__options = Options()
            #self.__options.add_argument('--headless')
            # self.__options.add_argument('--no-sandbox')
            self.__options.add_argument('--disable-popup-blocking')
            self.__options.add_argument('--disable-notifications')
            self.__options.add_argument('--disable-gpu')
            self.__options.add_argument('--disable-software-rasterizer')
            self.__preferencesdict = {"download.default_directory": HeadlessBrowser.defaultdownloadlocation, "download.prompt_for_download": False,
                                      "download.directory_upgrade": True, "safebrowsing_for_trusted_sources_enabled": False, "safebrowsing.enable": False}
            self.__options.add_experimental_option(
                "prefs", self.__preferencesdict)
            self.__driver = webdriver.Chrome(
                browserservicelocation, chrome_options=self.__options)
        elif browsertype == "Mozilla":
            self.__driver = webdriver.Firefox(browserservicelocation)
        self.__web_url = ""
        self.__current_pagesource = None

    @property
    def web_url(self):
        return self.__web_url

    @property
    def driver(self):
        return self.__driver

    @property
    def current_pagesource(self):
        #self.driver.execute_script("return document.body")
        return self.__current_pagesource

    def load_pagesource(self, url):
        try:
            self.__web_url = url
            self.driver.get(self.__web_url)
            self.driver.execute_script("return document.body")
            self.__current_pagesource = PageSource(self)
            return self.__current_pagesource
        except Exception as e:
            print(e)
            return None

    def load_pagesource_condtionally(self, url, contional_tag_id):
        try:
            self.__web_url = url
            self.driver.get(self.__web_url)
            self.__wait = WebDriverWait(self.driver, 15)
            self.__wait.until(EC.presence_of_element_located((By.ID, contional_tag_id)))
            self.__current_pagesource = PageSource(self)
            print(self.__current_pagesource)
            return self.__current_pagesource
        except Exception as e:
            print(e)
            return None

    def upload_by_pagetag(self, webpagetag):
        self.driver.find_element_by_id(webpagetag.id)

    def close(self):
        self.driver.close()
        self.driver.quit()
        self.web_url = ""
        self.__current_pagesource = None
        self.driver = None


class ChromeHeadlessBrowser(HeadlessBrowser):

    def __init__(self, browserservicepath):
        HeadlessBrowser.__init__(
            self, browsertype="Chrome", browserservicelocation=browserservicepath)

    def load_page_source(self, weburl):
        page = PageSource(self)
        return page
