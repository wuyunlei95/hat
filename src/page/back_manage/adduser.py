from time import sleep

from common.base.log import Log
from src.page.back_manage.sys_user_admin_page import SysUserAdminPage


class AddUser(SysUserAdminPage):
    # 后台管理界面，添加成员位置
    ADDUSER_BUTTON = "x,.//*[@id='shortcutBox']/div/div[1]/div/a/h3"
    # 添加成功后，添加成员位置
    CONTINUE_ADDUSER = "x,html/body/div[1]/div/div/div[1]/div/div[2]/a[1]"
    # 第一次进入添加用户界面，添加成员的位置
    FIRST_ADDUSER = "x,/html/body/div/div/div[1]/div/div[2]/a[1]"
    # 添加用户信息
    ACCOUNT = 'i,account'
    REALNAME = 'i,realname'
    PW1 = 'i,password1'
    PW2 = 'i,password2'
    MALE = 'i,genderm'
    FEMALE = 'i,genderf'
    DEPT = 'i,dept'
    ROLE = 'i,role'
    EMAIL = 'i,email'
    SUBMIT = 'i,submit'
    # 输入页面数字的路径
    PAGE_INPUT = 'i,_pageID'
    # 跳转页面的路径
    PAGE_GOTO = 'i,goto'
    # 获取页面用户名集合的xpath路径
    NAMELIST_XPATH = 'x,html/body/div[1]/div/div/div[2]/div/div/table/tbody/tr/td[2]'
    # 添加用户失败，提示信息路径
    ACCOUNT_ERROR = 'i,accountLabel'
    REALNAME_ERROR = 'i,realnameLabel'
    PASSWORD_ERROR = 'i,password1Label'
    EMAIL_ERROR = 'i,emailLabel'
    ROLE_ERROR = 'i,roleLabel'
    log = Log('log')

    def enter_adduser(self):
        """进入添加用户界面"""
        driver = self.base_driver
        self.enter_module()

    def click_adduser(self):
        """点击添加成员"""
        self.base_driver.click(self.ADDUSER_BUTTON)
        sleep(2)

    def click_continue_adduser(self):
        """成员列表界面，点击添加成员按钮"""
        self.base_driver.click(self.CONTINUE_ADDUSER)
        sleep(2)

    def click_first_adduser_button(self):
        """添加成员界面，点击添加成员按钮"""
        self.base_driver.click(self.FIRST_ADDUSER)
        sleep(2)

    def add_user(self, data):
        """添加用户
        @:param data
        """
        # 传入driver
        driver = self.base_driver
        # 将data中的deptNum
        deptNum = int(data['deptNum'])
        # 输入用户名
        driver.type(self.ACCOUNT, data['name'])
        # 输入用户真实姓名
        driver.type(self.REALNAME, data['realname'])
        # 输入密码
        driver.type(self.PW1, data['password1'])
        driver.type(self.PW2, data['password2'])
        # 选择性别
        if (deptNum / 2 == 1):
            driver.click(self.MALE)
        else:
            driver.click(self.FEMALE)
        # 选择部门
        driver.select_by_index(self.DEPT, deptNum)
        # 选择角色
        # 如果roleNum不为空或者NULL,将其转为数字
        if data['roleNum'] != '' or data['roleNum'] is None:
            roleNum = int(data['roleNum'])
            driver.select_by_index(self.ROLE, roleNum)
        # 输入邮箱
        driver.type(self.EMAIL, data['email'])
        # 点击保存
        driver.click(self.SUBMIT)
        sleep(2)

    def input_page_number(self, num):
        """输入页面"""
        self.base_driver.type(self.PAGE_INPUT, 1000000)
        sleep(1)

    def go_to_page(self):
        """点击跳转"""
        self.base_driver.click(self.PAGE_GOTO)
        sleep(2)

    def get_page_name_list(self):
        """获取当前页面的用户名"""
        names = self.base_driver.get_text_list(self.NAMELIST_XPATH)
        return names

    def get_wrong_username(self, data):
        '''用户名错误用例，获取提示信息'''
        driver = self.base_driver
        text = driver.get_text(self.ACCOUNT_ERROR)
        # 将添加用户信息写入日志
        self.log.info(data['realname'] + '添加失败！')
        # 获取截屏图片
        driver.save_window_snapshot(data['realname'] + '添加失败')
        return text

    def get_wrong_realname(self, data):
        '''真实姓名失败用例，获取提示信息'''
        driver = self.base_driver
        text = driver.get_text(self.REALNAME_ERROR)
        # 将添加用户信息写入日志
        self.log.info(data['realname'] + '添加失败！')
        # 获取截屏图片
        driver.save_window_snapshot(data['realname'] + '添加失败')
        return text

    def get_wrong_password(self, data):
        driver = self.base_driver
        '''密码失败用例，获取提示信息'''
        text = driver.get_text(self.PASSWORD_ERROR)
        # 将添加用户信息写入日志
        self.log.info(data['realname'] + '添加失败！')
        # 获取截屏图片
        driver.save_window_snapshot(data['realname'] + '添加失败')
        return text

    def get_wrong_email(self, data):
        driver = self.base_driver
        '''邮箱失败用例，获取提示信息'''
        text = driver.get_text(self.EMAIL_ERROR)
        # 将添加用户信息写入日志
        self.log.info(data['realname'] + '添加失败！')
        # 获取截屏图片
        driver.save_window_snapshot(data['realname'] + '添加失败')
        return text

    def get_wrong_role(self, data):
        driver = self.base_driver
        '''角色失败用例，获取提示信息'''
        text = driver.get_text(self.ROLE_ERROR)
        # 将添加用户信息写入日志
        self.log.info(data['realname'] + '添加失败！')
        # 获取截屏图片
        driver.save_window_snapshot(data['realname'] + '添加失败')
        return text
