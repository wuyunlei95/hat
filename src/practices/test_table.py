from common.base.box_driver import BoxBrowser,BoxDriver
'''
UCKeFu3.7 为例
'''
driver = BoxDriver(BoxBrowser.Chrome)
driver.navigate("http://192.168.1.243:8080")
driver.maximize_window()
driver.forced_wait(2)
driver.click('x,//*[@id="invite-btn"]')
driver.forced_wait(2)
driver.type('id,username','admin')
driver.type('id,password','123456')
driver.click('x,//button[text()="立即登录"]')
driver.forced_wait(3)

driver.click('x,/html/body/div/div[2]/div/ul/li[1]/dl/dd[4]/a')
driver.switch_to_frame('id,maincontent')
driver.forced_wait(3)
driver.click('x,/html/body/div/div[1]/div/ul/li/dl/dd[1]/a')
driver.forced_wait(3)


# # 获取第一行所有字段（列）
# row_td = driver.get_text_list('x,/html/body/div/div[2]/div/div[1]/div/table/tbody/tr[1]//td')
# for i in range(len(row_td)):
#     print(row_td[i])
# # 获取所有行的所有列
# # 总行数
# row_counts = driver.count_elements('x,/html/body/div/div[2]/div/div[1]/div/table/tbody//tr')
# print('总行数%s'%row_counts)
# for row in range(row_counts):
#     # 总列数
#     column_counts = driver.count_elements('x,/html/body/div/div[2]/div/div[1]/div/table/tbody/tr[1]//td')
#     print('总列数%s'%column_counts)
#     for column in range(column_counts):
#         td_text = driver.get_text('x,/html/body/div/div[2]/div/div[1]/div/table/tbody/tr[%d+1]/td[%d+1]'%(row,column))
#         print(td_text)


# 获取所有行的“客户名称”
customes = driver.get_text_list('x,/html/body/div/div[2]/div/div[1]/div/table/tbody//tr/td[2]')
for i in range(len(customes)):
    # 勾选‘客户名称’为'Custom_1'和’Custom_2'的客户
    # if customes[i] == 'dsdsdcdcscdscdsscdc' or customes[i] == 'dsdsdcdcscdscdsscdc':
    #     print('%s在第%d行'%(customes[i],i+1))
    #     # 点击‘客户名称’为'Custom_1'的行的“勾选框”
    #     driver.click('x,/html/body/div/div[2]/div/div[1]/div/table/tbody/tr[%d]/td[1]/input'%(i+1))
    #     driver.forced_wait(3)
    # 删除‘客户名称’为'Custom_1'的客户
    if customes[i] == 'wew':
        print(('%s在第%d行'%(customes[i],i+1)))
        # 点击‘客户名称’为'Custom_1'的行的“删除”按钮
        driver.click('x,/html/body/div/div[2]/div/div[1]/div/table/tbody/tr[%d]/td[10]/a[2]'%(i+1))
        driver.switch_to_default()
        driver.click('x,//*[@id="layui-layer1"]/div[3]/a[1]')

driver.quit()