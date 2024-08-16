from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utilities.BaseClass import BaseClass
from pages.HomePage import HomePage
from pages.CheckoutPage import CheckoutPage
from pages.ConfirmPage import ConfirmPage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger(__name__)
        log.info("===== Purchasing E2E test =====")

        driver = self.driver
        home_page = HomePage(driver=driver)

        log.info("Moving to shopping page")
        checkout_page = home_page.shop()

        # Finding 'Blackberry' card
        
        log.info("Getting all cards")
        cards = checkout_page.get_cards()
        for card in cards:
            card_text = checkout_page.get_card_title(card)
            if card_text == "Blackberry":
                log.info(f"'{card_text}' found")
                log.info(f"Adding '{card_text}' to cart")
                checkout_page.get_card_button(card).click() 
        log.info("Checking out")
        checkout_page.get_checkout_button().click()
        confirm_page = checkout_page.get_checkout_green_button()

        # Choose delivery location
        
        country = "India"
        log.info(f"Finding '{country}' in Checkout page.")
        confirm_page.get_country_input().send_keys("ind")
        self.verify_link_presence(country)
        confirm_page.get_india_option().click()

        # Click the checkbox
        log.info("Selecting checkbox")
        chkbox = confirm_page.get_checkbox()
        confirm_page.get_label_for_checkbox().click()
        assert chkbox.is_selected

        # Click Purchase button
        log.info("Confirming by clicking Purchase button")
        confirm_page.get_purchase_button().click()

        # Check for Success message
        log.info("Checking for 'Success!' message")
        success = confirm_page.get_success_message()
        assert success == "Success!"
