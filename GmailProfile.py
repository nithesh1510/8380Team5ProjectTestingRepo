import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Onspar_notifications_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_log(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://onspar.pythonanywhere.com/login")
        driver.find_element_by_xpath("/html/body/div[2]/a[1]").click()
        time.sleep(6)
        elem = driver.find_element_by_name("identifier")
        elem.clear()
        elem.send_keys("onsparwebsite")
        elem.send_keys(Keys.RETURN)
        time.sleep(6)
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys("onspar@1234")
        elem.send_keys(Keys.RETURN)
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/nav/div/div/ul[2]/li[2]/a").click()
        time.sleep(3)
        elem = driver.find_element_by_name("phoneNumber")
        elem.clear()
        elem.send_keys("4023456382")
        elem = driver.find_element_by_name("address")
        elem.clear()
        elem.send_keys("1110 S 60th Street")
        elem = driver.find_element_by_name("city")
        elem.clear()
        elem.send_keys("Omaha")
        elem = driver.find_element_by_name("zipcode")
        elem.clear()
        elem.send_keys("68182")
        elem = driver.find_element_by_name("country")
        elem.clear()
        elem.send_keys("United States")
        elem = driver.find_element_by_name("photo")
        elem.clear()
        elem.send_keys("https://upload.wikimedia.org/wikipedia/commons/6/63/Luffy.jpg")
        elem.send_keys(Keys.RETURN)
        time.sleep(6)
        driver.find_element_by_xpath("/html/body/nav/div/div/ul[2]/li[2]/a").click()
        time.sleep(5)



        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()