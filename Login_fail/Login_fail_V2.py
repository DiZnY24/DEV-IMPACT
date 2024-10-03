from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException,TimeoutException


def login_fail(driver):
        result = None
        try:
            # เมื่อกรอกรหัสผ่านไม่ถูกต้องจะต้องขึ้น User not Found
            Key_Passwprd = driver.find_element(By.XPATH, '//div/div/div[2]/div[1]/div/div[2]/div/div/input')
            Key_Passwprd.send_keys('080000000')

            input_password = driver.find_element(By.XPATH, '//div/div/div[2]/div[1]/div/div[2]/div/div/input')
            input_value = input_password.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')

            Click_Otp = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/button')
            Click_Otp.click() 

            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'notistack-snackbar'))
            )
            print('wait : Show User not Found : Pass')

        except ArithmeticError as e:
            print(f'ตรวจสอบไม่สำเร็จ: {e}')
        except NoSuchElementException as b:
            print(f'ไม่พบองค์ประกอบของ Elenemt: {b}')
        except Exception as n:
            print(f'เงื่อนไขไม่ตรงตามที่คาดหวัง: {n}')
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')
        return result

# if __name__ == '__main__':
#     unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Impact/page event management'))




