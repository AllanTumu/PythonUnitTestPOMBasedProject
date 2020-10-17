import sys
import unittest
import HtmlTestRunner
import time
from selenium import webdriver

sys.path.append("/home/mea/PycharmProjects/UnitTestPOMBasedProject")
from pageObjects.LoginPageElements import LoginPageElements


class LoginTestCases(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/"
    email = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="/home/mea/PycharmProjects/UnitTestPOMBasedProject/drivers/chromedriver")

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login(self):
        lp = LoginPageElements(self.driver)
        lp.clearText()
        lp.setUserName(self.email)
        lp.clearPassword()
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        print(self.driver.title)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Webpage title incorrect")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/mea/PycharmProjects/UnitTestPOMBasedProject"
                                                                  "/reports"))
