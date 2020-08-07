from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\Selenium_browser_drivers\chromedriver.exe")
baseUrl = "https://www.bongobd.com/"
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(5)

class View():

    def getfreecontent(self):
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/div[3]/div/div[5]/div/div[2]/div/div/div/div/div[3]/div/div/button').click()
        driver.implicitly_wait(40)
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div/video-js/button").click()


ff = View()
ff.getfreecontent()