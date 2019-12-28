import unittest

from common.base.box_driver import BoxDriver, BoxBrowser

from src.page.sys_main_page_zl import SysMainPage
from common.util.csv_file import CSV_File


class ModuleTitleTest(unittest.TestCase):
    """
        TC-Login: 模块title测试
    """

    def setUp(self):
        """测试准备操作"""
        # 实例化driver
        self.driver = BoxDriver(BoxBrowser.Chrome)
        # 实例化系统页面
        self.sysMainPage = SysMainPage(self.driver)

    def tearDown(self):
        """测试退出操作"""
        # 关闭浏览器
        self.driver.quit()

    def test_module_titile(self):
        """模块标题测试"""
        # 进入登录页面
        self.sysMainPage.enter_login()
        # 登录
        self.sysMainPage.login({'username': 'admin', 'password': '123456'})
        # 读取测试用例数据
        data = CSV_File().read('data/module_title.csv')
        # 循环点击模块，获取模块标题，进行断言
        for list in data:
            module_name = list[0]
            # 获取标题预期结果
            expect_titles = list[1].split('|')
            # 点击模块，获取实际标题结果
            self.sysMainPage.click_module(module_name)
            # 进入窗体
            self.sysMainPage.enter_iframe(module_name)
            # 获取模块标题内容
            real_titles = self.sysMainPage.get_module_title(module_name)
            # 退出窗体
            self.sysMainPage.switch_out_iframe()
            length = len(real_titles)
            # 循环断言每个title
            for i in range(length - 1):
                self.assertEqual(expect_titles[i], real_titles[i], '%s标题没有正确显示' % expect_titles[i])


if __name__ == '__main__':
    unittest.main
