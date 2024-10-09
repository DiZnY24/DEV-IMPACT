from selenium import webdriver
import time
import unittest
from Login_Impact.login_Impact import login_impact
from Login_fail.Login_fail_V2 import login_fail
from Add_Event.event_V2 import add_event
from Delete_Event.delete_event_V2 import delete_event


class WebTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get('https://dev.backoffice.hr-impact.co/')
        cls.driver.set_window_size(1600, 1000)
        cls.driver.implicitly_wait(15)

    def test_event_management(self):
        # login_fail(self.driver) # ล็อกอินล้มเหลว
        login_impact(self.driver) # ล็อกอิน impact,IM
        if login_impact:
            print('--------------------------------')
        else:
            print('Fail')

        # for i in range(4):
        add_event(self.driver) # สร้าง Events ฟิล
        if add_event:
            print('--------------------------------')
        else:
            print('Fail')
        #         # break
        #     # pass
        
        delete_event(self.driver) # ลบ Events 
        if delete_event:
            print('--------------------------------')
        else:
            print('Fail')
       
        # คุณสามารถเพิ่มการตรวจสอบผลลัพธ์ที่นี่ เช่น assertIn

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
