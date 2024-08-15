from selenium.webdriver.common.by import By

from pages.CheckoutPage import CheckoutPage


class HomePage():

    shop_button = (By.XPATH, "//a[contains(@href,'shop')]")

    def __init__(self, driver) -> None:
        self.driver = driver

    def shop(self):
        # integration point with CheckoutPage
        self.driver.find_element(*HomePage.shop_button).click()
        checkout_page = CheckoutPage(driver=self.driver)
        return checkout_page
