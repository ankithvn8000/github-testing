from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DemoMouse:
    def demo_mouse(self):
        driver = webdriver.Chrome()
        driver.get("https://dribbble.com/tags/mouse-over")
        driver.maximize_window()
        time.sleep(5)
        xbutton  = driver.find_element(By.XPATH, "//a[normalize-space()='Explore']")
        achains = ActionChains(driver)
        achains.move_to_element(xbutton).perform()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[contains(text(),'Product Design')]").click()
        time.sleep(5)

DMouse = DemoMouse()
DMouse.demo_mouse()
