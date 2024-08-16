from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.CheckoutPage import CheckoutPage


class HomePage():

    shop_button = (By.XPATH, "//a[contains(@href,'shop')]")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    select = (By.ID, "exampleFormControlSelect1")
    option = (By.XPATH, "//input[@value='option1']")
    submit_button = (By.XPATH, "//input[@type='submit']")
    two_way_text = (By.XPATH, "(//input[@type='text'])[3]")
    success_message = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver) -> None:
        self.driver = driver

    def shop(self):
        # integration point with CheckoutPage
        self.driver.find_element(*HomePage.shop_button).click()
        return CheckoutPage(driver=self.driver)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)
    
    def get_email(self):
        return self.driver.find_element(*HomePage.email)
    
    def get_password(self):
        return self.driver.find_element(*HomePage.password)
    
    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)
    
    def get_option(self):
        return self.driver.find_element(*HomePage.option)
    
    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submit_button)
    
    def get_two_way_text(self):
        return self.driver.find_element(*HomePage.two_way_text)
    
    def get_success_message(self):
        return self.driver.find_element(*HomePage.success_message)
    
    def get_select(self):
        return Select(self.driver.find_element(*HomePage.select))
    
