import csv

class CSV_File(object):
    """读写csv文件"""

    def read_by_list(self, path):
        """
        list(数组）形式读取csv里面的数据
        过滤首行标题
        @:param path(文件路径)
        @:return list
        """
        file = open(path, 'r', encoding='utf8')
        data = csv.reader(file)
        list = []
        flag = True
        for data_list in data:
            if flag:
                flag = False
                continue
            list.append(data_list)
        file.close()
        return list

    def read_by_dict(self, path_dict):
        '''
        字典方式读取csv文件
        :param path: csv文件路径
        :return: 字典类型
        '''
        param = open(path_dict, mode='r', encoding='utf-8')
        data = csv.DictReader(param)
        return data

'''
main
ctrl + /    
main
'''
"""
多行注释
"""


if __name__ == '__main__':
# 类名() 实例化类
# 类名(变量)
#     Csv_File = CSV_File()
#     data =Csv_File.read_by_list('../../src/data/1.csv')
#     for list in data:
#         print(list)


    data = CSV_File().read_by_dict('..//..//src//data//1.csv')
    for row in data:
        print(row)


