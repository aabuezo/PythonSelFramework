import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request): # request is kind of a default parameter
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get("https://rahulshettyacademy.com/angularpractice/#")
    # driver.maximize_window()
    request.cls.driver = driver # to pass the driver to the test class
    yield driver
    driver.close()
