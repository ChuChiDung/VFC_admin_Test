


import time
from idlelib.mainmenu import menudefs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

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

    def test_18_TC18(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Nhan_Su()
        time.sleep(2)
        menu.NSu_Them_Nhan_Su()

        # 1.Chờ cho ô nhập họ và tên hiển thị rồi nhập giá trị
        ho_ten_NS = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelName"))
        )
        ho_ten_NS.clear()
        ho_ten_NS.send_keys("Nguyễn Văn Luân")

        #2. Chờ thẻ select hiển thị rồi khởi tạo đối tượng Select
        select_Chuc_Danh = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelPosition"))
        )
        dropdown = Select(select_Chuc_Danh)

        # Chọn chức danh theo tên hiển thị (ví dụ: "Kỹ sư")[cite: 8]
        dropdown.select_by_visible_text("Kỹ sư")

        #3. Chờ cho ô nhập số điện thoại hiển thị rồi nhập giá trị
        SDT_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelPhone"))
        )
        SDT_input.clear()
        SDT_input.send_keys("0987654321")

        #4. Chờ cho ô nhập Email hiển thị rồi nhập giá trị
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelEmail"))
        )
        email_input.clear()
        email_input.send_keys("nguyenvanluan@gmail.com")

        #5. Chờ cho dropdown loại nhân viên hiển thị và chọn giá trị
        personnel_type_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelType"))
        )
        dropdown_type = Select(personnel_type_element)

        # Chọn theo text hiển thị (ví dụ: "Cộng tác viên (CTV)" hoặc "VFC")
        dropdown_type.select_by_visible_text("Cộng tác viên (CTV)")

        #6. Chờ cho nút Lưu nhân sự hiển thị và có thể click được, sau đó tiến hành click
        save_NS_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer button[type='submit']"))
        )
        save_NS_btn.click()
        time.sleep(2)

        # Kiểm tra xem toast có tồn tại hay không trước khi lấy nội dung
        toast_text = self.driver.execute_script("""
            var toast = document.querySelector('#appToastContainer .app-toast-body');
            return toast ? toast.innerText.trim() : null;
        """)

        if toast_text:
            print("Nội dung thông báo nhận được là: " + toast_text)
            assert "Email này đã được sử dụng cho nhân sự khác" in toast_text
        else:
            print("Không có thông báo lỗi nào xuất hiện (Thêm nhân sự có thể đã thành công).")



        # Chờ cho ô tìm kiếm hiển thị rồi nhập tên nhân sự cần tìm
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelSearch"))
        )
        search_input.clear()
        search_input.send_keys("Nguyễn Văn Luân")
        search_input.send_keys(Keys.RETURN)


        # Chờ cho thẻ chứa tên của dòng đầu tiên hiển thị, sau đó lấy text
        Hien_thi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnel-directory > div.card-body.p-0 > div.table-responsive.personnel-table-responsive > table > tbody > tr > td"))
        )

        print("Tên nhân sự tôi vừa tạo ra đã có chưa: " + Hien_thi.text)

        time.sleep(5)

    def test_19_TC19(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Nhan_Su()
        time.sleep(2)
        menu.NSu_Them_Nhan_Su()

        # 1.Chờ cho ô nhập họ và tên hiển thị rồi nhập giá trị
        ho_ten_NS = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelName"))
        )
        ho_ten_NS.clear()
        ho_ten_NS.send_keys("Nguyễn Văn Luân")

        #2. Chờ thẻ select hiển thị rồi khởi tạo đối tượng Select
        select_Chuc_Danh = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelPosition"))
        )
        dropdown = Select(select_Chuc_Danh)

        # Chọn chức danh theo tên hiển thị (ví dụ: "Kỹ sư")[cite: 8]
        dropdown.select_by_visible_text("Kỹ sư")

        #3. Chờ cho ô nhập số điện thoại hiển thị rồi nhập giá trị
        SDT_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelPhone"))
        )
        SDT_input.clear()
        SDT_input.send_keys("0987654321")

        #4. Chờ cho ô nhập Email hiển thị rồi nhập giá trị
        # Tạo email ngẫu nhiên/động dựa trên thời gian hiện tại
        timestamp = int(time.time())
        dynamic_email = f"nguyenvanluan_{timestamp}@example.com"

        # Điền email động vào ô nhập
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelEmail"))
        )
        email_input.clear()
        email_input.send_keys(dynamic_email)

        #5. Chờ cho dropdown loại nhân viên hiển thị và chọn giá trị
        personnel_type_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelType"))
        )
        dropdown_type = Select(personnel_type_element)

        # Chọn theo text hiển thị (ví dụ: "Cộng tác viên (CTV)" hoặc "VFC")
        dropdown_type.select_by_visible_text("Cộng tác viên (CTV)")

        #6. Chờ cho nút Lưu nhân sự hiển thị và có thể click được, sau đó tiến hành click
        save_NS_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer button[type='submit']"))
        )
        save_NS_btn.click()
        time.sleep(2)

        # Kiểm tra xem toast có tồn tại hay không trước khi lấy nội dung
        toast_text = self.driver.execute_script("""
            var toast = document.querySelector('#appToastContainer .app-toast-body');
            return toast ? toast.innerText.trim() : null;
        """)

        if toast_text:
            print("Nội dung thông báo nhận được là: " + toast_text)

        else:
            print("Không có thông báo lỗi nào xuất hiện (Thêm nhân sự có thể đã thành công).")



        # Chờ cho ô tìm kiếm hiển thị rồi nhập tên nhân sự cần tìm
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelSearch"))
        )
        search_input.clear()
        search_input.send_keys("Nguyễn Văn Luân")
        search_input.send_keys(Keys.RETURN)


        # Chờ cho thẻ chứa tên của dòng đầu tiên hiển thị, sau đó lấy text
        Hien_thi = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "tbody tr:nth-child(1) td.personnel-name-cell strong"))
        )

        print("Tên nhân sự tôi vừa tạo ra đã có chưa: " + Hien_thi.text)

        time.sleep(5)

    def test_20_TC20(self):
        self.mo_web()
        self.Dang_nhap()

        menu=Menu(self.driver)
        menu.Nhan_Su()
        time.sleep(2)

        # Chờ cho ô tìm kiếm hiển thị rồi nhập tên nhân sự cần tìm
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#personnelSearch"))
        )
        search_input.clear()
        search_input.send_keys("Nguyễn Văn Luân")
        search_input.send_keys(Keys.RETURN)

        #1.CLick vào nút xóa dòng đầu
        delete_NS_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "tbody tr:nth-child(1) form[action*='/delete'] button[type='submit']"))
        )
        delete_NS_btn.click()

        #2.Chờ hộp thoại xác nhận bấm OK
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        print("Nội dung popup xác nhận: " + alert.text)
        alert.accept()

        time.sleep(1)

        #3.Lấy ND thông báo Toast phản hồi hệ thống bằng JS
        toast_text = self.driver.execute_script("""
            var toast = document.querySelector('#appToastContainer .app-toast-body');
            return toast ? toast.innerText.trim() : null;
        """)

        if toast_text:
            print("Nội dung thông báo nhận được là: " + toast_text)

        else:
            print("Không có thông báo Toast phản hồi từ hệ thống nào cả")

        time.sleep(4)










