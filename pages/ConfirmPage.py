from selenium.webdriver.common.by import By


class ConfirmPage:

    country = (By.ID, "country")
    india = (By.LINK_TEXT, "India")
    checkbox = (By.ID, "checkbox2")
    label_for_checkbox = (By.XPATH, "//label[@for='checkbox2']")
    purchase_button = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    success_message = (By.XPATH, "//div/strong")

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_country_input(self):
        return self.driver.find_element(*ConfirmPage.country)
    
    def get_india_option(self):
        return self.driver.find_element(*ConfirmPage.india)
    
    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)
    
    def get_label_for_checkbox(self):
        return self.driver.find_element(*ConfirmPage.label_for_checkbox)

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def get_success_message(self):
        return self.driver.find_element(*ConfirmPage.success_message).text
