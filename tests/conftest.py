import pytest

from selenium import webdriver


# getting browser_name option from CMD
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser_name: chrome or safari"
    )

@pytest.fixture(scope="class")
def setup(request): # request is kind of a default parameter

    # get browser_name from CMD
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/#")
    driver.maximize_window()
    request.cls.driver = driver # to pass the driver to the test class
    yield driver
    driver.close()
