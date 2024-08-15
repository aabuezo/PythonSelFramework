from selenium.webdriver.common.by import By

from pages.ConfirmPage import ConfirmPage


class CheckoutPage:

    cards = (By.XPATH, "//div[@class='card h-100']")
    card_title = (By.XPATH, "div/h4/a")
    card_button = (By.CSS_SELECTOR, "div button")
    checkout_button = (By.CSS_SELECTOR, "#navbarResponsive ul li a")
    checkout_green_button = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver) -> None:
        self.driver = driver

    def get_cards(self):
        return self.driver.find_elements(*CheckoutPage.cards)
    
    def get_card_title(self, card):
        return card.find_element(*CheckoutPage.card_title).text
    
    def get_card_button(self, card):
        return card.find_element(*CheckoutPage.card_button)

    def get_checkout_button(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)
    
    def get_checkout_green_button(self):
        # integration point with ConfirmPage
        self.driver.find_element(*CheckoutPage.checkout_green_button).click()
        confirm_page = ConfirmPage(driver=self.driver)
        return confirm_page
