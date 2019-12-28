import unittest
from common.base.box_driver import BoxBrowser, BoxDriver
from common.base.log import Log
from src.page.sys_main_page import SysMainPage
from src.page.sys_add_user_page import SysAddUserPage
from common.util.csv_file import CSV_File
import paramunittest

'''
参数化 paramunittest
'''
# csv_data = CSV_File().read_by_dict('src/data/add_user_fields.csv')

# @paramunittest.parametrized(
#     *csv_data
# )

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


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def setParameters(self,**csv_data):
    #     self.csv_data = csv_data

    def test_1(self):
        print("1")

    def test_2(self):
        print("2")


if __name__ == '__main__':
    unittest.main()