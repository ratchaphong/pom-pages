from selenium.webdriver.common.by import By
from base_page import BasePage

class HomePage(BasePage):
    # กำหนดโครงสร้างของหน้าหลัก
    code_message = (By.XPATH, '//span[contains(text(), "UW-EA-001-0001")]')
    
    # กำหนดวิธีการตรวจสอบข้อความต้อนรับ
    def get_code_message(self):
        return self.driver.find_element(*self.code_message).text
