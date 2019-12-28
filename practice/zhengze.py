import re
def main_1():
    '''
    1. 查找第一个匹配串
    :return:
    '''
    s = 'i love python very much'
    pat = 'python'
    r = re.search(pat,s)
    print(r.span()) # (7,13)

def main_2():
    '''
    re.findall()如果可以匹配返回的是一个列表，re.finditer()返回的是一个迭代器，
    需要对其进行遍历，才能获取数据。
    :return:
    '''
    s = '山东省潍坊市青州第1中学高三1班'
    pat = '1' # 需要匹配的字符
    r = re.finditer(pat, s)
    #r = re.findall(pat, s)
    # 将迭代出的结果添加至list中
    list = [ ]
    for i in r:
        list.append(i.group())
    print(list)

    c = re.findall(pat,s)
    print(c)

def main_3():
    '''
    匹配数字【0-9】
    :return:
    '''
    s = '一共20行代码运行时间13.59s'
    pat = '\d+'  # +表示匹配数字(\d表示数字的通用字符)1次或多次
    r = re.findall(pat, s)
    print(r)
    # ['20', '13', '59']







if __name__ == '__main__':
    main_3()