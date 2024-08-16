from utilities.BaseClass import BaseClass
from pages.HomePage import HomePage


class TestHomePage(BaseClass):
    
    def test_formSubmission(self):
        driver = self.driver
        home_page = HomePage(driver=driver)
        home_page.get_email().send_keys("johndoe@mail.com")
        home_page.get_password().send_keys("test123456")
        home_page.get_checkbox().click()
        home_page.get_name().send_keys("John")

        # Static Dropdown
        self.select_dropdown_option_by_text(home_page.get_dropdown(), "Female")

        home_page.get_submit_button().click()
        home_page.get_option().click()
        home_page.get_two_way_text().clear()
        home_page.get_two_way_text().send_keys("John Doe")

        success = home_page.get_success_message().text
        print(success)
        assert "Success!" in success

