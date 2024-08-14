import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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
        home_page.shop().click()

        # Finding 'Blackberry' card
        checkout_page = CheckoutPage(driver=driver)
        cards = checkout_page.get_cards()
        for card in cards:
            card_text = checkout_page.get_card_title(card)
            if card_text == "Blackberry":
                print(card_text)
                checkout_page.get_card_button(card).click()        
        checkout_page.get_checkout_button().click()

        confirm_page = ConfirmPage(driver=driver)
        confirm_page.get_checkout_button().click()
        

        # Choose delivery location
        driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//ul/li/a")))
        # countries = driver.find_elements(By.XPATH, "//ul/li/a")
        # for country in countries:
        #   if country.text == "India":
        #     country.click()
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        driver.find_element(By.LINK_TEXT, "India").click()

        # Click the checkbox
        chkbox = driver.find_element(By.ID, "checkbox2")
        driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        assert chkbox.is_selected

        # Click Purchase button
        driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()

        # Check for Success message
        success = driver.find_element(By.XPATH, "//div/strong").text
        assert success == "Success!"
