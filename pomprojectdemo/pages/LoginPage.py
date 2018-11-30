import sys
import os
#from pomprojectdemo import locatos
#sys.path.append(os.path.dirname(__file__),"...","...")
class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.userName_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.loginbutton = "btnLogin"
    def setUserName(self,userName):
        self.driver.find_element_by_id(self.userName_textbox_id).clear()
        self.driver.find_element_by_id( self.userName_textbox_id).send_keys(userName)
    def setPasswod(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    def click_Login(self):
        self.driver.find_element_by_id(self.loginbutton).click()
