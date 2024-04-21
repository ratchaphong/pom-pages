import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from login_page import LoginPage
from home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://st.rvpdplus.com/e-agent/login")
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    def test_successful_login(self):
        self.login_page.clear_credentials()
        self.login_page.enter_credentials("agent_001@mail.com", "Tqd12345")

        self.login_page.click_login_button()
        print(self.driver.current_url)
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://st.rvpdplus.com/e-agent/homepage"))

        code_message = self.home_page.get_code_message()
        print(code_message)
        self.assertIn("UW-EA-001-0001", code_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
