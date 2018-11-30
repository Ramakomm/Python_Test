import pomprojectdemo.Locators
import time
class Fb_Home:
    def __init__(self,driver):
        self.driver = driver

    def logout_fb(self):
        driver = self.driver
        #Fb_Home.logout_menu(self)
        #self.driver.find_element_by_css_selector(pomprojectdemo.Locators.locatos.Locators.fb_logout_selector).submit()
        #driver.find_element_by_xpath("//div[@id='userNavigationLabel']").click()
        #driver.find_element_by_xpath("//input[@value='Log Out']").click();
        #driver.find_element_by_css_selector('a[data-gt*="menu_logout"]>span>span._54nh').click();
        driver.find_element_by_id("userNavigationLabel").click();