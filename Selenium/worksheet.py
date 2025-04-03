import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




driver = webdriver.Chrome()
driver.execute_script("window.open('https://secure.yatra.com/social/common/yatra/signin.htm')")
driver.maximize_window()
time.sleep(3)  # Allow page to load
demo = driver.execute_script("return document.getElementsByTagName('p')[11];")
driver.execute_script("arguments[0].click();",demo)

driver.current_window_handle


departure_field = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
departure_field.click()
time.sleep(4)
driver.get_screenshot_as_file("C:\\Users\Lenovo\Pictures\Screenshots\\error.png")
driver.quit()



