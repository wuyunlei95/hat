from common.base.box_driver import BoxDriver,BoxBrowser

driver = BoxDriver(BoxBrowser.Chrome)
sqlfile_path = '..\\data\\sql\\select_tt1.sql'
ip = '192.168.1.246'
user = 'tester_6'
pwd = '123456'
database = 'a'
sql_data = driver.get_sql_data(sqlfile_path,ip,user,pwd,database)
print(sql_data)
for i in sql_data:
    print((i[1]))
# print(sql_data[0])
# print(sql_data[0][0])
# print(sql_data[0][1])
driver.quit()