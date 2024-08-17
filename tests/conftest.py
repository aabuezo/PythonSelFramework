import pytest

from selenium import webdriver


driver = None


# getting browser_name option from CMD
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser_name: chrome or safari"
    )


@pytest.fixture(scope="class")
def setup(request): # request is kind of a default parameter
    global driver
    # get browser_name from CMD
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "safari":
        # headless not available for safari
        driver = webdriver.Safari()
    
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/#")
    driver.maximize_window()

    request.cls.driver = driver # to pass the driver to the test class
    yield driver
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;"'\
                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extras.append(pytest_html.extras.html(html))
        report.extras = extras


def _capture_screenshot(name):
    global driver
    driver.get_screenshot_as_file(name)
