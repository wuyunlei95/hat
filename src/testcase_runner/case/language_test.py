# coding=utf-8
import unittest

from common.base.box_driver import BoxDriver, BoxBrowser
from src.page.sys_main_page_zl import SysMainPage
from common.util.csv_file import CSV_File


class LanguageTest(unittest.TestCase):
    """
        TC-Language: 语言测试
    """

    def setUp(self):
        self.driver = BoxDriver(BoxBrowser.Chrome)
        self.sysMainPage = SysMainPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_before(self):
        """登录前语言测试"""

        # 进入登录页面
        self.sysMainPage.enter_login()
        # 读取数据，过滤标题
        data = CSV_File().read('data/language_before.csv')
        for list in data:
            # 选择语言作为输入条件，获取实际结果
            language_list = self.sysMainPage.language_before_login(list[0])
            # 获取预期结果
            list_expect = list[1:]
            # 循环断言，判断每个位置是否正确显示
            length = len(language_list)
            for i in range(length - 1):
                self.assertEqual(list_expect[i], language_list[i], '语言没有正确显示，正确语言为%s' % str(list_expect[0]))

    def test_after(self):
        """登录后语言测试"""
        # 进入登陆页面
        self.sysMainPage.enter_login()
        # 登陆页面
        self.sysMainPage.login({'username': 'admin', 'password': '123456'})
        # 读取数据，过滤标题
        data = CSV_File().read('data/language_after.csv')
        for list in data:
            # 点击左侧底部用户功能按钮
            self.sysMainPage.click_left_buttom_user()
            # 获取当前语言类型
            text = self.sysMainPage.get_current_language()
            if text == list[0]:
                # 如果要切换的语言为当前语言，点击功能按钮，回到主页面
                self.sysMainPage.click_left_buttom_user()
            else:
                # 点击当前语言
                self.sysMainPage.click_current_language()
                # 切换语言
                self.sysMainPage.choose_language(list[0])
            # 实际标题内容
            top_list = self.sysMainPage.get_myplace_title_language()
            # 预期标题内容
            expect_list = list[1:]
            length = len(top_list)
            # 循环断言，判断每个位置是否正确显示
            for i in range(length - 1):
                self.assertEqual(expect_list[i], top_list[i], '语言没有正确显示，正确语言为%s' % str(expect_list[0]))


if __name__ == '__main__':
    # main是错的，要main()
    # unittest.main
    unittest.main()
