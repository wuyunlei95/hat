import unittest
import paramunittest
import time

from common.util.csv_file import CSV_File

'''

1. 必须在if __name__ == "__main__":下面运行；
2. 必须写def setParameters
3. def setParameters里面的参数严格对应的是@paramunittest.parametrized里的参数
4.    字典 {"user": "admin", "psw": "123", "result": "false"},或者元祖('admin','123','result')都可以

'''
# csv_data = CSV_File().read_by_dict('src/data/module_title.csv')
csv_data = CSV_File().read_by_dict('../../src/data/module_title.csv')


@paramunittest.parametrized(
    *csv_data
)


class TestDemo(unittest.TestCase):
    def setUp(self):
        pass

    def setParameters(self,**csv_data):
        self.csv_data = csv_data

    def test_case(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print(("module：%s" % self.csv_data['module']))
        print(("expect：%s" % self.csv_data['expect']))
        time.sleep(0.5)
        self.assertTrue(self.csv_data['module'] == "MY_PLACE")

    def test_1(self):
        print("2")
        self.assertEqual(1,2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
