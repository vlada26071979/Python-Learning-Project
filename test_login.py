from LoginPage import LoginPage
import time


class TestLogin:
    base_url = "https://admin-demo.nopcommerce.com"
    username = "admin@yourstore.com"
    password = "admin1"
    def test_home_page_title(self, setup):

        self.driver = setup

        self.driver.get(self.base_url)
        time.sleep(5)

        actual_page_title = self.driver.title
        expected_page_title = "Your store. Login"

        if actual_page_title == expected_page_title:
            assert True
            print(f"Navigated to {self.base_url}")
        else:
            assert False
        self.driver.close()

    def test_happy_path(self, setup):
        self.driver = setup

        self.driver.get(self.base_url)
        time.sleep(5)

        my_login_page = LoginPage(self.driver)
        my_login_page.enter_username(self.username)
        my_login_page.enter_password(self.password)
        my_login_page.click_on_login_button()

        actual_url = self.driver.current_url
        expected_url = "https://admin-demo.nopcommerce.com/admin/"

        if actual_url == expected_url:

            assert True

        else:
            self.driver.save_screenshot("loginfailed.png")
            assert False,"Unsuccessfull login!!"

        my_login_page.click_on_logout()









