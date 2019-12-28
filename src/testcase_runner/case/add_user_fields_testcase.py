import unittest
from common.base.box_driver import BoxBrowser, BoxDriver
from common.base.log import Log
from src.page.sys_main_page import SysMainPage
from src.page.sys_add_user_page import SysAddUserPage
from common.util.csv_file import CSV_File
import paramunittest

'''
参数化 paramun ittest
'''
csv_data = CSV_File().read_by_dict('src/data/add_user_fields.csv')

@paramunittest.parametrized(
    *csv_data
)

class AddUserFieldsTestcast(unittest.TestCase):
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
    WAIT_TIME = 2
    # 隐式等待时间
    IMPLICITYLY_WAIT_TIME = 10

    # 日志保存路径
    LOG_PATH = 'results\\log'
    # 实例化日志
    log = Log(LOG_PATH)

    @classmethod
    def setUpClass(cls):
        # Pycharm：查找并替换 快捷键  Ctrl + r
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

    def setParameters(self, **csv_data):
        self.csv_data = csv_data

    def test_add_user_failure(self):
        row = self.csv_data
        # 将每一行数据存入字典
        user_info = {'account': row['account'], 'realname': row['realname'], 'gender': row['gender'], 'dept': row['dept'],
                     'role': row['role'], 'password1': row['password1'], 'password2': row['password2'], 'email': row['email'],
                     'casetype': row['casetype'], 'error_msg': row['error_msg']}

        self.sys_add_user_page.add_user(user_info)
        self.driver.forced_wait(self.WAIT_TIME)
        add_user_error_info = self.sys_add_user_page.get_add_user_error_info()

        # 断言，待续
        if 'account_Null' in user_info['casetype']:
            self.assertEqual(user_info['error_msg'],add_user_error_info,"用户名为空，错误提示信息有问题！")
            self.log.info('[用户名]为空，错误提示信息正确！')
        elif 'realname_Null' in user_info['casetype']:
            self.assertEqual(user_info['error_msg'], add_user_error_info, "真实姓名为空，错误提示信息有问题！")
            self.log.info('[真实姓名]为空，错误提示信息正确！')
        elif 'password1_Null' in user_info['casetype']:
            self.assertEqual(user_info['error_msg'], add_user_error_info, "密码为空，错误提示信息有问题！")
            self.log.info('[密码]为空，错误提示信息正确！')
        elif 'email_Null' in user_info['casetype']:
            self.assertEqual(user_info['error_msg'], add_user_error_info, "邮箱为空，错误提示信息有问题！")
            self.log.info('[邮箱]为空，错误提示信息正确！')
        else:
            self.log.info('所有字段用例执行完毕！！！')
