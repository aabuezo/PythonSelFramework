from selenium.webdriver.common.by import By


class CheckoutPage:

    cards = (By.XPATH, "//div[@class='card h-100']")
    card_title = (By.XPATH, "div/h4/a")
    card_button = (By.CSS_SELECTOR, "div button")
    checkout_button = (By.CSS_SELECTOR, "#navbarResponsive ul li a")

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