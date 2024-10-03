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


def login_impact(driver):
        time.sleep(1)
        try:
        # ป้อนรหัสผ่าน
            wait_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="MuiBox-root mui-style-14b2eiy"]/div/div/input'))
            )
            print('รอจนพร้อมพิมพ์ : Pass')

            Check_messages = driver.find_element(By.XPATH, 
            '//div/div/div[2]/div[1]/div/div[1]/p')
            expected_text = 'เบอร์โทรศัพท์ / รหัสพนักงาน'
            assert Check_messages.text == expected_text, f"ข้อความไม่ตรงกัน: คาดว่า '{expected_text}' แต่ได้ '{Check_messages.text}'"
            time.sleep(0.1)
        
            Key_Passwprd = driver.find_element(By.XPATH, 
            '//div/div/div[2]/div[1]/div/div[2]/div/div/input')
            Key_Passwprd.send_keys('0800000000')

            input_password = driver.find_element(By.XPATH, 
            '//div/div/div[2]/div[1]/div/div[2]/div/div/input')
            input_value = input_password.get_attribute('value')
            print(f'ค่าที่ป้อนในฟิลด์: {input_value}')

            textbox_element = driver.find_element(By.XPATH, "//div/div/div[2]/div[1]/div/div[2]/div/div/input")  
            textbox_value = textbox_element.get_attribute("value")
            text_to_check = "0800000000"
            assert text_to_check in textbox_value, f"ไม่พบ '{text_to_check}' ในกล่องข้อความ"
        
            Click_Otp = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/button')
            assert Click_Otp.is_displayed(), 'Element is not displayed!'
            assert Click_Otp.is_enabled(), 'Element is not enabled!'
            Click_Otp.click() 
            if Click_Otp:
                print('กดคลิกขอ Otp สำเร็จ : Pass')
            else:
                print('กดคลิกขอ Otp ไม่สำเร็จ : Fail')

            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, 
            '//div/div/div[2]/button')) # คลิกขอ เข้าสู่ระบบ
            )
            assert element.is_displayed(), 'Element is not displayed!'
            assert element.is_enabled(), 'Element is not enabled!'
            element.click()
            if element:
                print('กดคลิกเข้าสู่ระบบสำเร็จ : Pass')
            else:
                print('กดคลิกขอเข้าสูาระบบไม่สำเร็จ : Fail')

            wait_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, 
            '/html/body/div/div/main/div/div/div[1]/button')) 
            )
            print('Show Page Impact : Pass')

        except NoSuchElementException:
            driver.fail('Element not Found')
        except AssertionError as e:
            driver.fail(str(e))
        except Exception as o:
            driver.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')


if __name__ == '__main__':
    unittest.main()