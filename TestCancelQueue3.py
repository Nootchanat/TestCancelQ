from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

# ระบุพาธของ ChromeDriver 
chrome_driver_path = "C:/webdriver/chromedriver.exe"

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")

# คลิกปุ่ม "เข้าสู่ระบบ"
open_modal_button = driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")

open_modal_button.click()

# ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
id_input = driver.find_element(By.ID, "LoginID_Card")
password_input = driver.find_element(By.ID, "LoginPassword")

# กรอกข้อมูลใน input field
id_input.send_keys("7777777777779")
password_input.send_keys("123456")
time.sleep(5)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย ID ที่กำหนดให้
login_button = driver.find_element(By.ID, "Login")
login_button.click()
# รอสักครู่เพื่อให้หน้าเว็บโหลดและดำเนินการต่อ
time.sleep(5)  # รอ 5 วินาที (หรือตามที่คุณต้องการ)

# คลิกปุ่ม "รายการจองคิว" โดยใช้ XPath
queue_list_button = driver.find_element(By.XPATH, "//h4[text()='รายการจองคิว']")
queue_list_button.click()
time.sleep(5)

# คลิกที่ input ประเภทวันที่ (type="date")
date_input = driver.find_element(By.ID, "TableBookDate")
date_input.click()

# ตั้งค่าวันที่เป็นวันนี้หรือวันที่เรากำหนดเอง (สามารถใช้วิธีอื่น ๆ ในการตั้งค่าวันที่ตามที่คุณต้องการ)
date_input.clear()
date_input.send_keys("10-19-2023")  # เอาเป็นวันเดือนปีนะจ๊ะ ต้องดูด้วยว่าแต่ละเครื่องวันเดือนปีเรียงกันยังไงด้วย
time.sleep(5)

# เลือกแผนกใน dropdown ที่คุณต้องการ (เช่น "ทั่วไป") โดยใช้ ID
department_dropdown = Select(driver.find_element(By.ID, "TableBookselectedDepartment"))
# เลือกแผนกที่คุณต้องการ (เช่น "ทั่วไป")
department_dropdown.select_by_visible_text("ทั่วไป")
time.sleep(5)

# เลือกคิวที่ dropdown โดยใช้ ID (เช่น "คิวที่จอง") ( "1" คิวที่จอง ) ("2" คิวที่กำลังดำเนินการ ) ("4"  ประวัติการจองคิว ) 
queue_status_dropdown = Select(driver.find_element(By.ID, "TableBookselectedStatusId"))
# เลือกคิวที่คุณต้องการ (เช่น "คิวที่จอง") ( "1" คิวที่จอง ) ("2" คิวที่กำลังดำเนินการ ) ("4"  ประวัติการจองคิว ) 
queue_status_dropdown.select_by_value("1")
time.sleep(5)

# # คลิกปุ่ม "Icon ถังขยะสีแดง" โดยใช้ ID
cancel_queue_button = driver.find_element(By.ID, "RemoveQueue")
cancel_queue_button.click()
time.sleep(5)

# # # คลิกปุ่ม "ยืนยัน" โดยใช้ XPath
confirm_cancel_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/button[1]")
confirm_cancel_button.click()
time.sleep(5)