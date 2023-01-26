import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

a1 = browser.find_element(By.ID, "num1")
a2 = a1.text
b1 = browser.find_element(By.ID, "num2")
b2 = b1.text
y = str(int(a2)+int(b2))

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(y)

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
browser.quit()