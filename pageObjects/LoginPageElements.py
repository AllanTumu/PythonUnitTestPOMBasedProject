from selenium import webdriver


# Locators of all the elements
class LoginPageElements:
    email_text_box_id = "Email"
    password_pswd_box_id = "Password"
    remember_me_check_box_xpath = "//input[@id='RememberMe']"
    login_button_xpath = "//*[contains(@type,'sub')]"
    link_welcome_linktext = "welcome"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def clearText(self):
        self.driver.find_element_by_id(self.email_text_box_id).clear()

    def setUserName(self, email):
        self.driver.find_element_by_id(self.email_text_box_id).send_keys(email)

    def clearPassword(self):
        self.driver.find_element_by_id(self.password_pswd_box_id).clear()

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_pswd_box_id).send_keys(password)

    def clickRememberMe(self):
        self.driver.find_element_by_id(self.remember_me_check_box_xpath).click()

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.link_logout_linktext).click()
