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
import sys

def delete_event(driver):
        
        driver.get('https://dev.backoffice.hr-impact.co/events')
        driver.implicitly_wait(10)
        time.sleep(0.5)

        result = None
        try: 

            Url =  driver.current_url == 'https://dev.backoffice.hr-impact.co/events'
            if Url:
                print('URL Show on page : Pass')
            else:
                print('URL is not Show on page! : Fail')

            element = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, 
            '/html/body/div[1]/div/main/div/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[7]/p/div/button[5]'))
            )
            print('รอปุ่ม Delete จนปรากฏขึ้น : Pass')

            Delete = driver.find_element(By.XPATH, 
            '/html/body/div[1]/div/main/div/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[7]/p/div/button[5]')
            assert Delete.is_displayed(), 'Element is not displayed!'
            assert Delete.is_enabled(), 'Element is not enabled!'
            Delete.click()
            if Delete:
                print('กดคลิก Delete สำเร็จ : Pass')
            else:
                print('กดคลิกขอ Delete ไม่สำเร็จ : Fail')


            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div/button[2]'))
            )
            print('รอจนกว่า Confirm ปรากฏขึ้น : Pass')

            Confirm = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/button[2]')
            assert Confirm.is_displayed(), 'Element is not displayed!'
            assert Confirm.is_enabled(), 'Element is not enabled!'
            Confirm.click()

            if Delete:
                print('Click is Delete :',True)
                if Confirm:
                    print('คลิก Confirm สำเร็จ :',True)
                else:
                    print('คลิก Confirm สำเร็จ :',False)
            else:
                print('Click is not Delete :',False)


            wait_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'notistack-snackbar'))
            )
            assert wait_element.is_displayed(), 'Element is not displayed!'
            assert wait_element.is_enabled(), 'Element is not enabled!'
            if wait_element:
                print('Show Delete Event succesfully : Pass')
            elif wait_element:
                print('Show Delete Event succesfully : Fail')
            else:
                print('Cannot Show Delete Event succesfully : Fail')

            # element_locator = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[2]/p/div") 

            # # รอให้ element หายไป
            # WebDriverWait(driver, 15).until(
            #     EC.invisibility_of_element(element_locator)
            # )
            # print("Element หายไปแล้ว!")
                
        except ArithmeticError as e:
            driver.fail(f'ตรวจสอบไม่สำเร็จ' + str(e))
        except NoSuchElementException as s:
            driver.fail(f'ไม่พบองค์ประกอบของ Elenemt')
        except Exception as n:
            driver.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง :' + str(n))
        except TimeoutException:
            driver.fail('การรอองค์ประกอบล้มเหลว')
        return result

if __name__ == '__main__':
    unittest.main()
   

    

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Impact/page event management'))


