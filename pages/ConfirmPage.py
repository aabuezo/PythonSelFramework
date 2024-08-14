from selenium.webdriver.common.by import By


class ConfirmPage:

    checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_checkout_button(self):
        return self.driver.find_element(*ConfirmPage.checkout_button)
