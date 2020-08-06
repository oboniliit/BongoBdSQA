import unittest
from selenium import webdriver


class BongoBdCheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="c:\Selenium_browser_drivers\chromedriver.exe")

    def test_bongobdSetUpCheck(self):
        baseUrl = "https://www.bongobd.com/"
        driver = self.driver
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.close()

    def test_getFreeContentCheck(self):
        driver = self.driver
        baseUrl = "https://www.bongobd.com/"
        driver = self.driver
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[3]/div/div[5]/div/div[2]/div/div/div/div/div[3]/div/div/button').click()
        driver.implicitly_wait(40)
        driver.find_element_by_xpath("/html/body/div/div/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div/video-js/button").click()


if __name__ == "__main__":
    unittest.main()
