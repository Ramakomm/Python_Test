from selenium import webdriver
import sys
import os
from pomprojectdemo.pages import LoginPage
from pomprojectdemo.pages import HomePage
import time
import HtmlTestRunner
import LoginPage
import HomePage
import unittest
class LoginTest(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\selenium\\sofware\\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
     def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login1 = LoginPage.LoginPage(driver)
        hm = HomePage.Homepage(driver)
        login1.setUserName("Admin")
        login1.setPasswod("admin123")
        login1.click_Login()
        hm.chk_welcome_scrren()
        hm.Logout_page()
     def breakDown(self):
         self.driver.close()
         self.driver.quit()
         print("testing complete")
if __name__ == 'main':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output ='C:/Users/Akshara/ycharmProjects/sampleSELPython/pomprojectdemo/output'))

