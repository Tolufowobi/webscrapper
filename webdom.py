from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import webscrapper.headlessbrowser 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PageSource:

    def __init__(self, headless_browser):
        self.__browser = headless_browser
        self.__source = self.__browser.driver.page_source

    @property
    def page_url(self):
        return self.__browser.web_url

    @property
    def page_title(self):
        return self.__browser.page_title

    def __batch_constructor(self, constructor, elementslist):
        objects = []
        for e in elementslist:
            objects.append(constructor(self, e))
        return objects
    
    def __find_elements_by_tagname(self, tagname):
        elements = []
        elements = self.__browser.driver.find_elements_by_tag_name(tagname)
        return elements

    def get_tag_by_id(self, tagid):
        self.__wait = WebDriverWait(self.__browser.driver, 15)
        self.__wait.until(EC.presence_of_element_located((By.ID, tagid)))
        #element = [e for e in self.__browser.driver.find_element_by_id(tagid)]
        element = self.__browser.driver.find_element_by_id(tagid)
        return WebPageTag(self,"WebPageTag", element)
        
    def get_tag_by_classname(self, classname):
        try:
            element = self.__browser.driver.find_element_by_class_name(classname)
            tag = WebPageTag(self, "WebPageTag", element)
            return tag
        except Exception as e:
            print(e)
            return None

    def get_tag_by_xpath(self, path):
        try:
            element = self.__browser.driver.find_element_by_xpath(path)
            tag = WebPageTag(self, "WebPageTag", element)
            return tag
        except Exception as e:
            print(e)
            return None

    def get_tags_by_classname(self, classname):
        try:
            elements = [e for e in self.__browser.driver.find_elements_by_class_name(classname)]
            tags = []
            for e in elements:
                tags.append(WebPageTag(self, e, "WebPageTag"))
            return tags
        except:
            return None

    def find_tags_by_type_and_property(self, tagtype, ppty, value):
        try:
            elements = [e for e in self.__find_elements_by_tagname(tagtype) if e.get_attribute(ppty) == value]
            tags = []
            for e in elements:
                tags.append(WebPageTag(self, e, "WebPageTag"))
            return tags
        except:
            return None
        
    def get_button_by_id(self, buttonid):
        element = [e for e in self.__find_elements_by_tagname('button') if e.get_attribute("id") == buttonid][0]
        tag = ButtonTag(self, element)
        return tag

    def get_buttons_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('button') if e.get_attribute('class') == classname]
        constructor = lambda s, e: ButtonTag(s, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags

    def get_submitbutton_by_id(self, buttonid):
        element = [e for e in self.__find_elements_by_tagname('input') if e.get_attribute() == buttonid and e.get_attribute('type') == 'submit'][0]
        tag = ButtonTag(self, element)
        return tag

    def get_submitbuttons_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('input') if e.get_attribute("class") == classname and e.get_attribute('type') == 'submit']
        constructor = lambda s, e: ButtonTag(s, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags

    def get_link_by_id(self, linkid):
        element = [e for e in self.__find_elements_by_tagname('a') if e.get_attribute('id') == linkid][0]
        tag = LinkTag(self, element)
        return tag

    def get_links_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('a') if e.get_property("class") == classname]
        constructor = lambda s, e: LinkTag(s, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags

    def get_form_by_id(self, formid):
        element = [e for e in self.__find_elements_by_tagname('form') if e.get_attribute('id') == formid][0]
        tag = FormTag(self, element)
        return tag

    def get_forms_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('form') if e.get_property("class") == classname]
        constructor = lambda s, e: ButtonTag(s, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags

    def get_textbox_by_id(self, textboxid):
        element = [e for e in self.__find_elements_by_tagname('input') if e.get_attribute('id') == textboxid and e.get_attribute('type') == 'text'][0]
        tag = TextBoxTag(self, element)
        return tag

    def get_textboxes_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('input') if e.get_attribute("class") == classname and e.get_attribute('type') == 'text']
        constructor = lambda s, e: TextBoxTag(s, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags

    def get_select_by_id(self, selectid):
        element = [e for e in self.__find_elements_by_tagname('select') if e.get_attribute('id') == selectid][0]
        tag = SelectTag(self, element)
        return tag

    def get_selecttags_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('select') if e.get_attribute("class") == classname]
        constructor = lambda s, e: SelectTag(s, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags

    def get_radiobutton_by_id(self, radiobuttonid):
        element = [e for e in self.__find_elements_by_tagname('input') if e.get_attribute('id') == radiobuttonid and e.get_attribute('type') == 'radio'][0]
        tag = RadioButtonTag(self, element)
        return tag

    def get_radiobuttons_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('input') if e.get_attribute("class") == classname and e.get_attribute('type') == 'radio']
        constructor = lambda s, e: RadioButtonTag(s, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags

    def get_datetimepicker_by_id(self, datetimepickerid):
        element = [e for e in self.__find_elements_by_tagname('input') if e.get_attribute('id') == datetimepickerid and e.get_attribute('type') == 'datetime-local'][0]
        tag = DateTimePickerTag(self, element)
        return tag

    def get_datetimepickers_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('input') if e.get_attribute('class') == classname and e.get_attribute('type') == 'datetime-local']
        constructor = lambda s, e: RadioButtonTag(self, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags
        
    def get_orderedlist_by_id(self, orderedlistid):
        element = [e for e in self.__find_elements_by_tagname('ol') if e.get_attribute('id') == orderedlistid ][0]
        tag = OrderedListTag(self, element)
        return tag

    def get_orderedlists_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('ol') if e.get_attribute('class') == classname]
        constructor = lambda s, e: OrderedListTag(s, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags

    def get_unorderedlist_by_id(self, unorderedlistid):
        element = [e for e in self.__find_elements_by_tagname('ul') if e.get_attribute('id') == unorderedlistid ][0]
        tag = UnorderedListTag(self, element)
        return tag

    def get_unorderedlists_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('ul') if e.get_attribute('class') == classname]
        constructor = lambda s, e: UnorderedListTag(s, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags

    def get_image_by_id(self, imageid):
        element = [e for e in self.__find_elements_by_tagname('img') if e.get_attribute('id') == imageid][0]
        tag = ImageTag(self, element)
        return tag

    def get_Images_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('img') if e.get_attribute('class') == classname]
        constructor = lambda s, e: ImageTag(s, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags

    def get_table_by_id(self, tableid):
        element = [e for e in self.__find_elements_by_tagname('table') if e.get_attribute('id') == tableid][0]
        tag = TableTag(self, element)
        return tag

    def get_table_by_classname(self, classname):
        elements = [e for e in self.__find_elements_by_tagname('table') if e.get_attribute('class') == classname]
        constructor = lambda s, e: TableTag(s, e)
        tags = self.__batch_constructor(constructor, elements)
        return tags
    
    def __str__(self):
        if self.__browser is not None:
            return self.__browser.driver.page_source
        else:
            return ""

class WebPageTag:

    def __init__(self, sourcepage, tagtype,webelement):
        self.__tagtype = tagtype
        self.__webelement = webelement
        self.__pagesource = sourcepage

    def get_tag_id(self):
        return self.webelement.get_attribute('id')

    def get_tag_classname(self):
        return self.webelement.get_attribute('class')

    def get_text(self):
        return self.webelement.text

    def click_to_upload(self, file):
        try:
            self.webelement._upload(file)
        except Exception as e:
            print(e)

    def click(self):
        try:
            self.webelement.click()
        except Exception as e:
            print(e)

    def focus(self):
        try:
            self.webelement.focus()
        except Exception as e:
            print(e)

    @property
    def webelement(self):
        return self.__webelement

class ButtonTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        WebPageTag.__init__(self, sourcepage, "Button", webelement)

    @property
    def tagtype(self):
        return self.__tagtype

class LinkTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        self.__tagtype = "Link"
        WebPageTag.__init__(self, sourcepage, self.__tagtype, webelement)

    @property
    def tagtype(self):
        return self.__tagtype

    def click(self):
        self.webelement.click()

class FormTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        WebPageTag.__init__(self, sourcepage, "Form", webelement)

    @property
    def tagtype(self):
        return self.__tagtype
    
    def submit(self):
        self.webelement.submit()

class InputTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        WebPageTag.__init__(self, sourcepage, "Input", webelement)

    @property
    def tagtype(self):
        return self.__tagtype

    def get_text_value(self):
        return self.webelement.get_attribute('value')

    def entertext(self, text):
        return self.webelement.send_keys(text)

class TextBoxTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        WebPageTag.__init__(self, sourcepage, "TextBox", webelement)

    @property
    def tagtype(self):
        return self.__tagtype

    def get_text_value(self):
        return self.webelement.get_attribute('value')

    def entertext(self, text):
        return self.webelement.send_keys(text)

class SelectTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        WebPageTag.__init__(self, sourcepage,"Select", webelement)
        self.__options = []
        optionselements = webelement.find_elements_by_tag_name('option')
        for o in optionselements:
            self.__options.append(SelectOptionTag(sourcepage, self, o))

    @property
    def tagtype(self):
        return self.__tagtype

    @property
    def options(self):
        return self.__options

class SelectOptionTag(WebPageTag):
    def __init__(self, sourcepage, parentselect, webelement):
        WebPageTag.__init__(self, sourcepage, "Option", webelement)
        self.__parentselect = parentselect

    @property
    def tagtype(self):
        return self.__tagtype

    @property
    def parentselect(self):
        return self.__parentselect

    def select(self):
        return self.webelement.click()

    def is_selected(self):
        return self.webelement.is_selected()

class RadioButtonTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        WebPageTag.__init__(self, sourcepage, "RadioButton", webelement)

    @property
    def tagtype(self):
        return self.__tagtype

    def select(self):
        return self.webelement.click()

    def is_selected(self):
        return self.webelement.is_selected()

class DateTimePickerTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        WebPageTag.__init__(self, sourcepage, "DateTimePicker", webelement)

    @property
    def tagtype(self):
        return self.__tagtype   

class OrderedListTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        WebPageTag.__init__(self, sourcepage,"OrderedList", webelement)
        self.__listitems = []
        itemelements = webelement.find_elements_by_tag_name('li')
        for i in itemelements:
            self.__listitems.append(ListItemTag(sourcepage, self, i))

    @property
    def tagtype(self):
        return self.__tagtype

    @property
    def listitems(self):
        return self.__listitems

class UnorderedListTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        WebPageTag.__init__(self, sourcepage, "UnorderedList", webelement)
        self.__listitems = []
        itemelements = webelement.find_elements_by_tag_name('li')
        for i in itemelements:
            self.__listitems.append(ListItemTag(sourcepage, self, i))

    @property
    def tagtype(self):
        return self.__tagtype

    @property
    def listitems(self):
        return self.__listitems

class ListItemTag(WebPageTag):
    def __init__(self, sourcepage, parentlist, webelement):
        WebPageTag.__init__(self, sourcepage, "ListItem", webelement)
        self.__parentlist = parentlist

    @property
    def tagtype(self):
        return self.__tagtype

    @property
    def parentlist(self):
        return self.__parentlist

class ImageTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        WebPageTag.__init__(self, sourcepage, "Image", webelement)

    @property
    def tagtype(self):
        return self.__tagtype

class TableTag(WebPageTag):
    def __init__(self, sourcepage, webelement):
        WebPageTag.__init__(self, sourcepage, "Table", webelement) 
        self.__tablerows = []
        rowelements = []
        try:
            header = self.__webelement.find_element_by_tag_name('thead')
            hr = header.find_elements_by_tag_name('tr')
            self.__tableheader = TableRowTag(sourcepage, self, hr, 0)
        except:
            pass

        try:
            body = self.__webelement.find_element_by_tag_name('tbody')
            rowelements = body.__webelement.find_elements_by_tag_name('tr')
        except:
            pass
    
        index = 1
        if len(rowelements) == 0:
            rowelements = self.__webelement.find_elements_by_tag_name('tr')
        
        for r in rowelements:
            if len(r.find_elements_by_tag_name('th')) > 0 and self.__tableheader is None:
                self.__tableheader = TableRowTag(sourcepage, self, r, 0)
            else:
                self.__tablerows.append(TableRowTag(sourcepage, self, r, index))
                index += 1

    @property
    def tagtype(self):
        return self.__tagtype

    @property
    def tableheader(self):
        return self.__tableheader

    @property
    def tablerows(self):
        return self.__tablerows


class TableRowTag(WebPageTag):
    def __init__(self, sourcepage, table, webelement, index):
        WebPageTag.__init__(self, sourcepage, "TableRow", webelement)
        self.__rowtable = table
        self.__rowindex = index
        self.__rowcells = []
        if self.__rowindex  == 0:
            cellelements = webelement.find_elements_by_tag_name('th')
        else:
            cellelements = webelement.find_elements_by_tag_name('td')
        
        index = 0
        for c in cellelements:
            self.__rowcells.append(TableCellTag(sourcepage, self, c, index))
            index += 1

    @property
    def rowtable(self):
        return self.__rowtable

    @property
    def rowcells(self):
        return self.__rowcells

    @property
    def rowindex(self):
        return self.__rowindex

class TableCellTag(WebPageTag):
    def __init__(self, sourcepage, cellrow, webelement, index):
        WebPageTag.__init__(self, sourcepage, "TableCell", webelement)
        self.__cellrow = cellrow
        self.__cellindex = index

    @property
    def cellrow(self):
        return self.__cellrow

    @property
    def celldata(self):
        return self.webelement.text

    @property
    def cellindex(self):
        return self.__cellindex
