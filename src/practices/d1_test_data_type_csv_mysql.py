# 数字
from common.util.csv_file import CSV_File
from common.util.mysql_connect import MysqlConnect

print((1))

# 字符串
var1 = 'Hello World!'
var2 = "Python Runoob"

print(("var1[0]: ", var1[0]))
print(("var2[1:5]: ", var2[1:5]))
print(("var2[1:5]: ", var2[1:]))
print(("var2[1:5]: %s"%var2[1:]))

# 布尔值
b = True
if b == False:
    print("b为布尔值 False")
else:
    print("b为布尔值 True")

# 数组 list
a = [1,2,3,'a','b']
print(("数组的第一个数据是从下标0开始的,所以数组a[0]的值为：%s"%a[0]))
# 获取数组中所有元素(1)
for i in a:
    print(("循环打印数组中所有的数据(方法1):%s"%i))
# 获取数组中所有元素(2)
for j in range(len(a)):
    print(("循环打印数组中所有的数据(方法 2 ):%s"%a[j]))

# 元组 tuple
# 元组只有1个的时候，要加个,
a = (1,)
print(a)
print((a[0]))

b = ('a','b',3,4)
print((b[0]))
for i in b:
    print(("循环打印元组中所有的数据(方法1):%s"%i))
for j in range(len(b)):
    print(("循环打印元组中所有的数据(方法 2 ):%s"%b[j]))

# 字典 dict
a = {'name':'ZhangSan','Sex':'男','Address':'广东省深圳市'}
print((a['name']))


# for 循环
print((list(range(4))))

for i in range(4):
    print(("for循环方式range(4):%s"%i))

for i in range(1,4):
    print(("for循环方式range(1,4):%s"%i))

for i in range(1,4,2):
    print(("for循环方式range(1,4,2):%s"%i))

# while 循环
a = 1
while(a<8):
    print(("while循环test:%i"%a))
    # a = a + 1
    a +=1

# 条件判断 if .. elif ..else
a = 6
b = True
if a == 1:
    print(" a 的值为1")
elif a == 2:
    print(" a 的值为2")
elif a == 3:
    print(" a 的值为3")
else:
    print(" a 不为1,2,3")

if b == False:
    print("b为布尔值 False")
else:
    print("b为布尔值 True")

# 与 或 非
a = 4
b = 8
c = 'a'
if a == 7 or b == 5 or c == 'a':
    print("or（或）： 只需要任意一个条件成立即可！")
if a == 4 and b == 5:
    print("and（与）: 必须所有条件都成立才可以！")
if a == 4 and b == 8:
    print("and（与）: 都成立！")
if a != 3:
    print("!=（非）: 不等于")

# 读取 yaml配置文件
# 读取 csv
# 数组（列表）方式读取

Csv_File = CSV_File()

data = Csv_File.read_by_dict('../data/1.csv')
# data = Csv_File.read_by_dict('src/data/1.csv')
for row in data:
    print(("字典方式读取：%s"%row))
# 字典方式读取

data =Csv_File.read_by_list('../data/1.csv')
# data =Csv_File.read_by_list('src/data/1.csv')
for list in data:
    print(("数组方式读取：%s"%list))

# 读取 mysql
# 非 main.py 调用方法
db_path = '../../common/config/ranzhi.yaml'
# main.py主入口调用路径如下：
# db_path = 'common/config/ranzhi.yaml'
connect = MysqlConnect(db_path)
data = connect.query('select account,gender from sys_user;')
print(data)
user_accounts = []
for i in range(len(data)):
    user_accounts.append(data[i][0])
print(user_accounts)
connect.close()

# Pycharm 常用快捷键
'''
ctrl + shift + -  方法，类收缩
ctrl + shift + +  方法，类展开
ctrl + d 复制当前行
ctrl + x 删除当前行
shift + Enter 快速切换到下一行
shift + tab 反缩进； tab 缩进
ctrl + r 当前文件中搜索
Alt + Enter 快速导入包
main     if __name__ == '__main__':
三击选中一行
'''

