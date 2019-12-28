from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:81/ranzhi/www")
sleep(3)
account = driver.find_element_by_id('account')
account.send_keys("admin")
pwd = driver.find_element_by_id('password')
pwd.send_keys("admin")
submit = driver.find_element_by_id('submit')
submit.click()
