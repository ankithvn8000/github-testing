from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DemoRightClick:
    def demo_RClick(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(5)
        
        #Right_Click
        #xbutton  = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        #achains = ActionChains(driver)
        #achains.context_click(xbutton).perform()
        #time.sleep(5)
        #driver.find_element(By.XPATH, "//span[normalize-space()='Edit']").click()
        #time.sleep(5)


        #Double_Click
        xbutton = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        achains = ActionChains(driver)
        achains.double_click(xbutton).perform()
        time.sleep(5)

DMouse = DemoRightClick()
DMouse.demo_RClick()
