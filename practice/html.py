
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("file:///C:Users\wu\Desktop\单选框，复选框操作.html")
# 没点击操作前，判断选项框状态
s = driver.find_element_by_id("boy").is_selected()
print(s)
driver.find_element_by_id("boy").click()
# 点击后，判断元素是否为选中状态
r = driver.find_element_by_id("boy").is_selected()
print(r)
# 复选框单选
driver.find_element_by_id("c1").click()
# 复选框全选
checkboxs = driver.find_elements_by_xpath(".//*[@type='checkbox']")
for i in checkboxs:
    i.click()