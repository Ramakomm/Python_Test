import pomprojectdemo
import pomprojectdemo.Locators.locatos

class Fb_Login:
    def __init__(self,driver):
        self.driver = driver
        self.userName_textbox_id = pomprojectdemo.Locators.locatos.Locators.fb_username_textbox_id
        self.password_textbox_id = pomprojectdemo.Locators.locatos.Locators.fb_pasword_textbox_id
        self.loginbutton = pomprojectdemo.Locators.locatos.Locators.fb_login_button_id
    def setUsername(self,usrName):
        self.driver.find_element_by_id(self.userName_textbox_id).clear()
        self.driver.find_element_by_id(self.userName_textbox_id).send_keys(usrName)
    def setPassword(self,pwd):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(pwd)
    def click_Login(self):
        self.driver.find_element_by_id(self.loginbutton).click()

