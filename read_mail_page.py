from page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait

class ReadMailPage(BasePage):

    def open(self):
        driver = self.driver
        mail = WebDriverWait(driver,10).until(lambda driver :driver.find_element_by_xpath('//table[@class="F cf zt"]/tbody/tr[1]'))
        mail.click()


