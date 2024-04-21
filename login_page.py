from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    # กำหนดโครงสร้างของหน้าเข้าสู่ระบบ
    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    login_button = (By.CSS_SELECTOR, 'button[type="submit"]')

    # กำหนดวิธีการกรอกชื่อผู้ใช้และรหัสผ่าน
    def enter_credentials(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)

    # กำหนดวิธีการคลิกปุ่มเข้าสู่ระบบ
    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def clear_credentials(self):
        self.driver.find_element(*self.username_input).send_keys(Keys.CONTROL + "a", Keys.DELETE)
        self.driver.find_element(*self.password_input).send_keys(Keys.CONTROL + "a", Keys.DELETE)
