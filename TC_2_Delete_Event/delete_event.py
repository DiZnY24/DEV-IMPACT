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


class WebTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(login):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        login.driver = webdriver.Chrome(options=options)
        login.driver.get('https://backoffice-staging.hr-impact.co/login')
        login.driver.set_window_size(1600, 1000)
        login.driver.implicitly_wait(15)

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()   

    def test_page_title(self):
        driver = self.driver
        self.assertEqual(driver.title, 'Admin Events Management')  # ตรวจสอบว่า title ของหน้าว็บถูกต้อง
        
    def test_Login_Impact(self):
        result = None
        time.sleep(1)
        driver = self.driver

        try:
        # ป้อนรหัสผ่าน
            Check_messages = driver.find_element(By.XPATH, '//div/div/div[2]/div[1]/div/div[1]/p')
            expected_text = 'เบอร์โทรศัพท์ / รหัสพนักงาน'
            assert Check_messages.text == expected_text, f"ข้อความไม่ตรงกัน: คาดว่า '{expected_text}' แต่ได้ '{Check_messages.text}'"
            time.sleep(0.1)
        
            Key_Passwprd = driver.find_element(By.XPATH, '//div/div/div[2]/div[1]/div/div[2]/div/div/input')
            Key_Passwprd.send_keys('0800000000')

            input_password = driver.find_element(By.XPATH, '//div/div/div[2]/div[1]/div/div[2]/div/div/input')
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

            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div/div/div[2]/button')) # คลิกขอ เข้าสู่ระบบ
            )
            assert element.is_displayed(), 'Element is not displayed!'
            assert element.is_enabled(), 'Element is not enabled!'
            element.click()
            if element:
                print('กดคลิกเข้าสู่ระบบสำเร็จ : Pass')
            else:
                print('กดคลิกขอเข้าสูาระบบไม่สำเร็จ : Fail')


        # จับข้อผิดพลาดนี้เมื่อไม่พบองค์ประกอบ และเรียกใช้ self.fail() เพื่อบอกว่าการทดสอบล้มเหลว
        except NoSuchElementException:
            self.fail('Element not Found')
        except AssertionError as e:
            self.fail(str(e))
        except Exception as o:
            self.fail(f"An unexpected error occurred: {o}")
        except TimeoutException:
            print('การรอองค์ประกอบล้มเหลว')
        
        try:
        # ทดสอบการคลิก Element
            result_elemet = self.driver.find_element(By.XPATH, '//div[1]/div/main/div/div/div[1]/button')    
            self.assertIsNotNone(result_elemet)
        except NoSuchElementException as e:
            self.fail('Element not Found')
            self.driver.implicitly_wait(10)
        return result
    
    def test_delete(self):
        
        self.driver.get('https://backoffice-staging.hr-impact.co/events')
        self.driver.implicitly_wait(10)
        time.sleep(0.5)

        result = None
        try: 

            Url =  self.driver.current_url == 'https://backoffice-staging.hr-impact.co/events'
            if Url:
                print('URL Show on page : Pass')
            else:
                print('URL is not Show on page! : Fail')

            element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, 
            '/html/body/div/div/main/div/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[6]/p/div/button[5]'))
            )
            print('รอปุ่ม Delete จนปรากฏขึ้น : Pass')

            Delete = self.driver.find_element(By.XPATH, 
            '/html/body/div/div/main/div/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[6]/p/div/button[5]')
            assert Delete.is_displayed(), 'Element is not displayed!'
            assert Delete.is_enabled(), 'Element is not enabled!'
            Delete.click()
            if Delete:
                print('กดคลิก Delete สำเร็จ : Pass')
            else:
                print('กดคลิกขอ Delete ไม่สำเร็จ : Fail')


            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/button[2]'))
            )
            print('รอจนกว่า Confirm ปรากฏขึ้น : Pass')

            Confirm = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/button[2]')
            assert Confirm.is_displayed(), 'Element is not displayed!'
            assert Confirm.is_enabled(), 'Element is not enabled!'
            Confirm.click()

            if Delete:
                print('Click is Delete : Pass')
                if Confirm:
                    print('คลิก Confirm สำเร็จ : Pass')
                else:
                    print('คลิก Confirm สำเร็จ : Fail')
            else:
                print('Click is not Delete : Fail')

            wait_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'notistack-snackbar'))
            )
            assert wait_element.is_displayed(), 'Element is not displayed!'
            assert wait_element.is_enabled(), 'Element is not enabled!'
            print('Show Delete Event succesfully : Pass')

        except ArithmeticError as e:
            self.fail(f'ตรวจสอบไม่สำเร็จ' + str(e))
        except NoSuchElementException as s:
            self.fail(f'ไม่พบองค์ประกอบของ Elenemt')
        except Exception as n:
            self.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง :' + str(n))
        except TimeoutException:
            self.fail('การรอองค์ประกอบล้มเหลว')
        return result

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Impact/page event management'))


