import pytest
from utilities.BaseClass import BaseClass
from pages.HomePage import HomePage
from data.HomePageData import HomePageData


class TestHomePage(BaseClass):
    
    @pytest.mark.usefixtures("data_load")
    def test_formSubmission(self, data_load):
        driver = self.driver
        home_page = HomePage(driver=driver)

        home_page.get_email().send_keys(data_load["email"])
        home_page.get_password().send_keys(data_load["password"])
        home_page.get_checkbox().click()
        home_page.get_name().send_keys(data_load["first"])

        # Static Dropdown
        self.select_dropdown_option_by_text(home_page.get_dropdown_locator(), data_load["gender"])

        home_page.get_submit_button().click()
        home_page.get_option().click()
        home_page.get_two_way_text().clear()
        home_page.get_two_way_text().send_keys(
            data_load["first"] + " " + data_load["last"])

        success = home_page.get_success_message().text
        print(success)
        assert "Success!" in success
        driver.refresh()


    @pytest.fixture(params=HomePageData.test_data)
    def data_load(self, request):
        return request.param
