import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class Menu:
    def __init__(self, driver):
        self.driver = driver  # Nhận driver từ file test truyền sang

    def Trang_Chu (self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".sidebar-link.active"))
        )
        element.click()
    def Dang_Ki_Kich_Ban (self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title*='Đăng ký kịch bản']"))
        )

        # 2. Cuộn màn hình tới vị trí phần tử đó để chắc chắn nó nằm trong vùng nhìn thấy
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # 3. Dùng JavaScript để click trực tiếp, bất chấp việc nó có bị che khuất hay không
        self.driver.execute_script("arguments[0].click();", element)
    def Kich_Ban (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Kịch bản'] span"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def Thanh_Lap_Doan_Phim (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Thành lập đoàn phim'] span"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)


    def Doan_Phim (self):
        # Đợi cho đến khi nút Đoạn Phim xuất hiện trên DOM
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Đoàn phim']")) # Hoặc CSS Selector thực tế của nút đó
        )

        # Di chuột vào (nếu cần hover) hoặc scroll tới element trước khi click
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        # Tiến hành click an toàn
        element.click()

    def Muon_Thiet_Bi_Tien_Ky (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Mượn thiết bị tiền kỳ'] span"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def Muon_Va_Tra_Thiet_Bi (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Mượn và trả thiết bị'] span"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def Hau_Ky (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Hậu kỳ']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def Kho_Thiet_Bi (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Kho thiết bị'] span"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def Them_Thiet_Bi (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Thêm thiết bị'] span"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def Xoa_Thiet_Bi (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Xóa thiết bị'] span"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def Nhan_Su (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Nhân sự'] span"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def Thong_Ke (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Thống kê'] span"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def Loai_Thiet_Bi (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Quản lý loại thiết bị'] span"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def Chuc_Danh (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='Chức danh'] span"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def API_VTV (self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[title='API VTV']"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)