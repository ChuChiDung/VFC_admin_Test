import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Init(unittest.TestCase):


    def setUp(self):

        options = Options()

        # Bỏ cờ nhận diện Selenium/Bot
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        # Bỏ qua lỗi SSL/Certificate trong mạng nội bộ
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')


        """Khởi tạo Chrome Driver và cấu hình môi trường chạy test"""
        service = Service(executable_path=ChromeDriverManager().install())
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)

        #  Các cấu hình ẩn danh/bỏ qua SSL cũ của bạn
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--ignore-certificate-errors')


        # 3. Tạo driver
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def mo_web(self, url="https://vfcsx.vtv.gov.vn/admin/login"):
        """Hàm dùng chung: Mở trang web và làm mới (refresh)"""
        self.driver.get(url)
        self.driver.refresh()
        time.sleep(2)

    def Dang_nhap(self):
        while True:
            try:
                email_input= self.driver.find_element(By.ID, "adminUsername")
                email_input.clear()
                email_input.send_keys("adminvfc")
                time.sleep(1)

                pass_input= self.driver.find_element(By.ID,"adminPassword")
                pass_input.clear()
                pass_input.send_keys("12345678!")
                time.sleep(1)

                self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
                time.sleep(6)

                #Kiem tra xem phan tu sau khi dang nhap nay da co chua
                self.driver.find_element(By.CSS_SELECTOR, "#mainContent > nav > button.is-active")
                break #thoat khoi vong lap
            except Exception as e:
                print("Chua dang nhap duoc thu lai!!!")
                self.driver.refresh() #thao tac an f5
                time.sleep(2)




    def tearDown(self):
        if self.driver:
            self.driver.quit()



