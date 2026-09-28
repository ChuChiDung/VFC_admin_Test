


import time
from idlelib.mainmenu import menudefs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Initision import Init
from Menu_VFC import Menu

class Dang_Nhap(Init):
    def test_05_TC5(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Doan_Phim()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"#mainContent > section.page-heading > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_02_TC2(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Dang_Ki_Kich_Ban()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"#mainContent > section > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_03_TC3(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Kich_Ban()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"#mainContent > section.page-heading > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_04_TC4(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Thanh_Lap_Doan_Phim()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"#mainContent > section > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_06_TC6(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Muon_Thiet_Bi_Tien_Ky()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"#mainContent > section.page-heading > div:nth-child(1)")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_07_TC7(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Muon_Va_Tra_Thiet_Bi()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"#mainContent > section.page-heading.warehouse-loans-heading > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_08_TC8(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Hau_Ky()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"#mainContent > section.page-heading.post-production-heading > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_01_TC1(self):
        self.mo_web()
        self.Dang_nhap()
        time.sleep(5)

        Hien_Thi= self.driver.find_element(By.CSS_SELECTOR,"body > div > header > div.d-flex.align-items-center.gap-3 > div")
        print("Hiển thị ra: " + Hien_Thi.text)

    def test_09_TC9(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Kho_Thiet_Bi()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"body > div > header > div.d-flex.align-items-center.gap-3 > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_10_TC10(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Them_Thiet_Bi()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"body > div > header > div.d-flex.align-items-center.gap-3 > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_11_TC11(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Xoa_Thiet_Bi()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"body > div > header > div.d-flex.align-items-center.gap-3 > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_12_TC12(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Nhan_Su()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"body > div > header > div.d-flex.align-items-center.gap-3 > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_13_TC13(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Thong_Ke()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"body > div > header > div.d-flex.align-items-center.gap-3 > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_14_TC14(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Loai_Thiet_Bi()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"body > div > header > div.d-flex.align-items-center.gap-3 > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_15_TC15(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Chuc_Danh()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"body > div > header > div.d-flex.align-items-center.gap-3 > div")
        print("Hiển thị ra: " + Hien_thi.text)

    def test_16_TC16(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.API_VTV()
        time.sleep(5)

        Hien_thi= self.driver.find_element(By.CSS_SELECTOR,"body > div > header > div.d-flex.align-items-center.gap-3 > div")
        print("Hiển thị ra: " + Hien_thi.text)


    def test_17_TC17(self):
        self.mo_web()
        self.Dang_nhap()

        menu = Menu(self.driver)
        menu.Doan_Phim()

    # Click vào nút Chi tiết đầu tiên và chờ nó clickable
        chi_tiet_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]//a[contains(@class, 'btn-outline-primary')]"))
    )
        chi_tiet_btn.click()

    # Chờ trang chi tiết load xong và hiển thị tiêu đề phim
        hien_thi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#projectProfileTitle"))
    )

        print("Hiển thị ra: " + hien_thi.text)

        time.sleep(4)







