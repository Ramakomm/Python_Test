import unittest
import pytest
import pomprojectdemo
from pomprojectdemo.pages import Fb_Login
from pomprojectdemo.pages import Fb_Home
from pomprojectdemo.tests import Setup
from pomprojectdemo.utils1 import setup
from selenium.webdriver.chrome.options import Options
import Fb_Login
import HtmlTestRunner
from selenium import webdriver
from Fb_Login import Fb_Login

class Login_FB(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=Setup.CHROME_PATH)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login_valid(self):
        #try:
            driver = self.driver

            chrome_options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications": 2}
            chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(chrome_options=chrome_options)

            driver.get(setup.fb_URL)
            log = pomprojectdemo.pages.Fb_Login.Fb_Login(driver)
            log.setUsername(setup.fb_username)
            log.setPassword(setup.fb_password)

            log.click_Login()

            assert "Facebook" in driver.title

            #driver.implicitly_wait(60000)
            #driver.get_screenshot_as_file("C:/Users/Akshara/PycharmProjects/sampleSELPython/pomprojectdemo/output/ss2.png")

            #driver.implicitly_wait(1000)
            hm = pomprojectdemo.pages.Fb_Home.Fb_Home(driver)

            #driver.switch_to_window(driver.current_window_handle)
            print("success")
            #driver.implicitly_wait(10)
            hm.logout_fb()
            #log.click_Login()

        #except Exception:
            #print("Error encounteres")
        #finally:
            #print("Testing done")





if __name__ == '__main__':
    log_file = 'C:/Users/Akshara/PycharmProjects/sampleSELPython/pomprojectdemo/output/log_file.txt'
    f = open(log_file, "w")
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)
    f.close()
    #unittest.main()
