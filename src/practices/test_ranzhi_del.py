from common.base.box_driver import BoxDriver,BoxBrowser
from common.base.log import Log
from common.util.csv_file import CSV_File
from src.page.sys_add_user_page import SysAddUserPage
from src.page.sys_main_page import SysMainPage
import unittest

class TestRanzhiDel(unittest.TestCase):
    '''
    测试“添加用户”页面场景用例
    '''

    RANZHI_LOGIN_URL = 'http://localhost:81/ranzhi/www'
    LOGIN_USER = 'admin'
    LOGIN_PWD = 'admin'
    LOGIN_KEEP_LOGIN = True

    # 添加用户信息csv路径
    ADD_USER_CSV_PATH = 'src\\data\\add_user_fields.csv'
    # 强制等待时间
    WAIT_TIME = 3
    # 隐式等待时间
    IMPLICITYLY_WAIT_TIME = 10


    '''
    其它区域元素定位
    '''
    WAIT_TIME = 3
    # 日志保存路径
    LOG_PATH = 'results\\log'
    # 实例化日志
    log = Log(LOG_PATH)



    def setUp(self):
        self.driver = BoxDriver(BoxBrowser.Chrome)
        self.driver.implicitly_wait(self.IMPLICITYLY_WAIT_TIME)
        self.driver.navigate(self.RANZHI_LOGIN_URL)
        self.driver.maximize_window()
        self.sys_main_page = SysMainPage(self.driver)
        self.driver.forced_wait(self.WAIT_TIME)
        self.sys_main_page.select_lang(self.sys_main_page.LANG_SIMPLE_CHINESE)
        self.sys_main_page.login(self.LOGIN_USER, self.LOGIN_PWD, self.LOGIN_KEEP_LOGIN)
        self.sys_add_user_page = SysAddUserPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_del(self):
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

