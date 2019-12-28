import unittest
from common.base.box_driver import BoxBrowser, BoxDriver
from common.base.log import Log
from src.page.sys_main_page import SysMainPage
from src.page.sys_add_user_page import SysAddUserPage
from common.util.csv_file import CSV_File


class AddUserScencesTestcast(unittest.TestCase):
    '''
    测试“添加用户”页面场景用例
    '''

    RANZHI_LOGIN_URL = 'http://localhost:81/ranzhi/www'
    LOGIN_USER = 'admin'
    LOGIN_PWD = 'admin'
    LOGIN_KEEP_LOGIN = True

    # 添加用户信息csv路径
    ADD_USER_CSV_PATH = 'src\\data\\add_user_scenes.csv'
    # 强制等待时间
    WAIT_TIME = 3
    # 隐式等待时间
    IMPLICITYLY_WAIT_TIME = 10

    # 日志保存路径
    LOG_PATH = 'results\\log'
    # 实例化日志
    log = Log(LOG_PATH)

    @classmethod
    def setUpClass(cls):
        cls.driver = BoxDriver(BoxBrowser.Chrome)
        cls.driver.implicitly_wait(cls.IMPLICITYLY_WAIT_TIME)
        cls.driver.navigate(cls.RANZHI_LOGIN_URL)
        cls.driver.maximize_window()
        cls.sys_main_page = SysMainPage(cls.driver)
        cls.driver.forced_wait(cls.WAIT_TIME)
        cls.sys_main_page.select_lang(cls.sys_main_page.LANG_SIMPLE_CHINESE)
        cls.sys_main_page.login(cls.LOGIN_USER, cls.LOGIN_PWD, cls.LOGIN_KEEP_LOGIN)
        cls.sys_add_user_page = SysAddUserPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @unittest.skip('跳过')
    def test_add_user_success_one(self):
        '''
        场景用例1： 成功添加1条记录
        :return:
        '''
        users_info = CSV_File().read_by_list(self.ADD_USER_CSV_PATH)
        for row in users_info:
            # 将每一行数据存入字典
            user_info = {'account': row[0], 'realname': row[1], 'gender': row[2], 'dept': row[3],
                         'role': row[4], 'password1': row[5], 'password2': row[6], 'email': row[7],
                         'casetype': row[8], 'error_msg': row[9]}

            if "Scene_add_one_success" in user_info['casetype']:
                self.sys_add_user_page.add_user(user_info)
                self.driver.forced_wait(self.WAIT_TIME)
                # 添加的用户名与页面成员列表中用户名比对(此方法有局限性，只针对无翻页显示的列表）
                # self.assertIn(user_info['account'], self.sys_add_user_page.get_add_user_success_by_member_list(),
                #               '成员列表页面无此新增用户名')
                # 添加的用户名与页面成员列表中用户名比对(此方法无论是否有翻页都适用！！！）
                self.assertEqual(True,self.sys_add_user_page.get_add_user_success_by_member_list_pages(user_info['account']),'成员列表页面无此新增用户名')
                # 添加的用户名与数据库中对应表ranzhi.user字段account进行比对断言
                # self.assertIn(user_info['account'], self.sys_add_user_page.get_add_user_success_by_mysql(), '数据库中无此新增用户名')
                # 使用yaml配置数据库方式，实现数据库ranzhi.user字段account与添加的用户名比对断言
                # self.assertIn(user_info['account'], self.sys_add_user_page.get_add_user_success_by_mysql_by_yaml_config(), '数据库中无此新增用户名')
                self.assertEqual(True,self.sys_add_user_page.get_add_user_success_by_mysql_wrapper(user_info['account']), '数据库中无此新增用户名')

    # @unittest.skip('跳过')
    def test_add_user_success_many_but_diff(self):
        '''
        场景用例2： 连续成功添加多条不同用户名的记录
        :return:
        '''
        users_info = CSV_File().read_by_list(self.ADD_USER_CSV_PATH)
        for row in users_info:
            user_info = {'account': row[0], 'realname': row[1], 'gender': row[2], 'dept': row[3],
                         'role': row[4], 'password1': row[5], 'password2': row[6], 'email': row[7],
                         'casetype': row[8], 'error_msg': row[9]}
            if "Scene_add_many_but_diff" in user_info['casetype']:
                self.sys_add_user_page.add_user(user_info)
                self.driver.forced_wait(self.WAIT_TIME)
                self.assertEqual(True, self.sys_add_user_page.get_add_user_success_by_member_list_pages(
                    user_info['account']), '成员列表页面无此新增用户名')
                self.assertEqual(True,
                                 self.sys_add_user_page.get_add_user_success_by_mysql_wrapper(user_info['account']),
                                 '数据库中无此新增用户名')

    @unittest.skip('跳过')
    def test_del_success(self):
        users_info = CSV_File().read_by_list(self.ADD_USER_CSV_PATH)
        for row in users_info:
            # 将每一行数据存入字典
            user_info = {'account': row[0], 'realname': row[1], 'gender': row[2], 'dept': row[3],
                         'role': row[4], 'password1': row[5], 'password2': row[6], 'email': row[7],
                         'casetype': row[8], 'error_msg': row[9]}
            self.sys_add_user_page.del_member_list(user_info['account'])
            # 成员列表中检查该用户是否被成功删除
            self.assertEqual(False, self.sys_add_user_page.get_del_success_search_by_table_list(user_info['account']))
            self.log.info('成员列表中没有该用户%s，已被成功删除！' % user_info['account'])
            # 数据库中校验，是否用户被成功删除
            self.assertEqual(True, self.sys_add_user_page.get_add_user_success_by_mysql_wrapper(user_info['account']),
                             '数据库中无此用户名，已被成功删除')




