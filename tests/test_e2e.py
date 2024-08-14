import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()

        # Finding 'Blackberry' card
        cards = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for card in cards:
            card_text = card.find_element(By.XPATH, "div/h4/a").text
            print(card_text)
        if card_text == "Blackberry":
            card.find_element(By.CSS_SELECTOR, "div button").click()

        # Checkout
        driver.find_element(By.CSS_SELECTOR, "#navbarResponsive ul li a").click()
        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

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
