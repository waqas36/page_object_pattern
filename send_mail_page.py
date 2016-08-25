from page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


class SendMailPage(BasePage):

    def send_mail(self,to,subject,data):
        driver = self.driver
        compose = WebDriverWait(driver,10).until(lambda driver :driver.find_element_by_xpath("//div[contains(text(),'COMPOSE')]"))
        compose.click()
        to = WebDriverWait(driver,10).until( lambda driver :driver.find_element_by_xpath("//textarea[@aria-label='To']"))
        to.send_keys("waqasgem@gmail.com"+Keys.ENTER)
        subject = driver.find_element_by_xpath("//input[@name='subjectbox']")
        subject.send_keys("test ")
        send = driver.find_element_by_xpath("//div[contains(text(),'Send')]")
        send.click()




