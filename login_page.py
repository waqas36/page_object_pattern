
from page import BasePage
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage(BasePage):

    def login(self,email,password):

        driver = self.driver
        inputElement = driver.find_element_by_id("Email")
        inputElement.send_keys(email)
        next_button = driver.find_element_by_id("next")
        next_button.click()
        pass_field = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("Passwd"))
        pass_field.send_keys(password)
        sign_in_button = driver.find_element_by_id("signIn")
        sign_in_button.click()



