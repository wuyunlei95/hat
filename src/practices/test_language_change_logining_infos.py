from src.page.sys_main_page_zl import SysMainPage
from common.util.csv_file import CSV_File
from common.base.box_driver import BoxBrowser,BoxDriver
import unittest

class TestLanguageChangeLoginingInfos(unittest.TestCase):
    '''
    获取所有的页面元素文本信息，与预期逐一进行断言
    '''
    def setUp(self):
        self.driver = BoxDriver(BoxBrowser.Chrome)
        self.driver.navigate("http://localhost:81/ranzhi/www")
        self.driver.maximize_window()
        self.sys_main_page = SysMainPage(self.driver)
        self.driver.forced_wait(2)

    def tearDown(self):
        self.driver.quit()

    def test_language_change_logining_infos(self):
        # 读取数据，过滤标题
        data = CSV_File().read('../data/language_before.csv')
        print(("读取csv数据list:%s" % data))
        for list in data:
            print(('list:%s' % list))
            # 选择语言作为输入条件，获取实际结果
            language_list = self.sys_main_page.language_before_login(list[0])
            # 获取预期结果
            # 数组的第2个至最后一个
            list_expect = list[1:]
            print(("list_expect:%s" % list_expect))
            # 循环断言，判断每个位置是否正确显示
            length = len(language_list)
            print(("length:%d" % length))
            for i in range(length):
                print(('list_expert:%s,language_list:%s' % (list_expect[i], language_list[i])))
                # assert list_expect[i] == language_list[i]
                self.assertEqual(list_expect[i], language_list[i])

if __name__ == '__main__':
    unittest.main()



