import unittest
import paramunittest

from common.base.html_test_runner import HtmlTestRunner
from common.util.csv_file import CSV_File


data = CSV_File().read_by_dict('src//data//multi_data.csv')



@paramunittest.parametrized(
    # ('1', '2'),
    # (4, 3),
    # ('2', '3'),
    # (('4', ), {'b': '5'}),
    # ((), {'a': 5, 'b': 6}),
    # {'a': 5, 'b': 6},
    # print(data)
    *data


)
class TestBar(unittest.TestCase):
    def setUp(self):
        pass

    def setParameters(self, **data):
        print((1))
        self.data = data


    def testLess(self):
        data = self.data
        print((1))
        self.assertLess(data['a'], data['b'])

    # def testMore(self,):
    #     data = self.data
    #     print(2)
    #     self.assertTrue(data['a']>data['b'])


if __name__ == '__main__':
    # unittest.main()
    test_dir = '.'
    suite = unittest.defaultTestLoader.discover(test_dir,
                                                pattern='multi_data_run.py')
    file_name = 'testresult.html'
    fp = open(file_name, 'wb')
    runner = HtmlTestRunner(stream=fp,title='multi_data',verbosity=2,description='测试多条数据')
    runner.run(suite)
    fp.close()