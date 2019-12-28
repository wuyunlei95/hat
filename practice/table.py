import time
from selenium import webdriver
from common.base.box_driver import BoxDriver, BoxBrowser

driver = BoxDriver(BoxBrowser.Chrome)
d=webdriver.Chrome
# driver.navigate("https://www.baidu.com")
# 用xpath通过ID属性定位
# driver.type("x,//*[@id='kw']", "python")
# 用xpath通过name属性定位
# driver.type_enter("x,//*[@name='wd']", '北京')
# 用xpath通过name属性定位
# driver.type_enter("x,//*[@class='s_ipt']", "baijing")
# driver.type_enter("x,//input[@autocomplete='off']", "baijing")
# driver.type_enter("x,//input[@class='s_ipt']","北京")
driver.navigate("http://bj.ganji.com/")
time.sleep(2)
h = d.current_window_handle
# print("1")
print(h)
# print("2")
driver.click("l,兼职")
all_h = d.window_handles
print(all_h)

