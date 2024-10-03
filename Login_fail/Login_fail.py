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
        login.driver.implicitly_wait(10)
        
    def test_login_fail(login1):
            result = None
            try:
                # เมื่อกรอกรหัสผ่านไม่ถูกต้องจะต้องขึ้น User not Found
                login1.Key_Passwprd = login1.driver.find_element(By.XPATH, '//div/div/div[2]/div[1]/div/div[2]/div/div/input')
                login1.Key_Passwprd.send_keys('080000000')

                input_password = login1.driver.find_element(By.XPATH, '//div/div/div[2]/div[1]/div/div[2]/div/div/input')
                input_value = input_password.get_attribute('value')
                print(f'ค่าที่ป้อนในฟิลด์: {input_value}')

                Click_Otp = login1.driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/button')
                Click_Otp.click() 

                element = WebDriverWait(login1.driver, 10).until(
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
  


    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.quit()   

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Impact/page event management'))




