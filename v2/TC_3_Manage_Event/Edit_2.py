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


def edit_event2(driver):

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

        Edit_Event = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div[2]/div/div/div[1]/table/tbody/tr[1]/td[7]/p/div/button[1]')
        assert Edit_Event.is_displayed(), 'Element is not displayed!'
        assert Edit_Event.is_enabled(), 'Element is not enabled!'
        Edit_Event.click()
        if Edit_Event:
            print('กดคลิก Edit Event สำเร็จ : Pass')
        else:
            print('กดคลิกขอ Edit Event ไม่สำเร็จ : Fail')

        element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.NAME, 'name'))
        )
        print('รอจนสามารถกรอกข้อมความได้ : Pass')
        time.sleep(1)

        pyautogui.click(x=885 , y=489)
        time.sleep(0.3)
        pyautogui.moveTo(x=483, y=523)
        time.sleep(0.3)
        pyautogui.click(x=483, y=523)
        time.sleep(0.2)
        pyautogui.click(x=642, y=437)
        pyautogui.press('enter')

        
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
        Key_Name_Event.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        Key_Name_Event.send_keys('กิจกรรมบิงโก')

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
        key_Type_for_something.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_Type_for_something.send_keys('องค์กรใดใส่ใจ Job Description เป็นอย่างดี ปัญหาต่างๆ ในระบบการทำงานก็มักจะไม่เกิดขึ้น เพราะ Job Description ที่ดีนั้นจะสามารถบ่งบอกบทบาทและหน้าที่ของแต่ละคนในองค์กรได้อย่างชัดเจน ไม่ทำงานทับซ้อน ล้ำเส้น ')

        # key_Type_for_something = driver.find_element(By.XPATH, '')
        # key_Type_for_something.send_keys(
        # 'ระบุทรัพยากรเป้าหมายของคำขอเมื่อรวมกับข้อมูลที่ให้ไว้ในHostส่วนหัว นี่คือเส้นทางสัมบูรณ์ (เช่น/path/to/file.html) ในคำขอไปยังเซิร์ฟเวอร์ต้นทาง และ URL สัมบูรณ์ในคำขอไปยังพร็อกซี')

        element_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[1]/div/div[2]/div/div/input")
        driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        time.sleep(1)

        key_location = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[1]/div/div[2]/div/div/input')
        key_location.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_location.send_keys('Impact เมืองทองธานี')

        input_key = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[1]/div/div[2]/div/div/input')
        input_value = input_key.get_attribute('value')
        print(f'ค่าที่ป้อนในฟิลด์: {input_value}') 

        key_Specify_quantity = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[4]/div[2]/div/div[2]/div/div/input')
        key_Specify_quantity.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_Specify_quantity.send_keys('50')

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
        pyautogui.moveTo(x=452, y=661) 
        time.sleep(0.5)
        pyautogui.click(x=452, y=661)

        # คลิกกรอบเวลา
        click_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[1]').click()        

        select_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[1]/li[11]')
        actions = ActionChains(driver)
        actions.move_to_element(select_time).click().perform()
        time.sleep(1)

        # คลิกกรอบเวลา
        click_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[2]').click()        

        select_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[2]/li[1]')
        actions = ActionChains(driver)
        actions.move_to_element(select_time).click().perform()
        time.sleep(0.5)

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

        # autogui เลือกเวลา วันที่จบ
        pyautogui.moveTo(x=845, y=646) 
        time.sleep(0.5)
        pyautogui.click(x=845, y=646)

        # คลิกกรอบเวลา
        click_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[1]').click()        

        select_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[1]/li[11]')
        actions = ActionChains(driver)
        actions.move_to_element(select_time).click().perform()
        time.sleep(1)

        # คลิกกรอบเวลา
        click_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[2]').click()        

        select_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[2]/li[1]')
        actions = ActionChains(driver)
        actions.move_to_element(select_time).click().perform()
        time.sleep(0.5)

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

        # autogui เลือกเวลา วันที่จบ
        pyautogui.moveTo(x=1159, y=648) 
        time.sleep(0.5)
        pyautogui.click(x=1159, y=648)

        # คลิกกรอบเวลา
        click_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[1]').click()        

        select_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[1]/li[11]')
        actions = ActionChains(driver)
        actions.move_to_element(select_time).click().perform()
        time.sleep(1)

        # คลิกกรอบเวลา
        click_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[2]').click()        

        select_time = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[1]/div/div[2]/ul[2]/li[1]')
        actions = ActionChains(driver)
        actions.move_to_element(select_time).click().perform()
        time.sleep(0.5)    

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
        time.sleep(0.5)

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

        wait_element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
        )
        print('รอจนสามารถพิมได้ : Tags')

        key_tage = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
        )
        key_tage.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        key_tage.send_keys('Competency V2' + Keys.ARROW_UP + Keys.ENTER)    

        # key_tage = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[1]/div/div/div/div[2]/div/div/input')
        # key_tage.send_keys('IMPACT Competency' + Keys.ARROW_UP + Keys.ENTER)    

        input_key = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[1]/div/div/div/div[2]/div/div/input')
        input_value = input_key.get_attribute('value')
        print(f'ค่าที่ป้อนในฟิลด์: {input_value}')

        creditAmount = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div[1]/form/div[1]/div[7]/div[2]/div[2]/div/div[2]/div/div/input')
        creditAmount.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        creditAmount.send_keys('5')

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

        # autogui เลือกเวลา วันที่อายุเครดิต
        pyautogui.moveTo(x=1068, y=471) 
        time.sleep(0.5)
        pyautogui.click(x=1068, y=471)

        # select time
        pyautogui.moveTo(x=1254, y=275)
        time.sleep(0.5)
        pyautogui.click(x=1254, y=275)
        time.sleep(0.5)
        pyautogui.moveTo(x=1315, y=270)
        time.sleep(0.5)
        pyautogui.click(x=1315, y=270)

    except ArithmeticError as e:
        driver.fail(f'ตรวจสอบไม่สำเร็จ: {e}')
    except NoSuchElementException as b:
        driver.fail(f'ไม่พบองค์ประกอบของ Elenemt: {b}')
    except Exception as n:
        driver.fail(f'เงื่อนไขไม่ตรงตามที่คาดหวัง: {n}')
    except TimeoutException:
        driver.fail('การรอองค์ประกอบล้มเหลว')

    try:

        element_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/form/button")
        driver.execute_script("arguments[0].scrollIntoView(true);", element_2)
        time.sleep(1)

        wait_element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/input'))
        )
        print('รอจนสามารถพิมได้ : company')

        Company = driver.find_element(by=By.XPATH, value=
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div/div/input')
        Company.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        Company.send_keys('บริษัท อิมแพ็ค เอ็กซิบิชั่น แมเนจเม้นท์ จำกัด' + Keys.ARROW_DOWN + Keys.ENTER)   


        wait_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/input'))
        )
        print('รอจนสามารถพิมได้ : Department')
    
        Department = driver.find_element(by=By.XPATH, value=
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/input')
        Department.send_keys(Keys.COMMAND + 'a' + Keys.DELETE)
        Department.send_keys('City Management Department' + Keys.ARROW_DOWN + Keys.ENTER)


        wait_element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div/div/input'))
        )
        print('รอจนสามารถพิมได้ : levels')

        # ลบ Levels
        pyautogui.moveTo(x=1014, y=872) 
        time.sleep(0.5)
        pyautogui.doubleClick(x=1014, y=872)
        time.sleep(0.3)


        levels = driver.find_element(by=By.XPATH, value=
        '/html/body/div[2]/div[3]/div/div[1]/form/div[2]/div/div[2]/div[3]/div/div/div/div[2]/div/div/input')
        levels.send_keys('5' + Keys.ARROW_UP + Keys.ENTER + Keys.ESCAPE)
        time.sleep(0.7)
        levels.send_keys('1' + Keys.ARROW_DOWN + Keys.ENTER + Keys.ESCAPE)


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


