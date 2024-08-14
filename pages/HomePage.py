from selenium.webdriver.common.by import By


class HomePage():

    shop_button = (By.XPATH, "//a[contains(@href,'shop')]")

    def __init__(self, driver) -> None:
        self.driver = driver

    def shop(self):
        return self.driver.find_element(*HomePage.shop_button)
