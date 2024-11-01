from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import unittest.main
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import pyautogui
import sys
from selenium.webdriver.common.action_chains import ActionChains


def add_event(driver):

    result = None
    try: 

        driver.get('https://dev.backoffice.hr-impact.co/events')
        driver.implicitly_wait(10)
        time.sleep(0.3)

        Url =  driver.current_url == 'https://dev.backoffice.hr-impact.co/events'
        if Url:
            print('URL Show on page : Pass')
        else:
            print('URL is not Show on page! : Fail')

        element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="MuiContainer-root MuiContainer-maxWidthLg mui-style-5gxgaq"]/div[1]/div[1]//button'))
        )
        print('รอปุ่ม Add Event จนปรากฏขึ้น : Pass')

        Add_Event = driver.find_element(By.XPATH, '//div[@class="MuiContainer-root MuiContainer-maxWidthLg mui-style-5gxgaq"]/div[1]/div[1]//button')
        assert Add_Event.is_displayed(), 'Element is not displayed!'
        assert Add_Event.is_enabled(), 'Element is not enabled!'
        Add_Event.click()
        if Add_Event:
            print('กดคลิก Add Event สำเร็จ : Pass')
        else:
            print('กดคลิกขอ Add Event ไม่สำเร็จ : Fail')

        element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.NAME, 'name'))
        )
        print('รอจนสามารถกรอกข้อมความได้ : Pass')

        pyautogui.click(x=743, y=445)
        time.sleep(0.5)
        pyautogui.click(x=484, y=528)
        pyautogui.click(x=629, y=411)
        time.sleep(0.5)
        pyautogui.click(x=839 , y=413)
        pyautogui.press('enter')

        # time.sleep(3)
        # current_position = pyautogui.position()
        # print(f"The current mouse position is: {current_position}")
        
    except ArithmeticError as e:
        driver.fail(f'ตรวจสอบไม่สำเร็จ' + str(e))
    except NoSuchElementException as s:
        driver.fail(f'ไม่พบองค์ประกอบของ Elenemt')
    except Exception as n:
        driver.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง :' + str(n))
    except TimeoutException:
        driver.fail('การรอองค์ประกอบล้มเหลว')

        time.sleep(0.3)

    try:        

        Key_Name_Event = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[2]/div/div[2]/div/div/input')
        Key_Name_Event.send_keys('Test')

        input_key = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[2]/div/div[2]/div/div/input')
        input_value = input_key.get_attribute('value')
        print(f'ค่าที่ป้อนในฟิลด์: {input_value}')        

        wait_element = WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[3]/div/div/div/div/div/div[1]/div/div/div'))
        )
        print('key_Type_for_something : Pass')

        click_type = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[3]/div/div/div/div/div/div[1]/div/div/div'))
        )
        click_type.click()

        key_Type_for_something = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[3]/div/div/div/div/div/div[1]/div/div/div'))
        )
        key_Type_for_something.send_keys('ระบุทรัพยากรเป้าหมายของคำขอเมื่อรวมกับข้อมูลที่ให้ไว้ในHostส่วนหัว นี่คือเส้นทางสัมบูรณ์ (เช่น/path/to/file.html) ในคำขอไปยังเซิร์ฟเวอร์ต้นทาง และ URL สัมบูรณ์ในคำขอไปยังพร็อกซี')

        # key_Type_for_something = driver.find_element(By.XPATH, '')
        # key_Type_for_something.send_keys(
        # 'ระบุทรัพยากรเป้าหมายของคำขอเมื่อรวมกับข้อมูลที่ให้ไว้ในHostส่วนหัว นี่คือเส้นทางสัมบูรณ์ (เช่น/path/to/file.html) ในคำขอไปยังเซิร์ฟเวอร์ต้นทาง และ URL สัมบูรณ์ในคำขอไปยังพร็อกซี')

        element_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[1]/div/div[2]/div/div/input")
        driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        time.sleep(1)

        key_location = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[1]/div/div[2]/div/div/input')
        key_location.send_keys('Impact')

        input_key = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[1]/div/div[2]/div/div/input')
        input_value = input_key.get_attribute('value')
        print(f'ค่าที่ป้อนในฟิลด์: {input_value}') 

        key_Specify_quantity = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[2]/div/div[2]/div/div/input')
        key_Specify_quantity.send_keys('90')

        input_key = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[2]/div/div[2]/div/div/input')
        input_value = input_key.get_attribute('value')
        print(f'ค่าที่ป้อนในฟิลด์: {input_value}') 

    except ArithmeticError as e:
        driver.fail(f'ตรวจสอบไม่สำเร็จ' + str(e))
    except NoSuchElementException as s:
        driver.fail(f'ไม่พบองค์ประกอบของ Elenemt')
    except Exception as n:
        driver.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง :' + str(n))
    except TimeoutException:
        driver.fail('การรอองค์ประกอบล้มเหลว')

    
    try:
        start_date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[5]/div[1]/div/div/div/div/button')
        assert start_date.is_displayed(), 'Element is not displayed!'
        assert start_date.is_enabled(), 'Element is not enabled!'
        start_date.click()

        date_28 = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[4]/button[7]')
        assert start_date.is_displayed(), 'Element is not displayed!'
        assert start_date.is_enabled(), 'Element is not enabled!'
        date_28.click()  

        # autogui เลือกเวลา วันที่เริ่ม
        pyautogui.moveTo(x=637, y=335) 
        pyautogui.scroll(-15)
        time.sleep(0.5)
        pyautogui.click(x=637, y=335)
        pyautogui.click(x=701, y=338)

        if start_date:
            print('คลิกเลือกวันที่เริ่มต้นสำเร็จ : Pass')
            if date_28:
                print('คลิกเลือกวันที่ 28 สำเร็จ : Pass')
            else:
                print('คลิกเลือกวันที่ 28 ไม่สำเร็จ : Fail')
        else:
            print('คลิกเลือกวันที่เริ่มต้นไม่สำเร็จ : Fail')

        time.sleep(0.5)
        
        End_date = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[5]/div[2]/div/div/div/div/button')
        End_date.click()

        date_29 = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[5]/button[1]')
        assert start_date.is_displayed(), 'Element is not displayed!'
        assert start_date.is_enabled(), 'Element is not enabled!'
        date_29.click()  

        # autogui เลือกเวลา วันที่สิ้นสุด
        pyautogui.moveTo(x=991, y=292) 
        pyautogui.scroll(15)
        time.sleep(0.5)
        pyautogui.click(x=991, y=292)
        pyautogui.click(x=1044, y=308)

        if End_date:
            print('คลิกเลือกวันที่สิ้นสุดต้นสำเร็จ : Pass')
            if date_29:
                print('คลิกเลือกวันที่ 29 สำเร็จ : Pass')
            else:
                print('คลิกเลือกวันที่ 29 ไม่สำเร็จ : Fail')
        else:
            print('คลิกเลือกวันที่สิ้นสุดไม่สำเร็จ : Fail')

        time.sleep(0.5)

        port_date = driver.find_element(By.XPATH, '//div[3]/div/div/div/div/button')
        port_date.click()

        date_30 = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[5]/button[2]')
        assert start_date.is_displayed(), 'Element is not displayed!'
        assert start_date.is_enabled(), 'Element is not enabled!'
        date_30.click()  

        # autogui เลือกเวลา วันที่แผร่เผย
        pyautogui.moveTo(x=1355, y=315) 
        pyautogui.scroll(-15)
        time.sleep(0.5)
        pyautogui.click(x=1355, y=315)
        pyautogui.click(x=1412, y=550)

        if port_date:
            print('คลิกเลือกวันที่แผร่เผยสำเร็จ : Pass')
            if date_30:
                print('คลิกเลือกวันที่ 30 สำเร็จ : Pass')
            else:
                print('คลิกเลือกวันที่ 30 ไม่สำเร็จ : Fail')
        else:
            print('คลิกเลือกวันที่เผยแผร่ไม่สำเร็จ : Fail')

        time.sleep(0.5)

    except ArithmeticError as e:
        driver.fail(f'ตรวจสอบไม่สำเร็จ: {e}')
    except NoSuchElementException as b:
        driver.fail(f'ไม่พบองค์ประกอบของ Elenemt: {b}')
    except Exception as n:
        driver.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง: {n}')
    except TimeoutException:
        driver.fail('การรอองค์ประกอบล้มเหลว')
        
    try:

        type_of_work = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[6]/div/div[2]/div/div/div')
        assert type_of_work.is_displayed(), 'Element is not displayed!'
        assert type_of_work.is_enabled(), 'Element is not enabled!'
        type_of_work.click()

        if type_of_work:
            print('คลิกประเภทงานสำเร็จ : Pass')
        else:
            print('คลิกประเภทงานไม่สำเร็จ : Fail')

        wait_element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/div[3]/ul/li[1]'))
        )
        print('รอจนสามารถพิมได้ : Event')

        event = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/ul/li[1]')
        assert event.is_displayed(), 'Element is not displayed!'
        assert event.is_enabled(), 'Element is not enabled!'
        event.click()

        if event:
            print('คลิกเลือกกิจกรรมสำเร็จ : Pass')
        else:
            print('คลิกเลือกกิจกรรมไม่สำเร็จ : Fail')
    except ArithmeticError as e:
        driver.fail(f'ตรวจสอบไม่สำเร็จ: {e}')
    except NoSuchElementException as b:
        driver.fail(f'ไม่พบองค์ประกอบของ Elenemt: {b}')
    except Exception as n:
        driver.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง: {n}')
    except TimeoutException:
        driver.fail('การรอองค์ประกอบล้มเหลว')


    result = None
    time.sleep(1)
    
    try:    
        add_tags = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div/button')
        assert add_tags.is_displayed(), 'Element is not displayed!'
        assert add_tags.is_enabled(), 'Element is not enabled!'
        add_tags.click()

        if add_tags:
            print('คลิก Add Tage สำเร็จ : Pass')
        else:
            print('คลิก Add Tage ไม่สำเร็จ : Fail')

        wait_element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
        )
        print('รอจนสามารถพิมได้ : Tags')

        key_tage = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
        )
        key_tage.send_keys('IMPACT Competency' + Keys.ARROW_UP + Keys.ENTER)    

        # key_tage = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[1]/div/div/div/div[2]/div/div/input')
        # key_tage.send_keys('IMPACT Competency' + Keys.ARROW_UP + Keys.ENTER)    

        input_key = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[1]/div/div/div/div[2]/div/div/input')
        input_value = input_key.get_attribute('value')
        print(f'ค่าที่ป้อนในฟิลด์: {input_value}')

        creditAmount = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[2]/div/div[2]/div/div/input')
        creditAmount.send_keys('1')

        input_key = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[2]/div/div[2]/div/div/input')
        input_value = input_key.get_attribute('value')
        print(f'ค่าที่ป้อนในฟิลด์: {input_value}')

        credit_age = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[3]/div/div/div/div/button')
        assert credit_age.is_displayed(), 'Element is not displayed!'
        assert credit_age.is_enabled(), 'Element is not enabled!'
        credit_age.click()

        wait_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[5]/button[2]'))
        )
        print('รอคลิก date_30')

        date_30 = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div[5]/button[2]')
        assert date_30.is_displayed(), 'Element is not displayed!'
        assert date_30.is_enabled(), 'Element is not enabled!'
        date_30.click()

        if credit_age:
            print('คลิกเลือกวันที่หมดอายุเครดิตสำเร็จ : Pass')
            if date_30:
                print('คลิกเลือกวันที่ 30 สำเร็จ : Pass')
            else:
                print('คลิกเลือกวันที่ 30 ไม่สำเร็จ : Pass')
        else:
            print('คลิกเลือกวันที่หมดอายุเครดิตไม่สำเร็จ : Fail')


        # autogui เลือกเวลา อายุเครดิต
        pyautogui.moveTo(x=1266, y=620) 
        pyautogui.scroll(-15)
        time.sleep(0.5)
        pyautogui.click(x=1266, y=620)
        pyautogui.click(x=1317, y=641)
        # time.sleep(3)
        # current_position = pyautogui.position()
        # print(f"The current mouse position is: {current_position}")
        time.sleep(0.3)

    except ArithmeticError as e:
        driver.fail(f'ตรวจสอบไม่สำเร็จ: {e}')
    except NoSuchElementException as b:
        driver.fail(f'ไม่พบองค์ประกอบของ Elenemt: {b}')
    except Exception as n:
        driver.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง: {n}')
    except TimeoutException:
        driver.fail('การรอองค์ประกอบล้มเหลว')
    


    try:

        Add_Permissions = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[1]/button')
        assert Add_Permissions.is_displayed(), 'Element is not displayed!'
        assert Add_Permissions.is_enabled(), 'Element is not enabled!'
        Add_Permissions.click()


        element_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/input")
        driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        time.sleep(1)

        wait_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
        )
        print('รอจนสามารถพิมได้ : company')

        Company = driver.find_element(by=By.XPATH, value=
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/input')
        Company.send_keys('บริษัท บางกอกแลนด์ เอเจนซี่ จำกัด' + Keys.ARROW_DOWN + Keys.ENTER)   


        wait_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/input'))
        )
        print('รอจนสามารถพิมได้ : Department')
    
        Department = driver.find_element(by=By.XPATH, value=
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/input')
        Department.send_keys('TEST Department' + Keys.ARROW_DOWN + Keys.ENTER)


        wait_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div/div/input'))
        )
        print('รอจนสามารถพิมได้ : levels')


        levels = driver.find_element(by=By.XPATH, value=
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div/div/input')
        levels.send_keys('5' + Keys.ARROW_UP + Keys.ENTER + Keys.ESCAPE)


        Save = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/button')
        assert Save.is_displayed(), 'Element is not displayed!'
        assert Save.is_enabled(), 'Element is not enabled!'
        Save.click()

        if Save:
            print('คลิก save สำเร็จ :', True)
        else:
            print('คลิก save ไม่สำเร็จ :', False) 
            sys.exit(1)

        wait_element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.ID, 'notistack-snackbar'))
        )
        print('รอจนสร้าง Event สำเร็จ : Pass')

        try:
            check = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[3]/p')
            if check.text == 'ACTIVITY':
                print('ข้อความถูกต้อง!!')
            elif check.text == 'ACTIVITY ผิดพลาด':
                print('ข้อความเป็นอีกแบบ')
            else:
                print('ข้อความไม่ตรงกับเงื่อนไขใด ๆ')
                # sys.exit(1)
        except Exception:
            print(False)
        # finally:
            # driver.quit()

        time.sleep(3)
    
    except NoSuchElementException as o:
        driver.fail(f'ไม่พบองค์ประกอบของ Elenemt')
    except TimeoutException:
        driver.fail('การรอองค์ประกอบล้มเหลว')
    except Exception as n:
        driver.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง :' + str(n))
    except AssertionError as e:
        driver.fail(str(e))

    return result  

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/dizny/Desktop/Impact/page event management'))


