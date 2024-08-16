from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utilities.BaseClass import BaseClass
from pages.HomePage import HomePage
from pages.CheckoutPage import CheckoutPage
from pages.ConfirmPage import ConfirmPage


class TestOne(BaseClass):

    def test_e2e(self):
        driver = self.driver
        home_page = HomePage(driver=driver)
        checkout_page = home_page.shop()

        # Finding 'Blackberry' card
        
        cards = checkout_page.get_cards()
        for card in cards:
            card_text = checkout_page.get_card_title(card)
            if card_text == "Blackberry":
                print(card_text)
                checkout_page.get_card_button(card).click()        
        checkout_page.get_checkout_button().click()
        confirm_page = checkout_page.get_checkout_green_button()

        # Choose delivery location
        
        confirm_page.get_country_input().send_keys("ind")
        self.verify_link_presence("india")
        confirm_page.get_india_option().click()

        # Click the checkbox
        chkbox = confirm_page.get_checkbox()
        confirm_page.get_label_for_checkbox().click()
        assert chkbox.is_selected

        # Click Purchase button
        confirm_page.get_purchase_button().click()

        # Check for Success message
        success = confirm_page.get_success_message()
        assert success == "Success!"
