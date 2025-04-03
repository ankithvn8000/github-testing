import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
time.sleep(5)

dropdown = driver.find_element(By.XPATH, "//div[@id='withOptGroup']//div[contains(@class,'css-tlfecz-indicatorContainer')]//*[name()='svg']")
select = Select(dropdown)

select.select_by_index(0)
time.sleep(5)



driver.quit()