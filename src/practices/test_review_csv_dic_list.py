'''
字典练习
'''
# ele = {'account':'admin','pwd':'123456'}
# print(ele['account'])

'''
数组练习
'''
# ele = ['aaa','bbb','ccc']
# print(ele[0:3])
# for i in ele:
#     print(i)
# ele = open('..\\data\\uc_login.csv',mode = 'r',encoding =' utf8')
# a = ele.read()
# for t in ele:
#     print(t)

'''
读取csv练习
'''
import csv

open_csv = open('..\\data\\add_user_fields.csv', mode='r', encoding='utf-8')
read_csv = csv.reader(open_csv)
for i in read_csv:
    print(i)
# 注意，每次打开csv文件后，要关闭
open_csv.close()
