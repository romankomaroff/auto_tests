from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.CLASS_NAME, "first")
input1.send_keys("Ivan")
input2 = browser.find_element(By.CLASS_NAME, "second")
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, "third")
input3.send_keys("kom@mail.ru")
time.sleep(2)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(5)

a = browser.find_element(By.TAG_NAME, 'h1')
if "Congratulations! You have successfully registered!" == a.text:
	print('OK!')
else:
	print('WRONG!')

time.sleep(5)
browser.quit()