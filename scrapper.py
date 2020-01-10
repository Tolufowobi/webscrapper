import os
import shutil
from webscrapper.headlessbrowser import HeadlessBrowser
import webscrapper.webdom 
from selenium import webdriver



class Scrapper:
    def __init__(self, weburl, targetbrowser, driverlocation):
        self.__workingbrowser = HeadlessBrowser(targetbrowser, driverlocation)
        self.__targeturl = weburl
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.workingbrowser.close()
        del self.workingbrowser

    @property 
    def workingbrowser(self):
        return self.__workingbrowser

    @property
    def targeturl(self):
        return self.__targeturl

    def loadpage(self, url="",conditionaltag=""):
        try:
            if url == "":
                url = self.__targeturl
            else:
                self.__targeturl = url
            if conditionaltag == "":
                self.workingbrowser.load_pagesource(self.__targeturl)
            else:
                self.workingbrowser.load_pagesource_condtionally(self.__targeturl,conditionaltag)
        except Exception as e:
            print(e)

    def upload_file(self, filelocation, elementid):
        try:
            self.workingbrowser.current_pagesource.get_tag_by_id(elementid).click_to_upload(filelocation)
            return True
        except Exception as e:
            print(e)
            return False

    def download_file(self, triggertag, destinationlocation):
        try:
            self.workingbrowser.driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
            params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': destinationlocation}}
            self.workingbrowser.driver.execute("send_command", params)
            triggertag.click()
            return True
        except Exception as e:
            print(e)
            return False
    
    def click_button(self, buttonid):
        try:
            self.workingbrowser.current_pagesource.get_button_by_id(buttonid).click()
            return True
        except Exception as e:
            print(e)
            return False

    def enter_text(self, textboxid, textvalue):
        try:
            self.workingbrowser.current_pagesource.get_textbox_by_id(textboxid).entertext(textvalue)
            return True
        except Exception as e:
            print(e)
            return False

    def get_tag_value(self, tagid):
        try:
            return self.workingbrowser.current_pagesource.get_tag_by_id(tagid).get_text()
        except Exception as e:
            print(e)
            return ""

    def submit_form(self, formid):
        try:
            self.workingbrowser.current_pagesource.get_form_by_id(formid).submit()
            return True
        except Exception as e:
            print(e)
            return False

    def select_from_selecttag(self, selecttagid, selectoption):
        try:
            selecttag = self.workingbrowser.current_pagesource.get_select_by_id(selecttagid)
            flag=False
            for o in selecttag.options:
                if o.get_text().strip() == selectoption:
                    o.select()
                    flag=True
                    break
            return flag
        except Exception as e:
            print(e)
            return False

    def lift_table(self, tableid):
        table = self.workingbrowser.current_pagesource.get_table_by_id(tableid)
        return table
    
    def element_exists(self, elementkey):
        try:
            if len(self.workingbrowser.driver.find_elements_by_id(elementkey)) > 0:
                return True
        except:
            try:
                if len(self.workingbrowser.driver.find_elements_by_xpath(elementkey)) > 0:
                    return True
            except:
                try:
                    if len(self.workingbrowser.driver.find_elements_by_class_name(elementkey)) > 0:
                        return True
                except:
                    try:
                        if len(self.workingbrowser.driver.find_elements_by_tag_name(elementkey)) > 0:
                            return True
                    except Exception as e:
                        print(e)
                        return False
            

    def execute_js_function(self,function_name):
        try:
            self.workingbrowser.driver.execute_script(function_name)
            return True
        except Exception as e:
            print(e)
            return False