import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ManageCancelQueueTest(unittest.TestCase):


 def setUp(self):
        # Initialize the Chrome WebDriver
        self.driver = webdriver.Chrome()

 def tearDown(self):
        # Close the browser( ทำการปิดเบราว์เซอร์ )
        self.driver.quit()


 def test_ManageCancelQueue_in_Q_Online(self):
        # Open the web application ( ทำการเปิดเว็บแอพตาม url ที่กำหนด )
        self.driver.get("https://online-web-mauve.vercel.app/")

        # Click the "เข้าสู่ระบบ" button (คลิกปุ่ม "เข้าสู่ระบบ")
        open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        # Find the input fields for ID and password in the modal (ค้นหา input field สำหรับ ID และรหัสผ่านใน Modal)
        id_input = self.driver.find_element(By.ID, "LoginID_Card")
        password_input = self.driver.find_element(By.ID, "LoginPassword")

        # Enter your ID and password (ใส่ ID และรหัสผ่าน)
        id_input.send_keys("7777777777779")
        password_input.send_keys("123456")
        # Wait for the search results to load (รอให้ผลการค้นหาโหลด)
        time.sleep(5)

        # Click the "เข้าสู่ระบบ" button with the specified ID (คลิกปุ่ม "เข้าสู่ระบบ" ด้วย ID)
        login_button = self.driver.find_element(By.ID, "Login")
        login_button.click()
        # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(4)  

         # Click the "จองคิว" button using XPath (คลิกปุ่ม "จองคิว" โดยใช้ XPath)
        booking_button = self.driver.find_element(By.XPATH, "//h4[text()='จองคิว']")
        booking_button.click()
        # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(5)

        # Enter data in the "กรุณาระบุอาการเบื้องต้น" field (กรอกข้อมูลในฟิลด์ "กรุณาระบุอาการเบื้องต้น")
        symptom_input = self.driver.find_element(By.ID, "QueueUsersymptom")
        symptom_input.click()
        symptom_input.send_keys("ไข้สูง")
        # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(3)

        # Select the department from the dropdown (เลือกแผนกจาก dropdown)
        department_dropdown = Select(self.driver.find_element(By.ID, "QueueUserdepartment_id"))
        department_dropdown.select_by_visible_text("ทั่วไป")
        # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(3)

        # Enter the date (กรอกวันที่)
        date_input = self.driver.find_element(By.ID, "QueueUserqueue_date")
        date_input.clear()
        date_input.send_keys("10-19-2023") 
        # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(3)

        # Click the "จองคิว" button with the specified ID (คลิกปุ่ม "จองคิว" ด้วย ID)
        booking_button = self.driver.find_element(By.ID, "BookingQ")
        booking_button.click()

        # Click the "ยืนยัน" button using XPath (คลิกปุ่ม "ยืนยัน" โดยใช้ XPath)
        confirm_button = self.driver.find_element(By.XPATH, "//button[text()='ยืนยัน']")
        confirm_button.click()
        # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(4)

        # Click the date input field (คลิกที่ input ประเภทวันที่)
        date_input = self.driver.find_element(By.ID, "TableBookDate")

        # Set the date to your desired date (ตั้งค่าวันที่ตามที่คุณต้องการ)
        date_input.clear()
        date_input.send_keys("10-19-2023")  
        # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(4)

        # Select the department from the dropdown (เลือกแผนกจาก dropdown)
        department_dropdown = Select(self.driver.find_element(By.ID, "TableBookselectedDepartment"))
        department_dropdown.select_by_visible_text("ทั่วไป")
        # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(4)

        # Select the queue status from the dropdown (เลือกสถานะคิวจาก dropdown)
        queue_status_dropdown = Select(self.driver.find_element(By.ID, "TableBookselectedStatusId"))
        queue_status_dropdown.select_by_value("1")
        # รอ 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(4)

        # Click the "Icon ถังขยะสีแดง" button with the specified ID (คลิกปุ่ม "Icon ถังขยะสีแดง" ด้วย ID)
        cancel_queue_button = self.driver.find_element(By.ID, "RemoveQueue")
        cancel_queue_button.click()
        # Wait for the page to load (รอให้หน้าโหลด) 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(4)

        # Click the "ยืนยัน" button using XPath (คลิกปุ่ม "ยืนยัน" โดยใช้ XPath)
        confirm_cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/button[1]")
        confirm_cancel_button.click()
        # Wait for the page to load (รอให้หน้าโหลด) 5 วินาที (หรือตามที่คุณต้องการ)
        time.sleep(4)

 def test_ManageCancelQueue_in_Q_Online2(self):

        self.driver.get("https://online-web-mauve.vercel.app/")

        # Click the "เข้าสู่ระบบ"
        open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        # Find the input fields for ID and password in the modal
        id_input = self.driver.find_element(By.ID, "LoginID_Card")
        password_input = self.driver.find_element(By.ID, "LoginPassword")

        # Enter your ID and password
        id_input.send_keys("7777777777779")
        password_input.send_keys("123456")
        # Wait for the search results to load
        time.sleep(4)

        # Click the "เข้าสู่ระบบ" button with the specified ID
        login_button = self.driver.find_element(By.ID, "Login")
        login_button.click()
        # Wait for the page to load
        time.sleep(4)

        # Click the "จองคิว" button using XPath
        booking_button = self.driver.find_element(By.XPATH, "//h4[text()='จองคิว']")
        booking_button.click()
        # Wait for the page to load
        time.sleep(4)

        # Enter data in the "กรุณาระบุอาการเบื้องต้น" field
        symptom_input = self.driver.find_element(By.ID, "QueueUsersymptom")
        symptom_input.click()
        symptom_input.send_keys("ไข้สูง")
        # Wait for the page to load
        time.sleep(4)

        # Select the department from the dropdown
        department_dropdown = Select(self.driver.find_element(By.ID, "QueueUserdepartment_id"))
        department_dropdown.select_by_visible_text("ทั่วไป")
        # Wait for the page to load
        time.sleep(4)

        # Enter the date
        date_input = self.driver.find_element(By.ID, "QueueUserqueue_date")
        date_input.clear()
        date_input.send_keys("10-19-2023")
        # Wait for the page to load
        time.sleep(4)

        # Click the "จองคิว" button with the specified ID
        booking_button = self.driver.find_element(By.ID, "BookingQ")
        booking_button.click()
        # Wait for the page to load
        time.sleep(4)

        # Click the "ยืนยัน" button using XPath
        confirm_button = self.driver.find_element(By.XPATH, "//button[text()='ยืนยัน']")
        confirm_button.click()
        # Wait for the page to load
        time.sleep(4)

        # Click the date input field
        date_input = self.driver.find_element(By.ID, "TableBookDate")

        # Set the date to your desired date
        date_input.clear()
        date_input.send_keys("10-19-2023")
        # Wait for the page to load
        time.sleep(4)

        # Select the department from the dropdown
        department_dropdown = Select(self.driver.find_element(By.ID, "TableBookselectedDepartment"))
        department_dropdown.select_by_visible_text("ทั่วไป")
        # Wait for the page to load
        time.sleep(4)

        # Select the queue status from the dropdown
        queue_status_dropdown = Select(self.driver.find_element(By.ID, "TableBookselectedStatusId"))
        queue_status_dropdown.select_by_value("1")
        # Wait for the page to load
        time.sleep(4)

        # Click the "Icon ถังขยะสีแดง" button with the specified ID
        cancel_queue_button = self.driver.find_element(By.ID, "RemoveQueue")
        cancel_queue_button.click()
        # Wait for the page to load
        time.sleep(4)

        # Click the "ยกเลิก" button using XPath
        cancel_cancel_button = self.driver.find_element(By.XPATH, "//button[text()='ยกเลิก']")
        cancel_cancel_button.click()
        # Wait for the page to load
        time.sleep(4)
 
 def test_ManageCancelQueue_in_Q_Online3(self):
        self.driver.get("https://online-web-mauve.vercel.app/")

        # Click the "เข้าสู่ระบบ"
        open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        # Find the input fields for ID and password in the modal
        id_input = self.driver.find_element(By.ID, "LoginID_Card")
        password_input = self.driver.find_element(By.ID, "LoginPassword")

        # Enter your ID and password
        id_input.send_keys("7777777777779")
        password_input.send_keys("123456")
        # Wait for the search results to load
        time.sleep(4)

        # Click the "เข้าสู่ระบบ" button with the specified ID
        login_button = self.driver.find_element(By.ID, "Login")
        login_button.click()
        # Wait for the page to load
        time.sleep(4)

        # Click the "รายการจองคิว" button using XPath
        queue_list_button = self.driver.find_element(By.XPATH, "//h4[text()='รายการจองคิว']")
        queue_list_button.click()
        # Wait for the page to load
        time.sleep(4)

        # Click the date input field
        date_input = self.driver.find_element(By.ID, "TableBookDate")

        # Set the date to your desired date
        date_input.clear()
        date_input.send_keys("10-19-2023")
        # Wait for the page to load
        time.sleep(4)

        # Select the department from the dropdown
        department_dropdown = Select(self.driver.find_element(By.ID, "TableBookselectedDepartment"))
        department_dropdown.select_by_visible_text("ทั่วไป")
        # Wait for the page to load
        time.sleep(4)

        # Select the queue status from the dropdown
        queue_status_dropdown = Select(self.driver.find_element(By.ID, "TableBookselectedStatusId"))
        queue_status_dropdown.select_by_value("1")
        # Wait for the page to load
        time.sleep(4)

        # Click the "Icon ถังขยะสีแดง" button with the specified ID
        cancel_queue_button = self.driver.find_element(By.ID, "RemoveQueue")
        cancel_queue_button.click()
        # Wait for the page to load
        time.sleep(4)

        # Click the "ยืนยัน" button using XPath
        cancel_cancel_button = self.driver.find_element(By.XPATH, "//button[text()='ยืนยัน']")
        cancel_cancel_button.click()
        # Wait for the page to load
        time.sleep(4)

#  def wait_for_element_to_be_clickable(driver, by, value, timeout=10):
#         return WebDriverWait(driver, timeout).until(
#             EC.element_to_be_clickable((by, value))
#         )

 def test_ManageCancelQueue_in_Q_Online4(self):

        self.driver.get("https://online-web-mauve.vercel.app/")

        # Click the "เข้าสู่ระบบ"
        open_modal_button = self.driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
        open_modal_button.click()

        # Find the input fields for ID and password in the modal
        id_input = self.driver.find_element(By.ID, "LoginID_Card")
        password_input = self.driver.find_element(By.ID, "LoginPassword")

        # Enter your ID and password
        id_input.send_keys("7777777777779")
        password_input.send_keys("123456")
        # Wait for the search results to load
        time.sleep(4)

        # Click the "เข้าสู่ระบบ" button with the specified ID
        login_button = self.driver.find_element(By.ID, "Login")
        login_button.click()
        # Wait for the page to load
        time.sleep(4)

        # Click the "รายการจองคิว" button using XPath
        queue_list_button = self.driver.find_element(By.XPATH, "//h4[text()='รายการจองคิว']")
        queue_list_button.click()
        # Wait for the page to load
        time.sleep(4)

        # Click the date input field
        date_input = self.driver.find_element(By.ID, "TableBookDate")

        # Set the date to your desired date
        date_input.clear()
        date_input.send_keys("10-19-2023")
        # Wait for the page to load
        time.sleep(4)

        # Select the department from the dropdown
        department_dropdown = Select(self.driver.find_element(By.ID, "TableBookselectedDepartment"))
        department_dropdown.select_by_visible_text("ทั่วไป")
        # Wait for the page to load
        time.sleep(4)

        # Select the queue status from the dropdown
        queue_status_dropdown = Select(self.driver.find_element(By.ID, "TableBookselectedStatusId"))
        queue_status_dropdown.select_by_value("1")
        # Wait for the page to load
        time.sleep(4)



if __name__ == "__main__":
    unittest.main()


