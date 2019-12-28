import unittest

from common.base.box_driver import BoxDriver, BoxBrowser
from src.page.sys_main_page_zl import SysMainPage
from common.util.csv_file import CSV_File


class LoginTest(unittest.TestCase):
    """
    TC-Login: 登录测试
    """

    def setUp(self):
        """实例化BoxDriver,实例化Login，传入driver"""
        self.driver = BoxDriver(BoxBrowser.Chrome)
        self.sysMainPage = SysMainPage(self.driver)

    def tearDown(self):
        """退出浏览器，释放资源"""
        self.driver.close_browser()

    def test_login_success(self):
        """登录成功测试"""
        # 以csv文件方式读取数据
        data = CSV_File().read('data/login_user_success.csv')
        # 进入登录页面
        self.sysMainPage.enter_login()
        for list in data:
            # 读取一行数据
            username = list[0]
            password = list[1]
            casetype = list[2]
            # 将数据存入一个字典
            data = {'username': username, 'password': password, 'casetype': casetype}
            # 判断数据类型
            if (casetype == 'success'):
                '''类型1，登录成功用例'''
                # 输入用户名密码登陆
                self.sysMainPage.login(data)
                # 获取登录的用户名realname
                name = self.sysMainPage.login_success_get_name(data)
                # 断言，获取用户名与输入用户名相同，登录成功，否则登录失败
                self.assertEqual(name, username, '输入正确的用户名密码，登录失败！')
                # 签退，回到登陆页面
                self.sysMainPage.logout()

    def test_login_fail(self):
        """登录失败测试"""
        # 以csv文件方式读取数据
        data = CSV_File().read('data/login_user_fail.csv')
        # 进入登录页面
        self.sysMainPage.enter_login()
        for list in data:
            # 读取一行数据
            username = list[0]
            password = list[1]
            casetype = list[2]
            # 将数据存入一个字典
            data = {'username': username, 'password': password, 'casetype': casetype}
            # 判断数据类型
            if casetype != 'success':
                '''密码登录失败用例'''
                # 输入用户名密码登录
                self.sysMainPage.login(data)
                # 获取错误提示信息
                text = self.sysMainPage.login_fail_get_wrong_msg(data)
                # 断言，输入错误密码，登录失败
                if casetype == 'empty_name':
                    self.assertIn('登录失败', text, '用户名为空，也能登录成功！')
                elif casetype == 'wrong_name':
                    self.assertIn('登录失败', text, '用户名不存在，也能登录成功！')
                elif casetype == 'empty_password':
                    self.assertIn('登录失败', text, '密码为空，也能登录成功！')
                elif casetype == 'wrong_password':
                    self.assertIn('登录失败', text, '，密码错误，也能登录成功！')
                # 登陆失败，点击确定，返回登录页面
                self.sysMainPage.wrong_confirm()


if __name__ == '__main__':
    unittest.main()
