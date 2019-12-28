from src.page.sys_main_page import SysMainPage
from common.base.box_driver import BoxBrowser, BoxDriver
from common.util.mysql_connect import MysqlConnect
from common.base.log import Log


class SysAddUserPage(SysMainPage):
    '''
    作者：Jet
    时间：2018-05-31
    描述：ranzhi-后台管理-组织-添加成员页面
    '''

    # 后台管理按钮定位
    LOCATE_BY_XPATH_SUPERADMIN_BUTTON = 'x,//*[@id="s-menu-superadmin"]/button'
    # 后台管理框架
    LOCATE_BY_ID_SUPERADMIN_FRAME = 'id,iframe-superadmin'
    # [组织]按钮定位
    LOCATE_BY_LINK_TEXT_GROUP_BUTTON = 'l,组织'
    # [添加成员]按钮定位
    LOCATE_BY_LINK_TEXT_ADD_USER_BUTTON = 'l,添加成员'
    '''
    添加成员页面元素定位
    '''
    LOCATE_BY_ID_ACCOUNT = 'id,account'
    LOCATE_BY_ID_REALNAME = 'id,realname'
    LOCATE_BY_ID_GENDERM = 'id,genderm'
    LOCATE_BY_ID_GENDERF = 'id,genderf'
    GENDERM = 'M'
    GENDERF = 'F'
    LOCATE_BY_ID_DEPT_SELECT = 'id,dept'
    DEPT_SELECT_BY_TEXT = {'sales': '/Sales', 'tech': '/Tech'}
    LOCATE_BY_ID_ROLE_SELECT = 'id,role'
    ROLE_SELECT_BY_TEXT = {'dev': '研发', 'sales': '销售', 'tech': '技术支持'}
    LOCATE_BY_ID_PASSWORD1 = 'id,password1'
    LOCATE_BY_ID_PASSWORD2 = 'id,password2'
    LOCATE_BY_ID_EMAIL = 'id,email'
    LOCATE_BY_ID_USER_ADD_SUBMIT = 'id,submit'


    '''
    添加成员页面，错误提示语定位信息
    '''
    LOCATE_BY_ID_ACCOUNT_ERROR_INFO = 'id,accountLabel'
    LOCATE_BY_ID_REALNAME_ERROR_INFO = 'id,realnameLabel'
    LOCATE_BY_ID_PASSWORD1_ERROR_INFO = 'id,password1Label'
    LOCATE_BY_ID_EMAIL_ERROR_INFO = 'id,emailLabel'
    # 未完待续

    '''
    添加成员成功后，成员列表页面元素定位
    '''
    LOCATE_BY_XPATH_MEMBER_LIST_USERNAME = 'x,/html/body/div/div/div/div[2]/div/div/table/tbody//tr/td[3]'
    # “下一页”按钮
    LOCATE_BY_LINK_TEXT_NEXT_PAGE = 'l,下页'
    LOCATE_BY_XPATH_MEMBER_LIST_DEL_BUTTON = 'x,/html/body/div/div/div/div[2]/div/div/table/tbody/tr[%d]/td[11]/a[3]'


    '''
    连接 ranzhi 数据库相关信息
    '''
    # 在此文件中，调试if __name__ == '__main__': csv路径必须是..\\data\\**.csv
    # SQL_PATH = '..\\data\\get_mysql_table_user_account.csv'
    # 在main.py中运行，则路径为data\\**.csv
    SQL_PATH = 'src\\data\\get_mysql_table_user_account.csv'
    DATABASE = 'ranzhi'
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PWD = ''

    '''
    将上面的MySQL配置文件放到config/ranzhi.yaml中
    '''
    SQL_QUERY_ACCOUNT_FROM_SYS_USER = 'select account,gender from sys_user;'

    '''
    成员列表相关变量
    '''
    MEMBER_LIST_URL = 'http://localhost:81/ranzhi/www/sys/user-admin.html'
    # 日志保存路径
    # LOG_PATH = '..\\..\\results\\log'
    LOG_PATH = 'results\\log'

    # 实例化日志
    log = Log(LOG_PATH)
    def add_user(self, user_info):
        driver = self.base_driver
        driver.click(self.LOCATE_BY_XPATH_SUPERADMIN_BUTTON)
        self.log.info('成功点击“后台管理”按钮')
        driver.save_window_snapshot('后台管理')
        driver.forced_wait(3)
        driver.switch_to_frame(self.LOCATE_BY_ID_SUPERADMIN_FRAME)
        self.log.info('成功进入“后台管理”框架')
        driver.click(self.LOCATE_BY_LINK_TEXT_GROUP_BUTTON)
        self.log.info('成功点击“组织”按钮')
        driver.save_window_snapshot('进入“组织”')
        driver.forced_wait(2)
        # 开始点击“添加成员”按钮
        driver.click(self.LOCATE_BY_LINK_TEXT_ADD_USER_BUTTON)
        self.log.info('成功点击“新增用户”按钮')
        driver.save_window_snapshot('进入“新增用户”页面')
        driver.forced_wait(4)
        driver.type(self.LOCATE_BY_ID_ACCOUNT, user_info['account'])
        self.log.info('输入“用户名”')
        driver.type(self.LOCATE_BY_ID_REALNAME, user_info['realname'])
        self.log.info('输入“真实姓名”')
        if user_info['gender'] == self.GENDERM:
            driver.click(self.LOCATE_BY_ID_GENDERM)
            self.log.info('性别选择“男”')
        elif user_info['gender'] == self.GENDERF:
            driver.click(self.LOCATE_BY_ID_GENDERF)
            self.log.info('性别选择“女”')
        if user_info['dept'] == self.DEPT_SELECT_BY_TEXT['sales']:
            driver.select_by_visible_text(self.LOCATE_BY_ID_DEPT_SELECT, self.DEPT_SELECT_BY_TEXT['sales'])
            self.log.info('部门选择“销售”')
        # 还有很多 dept 条件选择待后续添加
        if user_info['role'] == self.ROLE_SELECT_BY_TEXT['sales']:
            driver.select_by_visible_text(self.LOCATE_BY_ID_ROLE_SELECT, self.ROLE_SELECT_BY_TEXT['sales'])
            self.log.info('角色选择“销售”')
        # 还有很多 role 条件选择待后续添加
        driver.type(self.LOCATE_BY_ID_PASSWORD1, user_info['password1'])
        self.log.info('输入密码')
        driver.type(self.LOCATE_BY_ID_PASSWORD2, user_info['password2'])
        self.log.info('再次输入密码')
        driver.type(self.LOCATE_BY_ID_EMAIL, user_info['email'])
        self.log.info('输入邮箱')
        driver.click(self.LOCATE_BY_ID_USER_ADD_SUBMIT)
        self.log.info('点击“提交”按钮')
        driver.save_window_snapshot('新增成员状态')
        driver.switch_to_default()
        self.log.info('退出“后台管理”框架')


    def get_add_user_error_info(self):
        '''
        获取添加成员页面所有字段的错误提示信息
        无效等价类，每个都单独验证
        :return: String
        '''
        driver = self.base_driver
        driver.switch_to_frame(self.LOCATE_BY_ID_SUPERADMIN_FRAME)
        self.log.info('进入框架')
        if driver.is_element_exist(self.LOCATE_BY_ID_ACCOUNT_ERROR_INFO):
            error_info = driver.get_text(self.LOCATE_BY_ID_ACCOUNT_ERROR_INFO)
        elif driver.is_element_exist(self.LOCATE_BY_ID_REALNAME_ERROR_INFO):
            error_info = driver.get_text(self.LOCATE_BY_ID_REALNAME_ERROR_INFO)
        elif driver.is_element_exist(self.LOCATE_BY_ID_PASSWORD1_ERROR_INFO):
            error_info = driver.get_text(self.LOCATE_BY_ID_PASSWORD1_ERROR_INFO)
        elif driver.is_element_exist(self.LOCATE_BY_ID_EMAIL_ERROR_INFO):
            error_info = driver.get_text(self.LOCATE_BY_ID_EMAIL_ERROR_INFO)
        else:
            raise NameError("没有您想要的错误提示信息！！！")
        driver.switch_to_default()
        self.log.info('退出框架')
        return error_info

    def del_member_list(self,expected_del_value):
        '''

        :param expected_del_value:
        :return:
        '''
        driver = self.base_driver
        self.log.info("当前页面的url为:%s"%driver.get_url())
        if driver.get_url() == self.MEMBER_LIST_URL:
            driver.del_edit_choose_the_row(self.LOCATE_BY_LINK_TEXT_NEXT_PAGE,self.LOCATE_BY_XPATH_MEMBER_LIST_USERNAME,
                                           self.LOCATE_BY_XPATH_MEMBER_LIST_DEL_BUTTON,expected_del_value)
            self.log.info("点击删除按钮，删除%s"%expected_del_value)
            driver.forced_wait(3)
            driver.accept_alert()
            self.log.info('成功点击确定删除alert!')
            driver.forced_wait(1)
            driver.switch_to_default()
        else:
            driver.click(self.LOCATE_BY_XPATH_SUPERADMIN_BUTTON)
            self.log.info('成功点击“后台管理”按钮')
            driver.save_window_snapshot('后台管理')
            driver.forced_wait(3)
            driver.switch_to_frame(self.LOCATE_BY_ID_SUPERADMIN_FRAME)
            self.log.info('成功进入“后台管理”框架')
            driver.click(self.LOCATE_BY_LINK_TEXT_GROUP_BUTTON)
            self.log.info('成功点击“组织”按钮')
            driver.save_window_snapshot('进入“组织”')
            driver.forced_wait(4)
            # 点击“删除”按钮
            driver.del_edit_choose_the_row(self.LOCATE_BY_LINK_TEXT_NEXT_PAGE,
                                           self.LOCATE_BY_XPATH_MEMBER_LIST_USERNAME,
                                           self.LOCATE_BY_XPATH_MEMBER_LIST_DEL_BUTTON, expected_del_value)
            self.log.info("点击删除按钮，删除%s" % expected_del_value)
            driver.forced_wait(5)
            driver.accept_alert()
            self.log.info('成功点击确定删除alert!')
            driver.switch_to_default()
            driver.forced_wait(2)


    def get_del_success_search_by_table_list(self, deleted_record):
        '''
        验证deleted_record这条记录是否被成功删除
        :param deleted_record: 已经被删除的记录
        :return: 布尔值（False:成功删除）
        '''
        driver = self.base_driver
        flag = driver.assert_new_add_record_exist_in_table(self.LOCATE_BY_LINK_TEXT_NEXT_PAGE,self.LOCATE_BY_XPATH_MEMBER_LIST_USERNAME,deleted_record)
        return flag


    def get_add_user_success_by_mysql_wrapper(self,expect_data):
        '''
        调用box_driver自己封装好的方法，新增记录，到数据库中进行校验
        :param expect_data: csv中的原始新增数据
        :return: 布尔值（True为数据库校验成功，False为校验失败,数据库中没有该字段）
        '''
        driver = self.base_driver
        flag = driver.get_new_record_add_success_by_mysql(self.SQL_QUERY_ACCOUNT_FROM_SYS_USER, expect_data)
        return flag

    def get_add_user_success_by_mysql_by_yaml_config(self):
        '''
        yaml，可以让“一次配置，多处调用”
        调用yaml配置的mysql,ranzhi数据库
        :return: 数组（用户名）
        '''
        sys_user_accounts_and_genders = MysqlConnect().query(self.SQL_QUERY_ACCOUNT_FROM_SYS_USER)
        self.log.info('成功连接上数据库ranzhi.sys_user')
        MysqlConnect().close()
        sys_user_accounts = []
        # 可一次性查询出数据库中多个字段，进行数据库测试断言
        # sys_user_genders = []
        for i in range(len(sys_user_accounts_and_genders)):
            sys_user_accounts.append(sys_user_accounts_and_genders[i][0])
            # sys_user_genders.append(sys_user_accounts_and_genders[i][1])
        self.log.info('成功获取到sys_user表account用户名字段值')
        # 可返回多个值
        # return sys_user_accounts,sys_user_genders
        return sys_user_accounts



    def get_add_user_success_by_mysql(self):
        '''
        获取mysql数据库'ranzhi'数据库'user'表中所有用户名'account'字段值
        :return: 返回数组类型（用户名）
        '''
        driver = self.base_driver
        mysql_user_accounts = driver.get_sql_data(self.SQL_PATH, self.MYSQL_HOST, self.MYSQL_USER, self.MYSQL_PWD,
                                                  self.DATABASE)
        self.log.info('成功连接上数据库ranzhi.sys_user')
        # 关闭数据库
        driver.close_sql()
        # print(mysql_user_accounts)
        # (('admin',), ('admin1',), ('jet',), ('user2',), ('user_1',))
        # 获取数组的长度
        # print(len(mysql_user_accounts))
        # 获取第1组元素 ('admin',)
        # print(mysql_user_accounts[0])
        user_accounts = []
        for i in range(len(mysql_user_accounts)):
            # 获取到user表中的所有用户名account字段值
            # print(mysql_user_accounts[i][0])
            # 将所有用户名添加到user_accounts数组中
            user_accounts.append(mysql_user_accounts[i][0])
        self.log.info('成功获取到ranzhi.sys_user表字段account')
        return user_accounts

    def get_add_user_success_by_member_list_pages(self,expect_new_record):
        driver = self.base_driver
        # 注意，要记得进入框架
        driver.switch_to_frame(self.LOCATE_BY_ID_SUPERADMIN_FRAME)
        self.log.info('进入“后台管理”框架')
        # 判断是否新增成功 flag是布尔值，True代表新增成功，False：失败
        flag = driver.assert_new_add_record_exist_in_table(self.LOCATE_BY_LINK_TEXT_NEXT_PAGE,self.LOCATE_BY_XPATH_MEMBER_LIST_USERNAME,expect_new_record)
        driver.save_window_snapshot('成员列表用户名')
        driver.switch_to_default()
        self.log.info('成功退出“后台管理”框架')
        return flag


    def get_add_user_success_by_member_list(self):
        '''
        获取成员列表页面所有用户名
        此方法只针对无翻页显示的table（有很大局限性）
        :return: 数组
        '''
        driver = self.base_driver
        # 注意，要记得进入框架
        driver.switch_to_frame(self.LOCATE_BY_ID_SUPERADMIN_FRAME)
        self.log.info('进入“后台管理”框架')
        # 获取成员列表页面所有用户名的值
        member_list_usernames = driver.get_text_list(self.LOCATE_BY_XPATH_MEMBER_LIST_USERNAME)
        self.log.info('成功获取到成员列表页面的所有用户名')
        driver.save_window_snapshot('成员列表用户名')
        # print(member_list_usernames)
        driver.switch_to_default()
        self.log.info('成功退出“后台管理”框架')
        return member_list_usernames








    '''
    还有 XXX XXX XXX 方法待完善
    '''


if __name__ == '__main__':
    driver = BoxDriver(BoxBrowser.Chrome)
    SysAddUserPage(driver).get_add_user_success_by_mysql()
    driver.quit()
