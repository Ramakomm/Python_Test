class Homepage():
    def __init__(self,driver):
        self.driver = driver
        self.welcome_button = "welcome"
        self.Logout_link = "Logout"
    def chk_welcome_scrren(self):
        self.driver.find_element_by_id(self.welcome_button).click()
    def Logout_page(self):
        self.driver.find_element_by_link_text(self.Logout_link).click()
        