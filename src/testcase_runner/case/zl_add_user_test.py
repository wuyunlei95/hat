import unittest

from common.base.box_driver import BoxDriver, BoxBrowser
from src.page.back_manage.adduser import AddUser
from common.util.csv_file import CSV_File


class AddUserTest(unittest.TestCase):
    """
        TC-AddUser: 添加用户测试
    """

    def setUp(self):
        self.driver = BoxDriver(BoxBrowser.Chrome)
        self.addUser = AddUser(self.driver)
        # 登录
        self.addUser.enter_login()
        self.addUser.login({'username': 'admin', 'password': '123456'})
        # 进入添加成员界面
        self.addUser.enter_adduser()
        self.addUser.click_adduser()

    def tearDown(self):
        self.driver.quit()

    def test_add_user(self):
        # 读取测试数据文件add_user.csv
        datas = CSV_File().read('src/data/add_user.csv')
        for list in datas:
            # 将每一行数据存入字典
            data = {'name': list[0], 'realname': list[1], 'password1': list[2], 'password2': list[3],
                    'deptNum': list[4], 'roleNum': list[5], 'email': list[6], 'casetype': list[7]}
            # 添加用户，将字典参数传入,获取断言信息
            self.addUser.add_user(data)
            # 根据用例类型获取断言信息
            if data['casetype'] == '1':
                # 登陆成功，跳转尾页，抓取最后一页的用户名
                self.addUser.input_page_number(10000)
                self.addUser.go_to_page()
                names = self.addUser.get_page_name_list()
                text = names[names.__len__() - 1]
                self.assertEqual(list[1], text, '添加用户失败！')
            elif data['casetype'] == 'wrong_name':
                '''用户名错误用例，获取提示信息，断言'''
                name = self.addUser.get_wrong_username(data)
                self.assertIn('用户名', name, '用户名输入非法也能成功添加用户！')
            elif data['casetype'] == 'wrong_realname':
                '''真实姓名失败用例，获取提示信息'''
                realname = self.addUser.get_wrong_realname(data)
                self.assertIn('真实姓名', realname, '真实姓名非法，也能成功添加用户！')
            elif data['casetype'] == 'wrong_password':
                '''密码失败用例，获取提示信息'''
                password = self.addUser.get_wrong_password(data)
                self.assertIn('密码', password, '密码非法，也能成功添加用户！')
            elif data['casetype'] == 'wrong_email':
                email = self.addUser.get_wrong_email(data)
                self.assertIn('邮箱', email, '邮箱非法，也能成功添加用户！')
            elif data['casetype'] == 'wrong_role':
                '''角色失败用例，获取提示信息'''
                role = self.addUser.get_wrong_role(data)
                self.assertIn('角色', role, '角色为空，也能成功添加用户！')
            if data['casetype'] == '1':
                # 点击成员列表界面的添加成员按钮
                self.addUser.click_continue_adduser()
            else:
                # 点击添加成员界面的添加成员按钮
                self.addUser.click_first_adduser_button()


if __name__ == '__main__':
    unittest.main
