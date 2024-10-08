import pytest
import logging as log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verify_link_presence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_dropdown_option_by_text(self, locator, text):
        return Select(self.driver.find_element(*locator)).select_by_visible_text(text)

    def getLogger(self, filename):
            logger = log.getLogger(filename)
            fileHandler = log.FileHandler("my_logs.log")
            formatter = log.Formatter('%(asctime)s: %(levelname)s: [%(filename)s:%(lineno)s] %(message)s')
            fileHandler.setFormatter(formatter)
            logger.handlers = []
            logger.addHandler(fileHandler)
            logger.setLevel(log.DEBUG)

            return logger
