

class BasePage(object):
    "Page class that all page models can inherit from"

    def __init__(self,selenium_driver):
        "Constructor"

        self.driver = selenium_driver
        #Visit and initialize xpaths for the appropriate page

    def load(self,url):
        self.driver.get(url)


    def click_element(self,xpath):
        "Click the button supplied"

    def write(self,msg,level='info'):
        self.log_obj.write(msg,level)

