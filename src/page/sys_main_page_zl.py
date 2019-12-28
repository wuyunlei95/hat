from time import sleep

from common.base.base_page import BasePage
from common.base.log import Log


class SysMainPage(BasePage):
    """系统主页面"""
    # 用户名id
    LOGIN_USER = 'id,account'
    # 密码id
    LOGIN_PWD = 'id,password'
    # 登录按钮id
    LOGIN_SUBMIT = 'id,submit'
    # 然之首页网址
    RANZHI_PAGE = 'http://localhost:81/ranzhi/www'
    # 用户名信息位置
    USER_INFOR = 'xpath,//*[@id="mainNavbar"]/div/ul[1]/li/a'
    # 签退按钮位置
    LOGOUT_BUTTON = "l,签退"
    # 登录失败，提示信息位置
    LOGIN_ERRORMSG = 'xpath,html/body/div[2]/div/div/div[1]/div'
    # 登录失败，提示框确定按钮位置
    LOGIN_FAIL_CONFIRM = 'xpath,html/body/div[2]/div/div/div[2]/button'
    # 导入自定义Log,并且设置日志路径
    log = Log('../../results/log')
    # 语言类型
    LANGUAGE_TYPE = 'x,//*[@id="langs"]/button'
    # 语言：简体，繁体，英文
    CHINESE_EASY = 'x,//*[@id="langs"]/ul/li[1]'
    CHINESE_HARD = 'x,//*[@id="langs"]/ul/li[2]'
    ENGLISH = 'x,//*[@id="langs"]/ul/li[3]'
    # 系统名称
    SYSTEM_NAME = 'x,//*[@id="login"]/div[1]/h4'
    # 语言类型
    TYPE = 'x,//*[@id="langs"]/button'
    # 用户
    USER = 'x,//*[@id="loginForm"]/form/div[2]/div[2]/table/tbody/tr[1]/th'
    # 密码
    PASSWORD = 'x,//*[@id="loginForm"]/form/div[2]/div[2]/table/tbody/tr[2]/th'
    # 登录
    LOGIN = 'i,submit'
    # 保持登录
    KEEP_LOGIN = 'x,//*[@id="loginForm"]/form/div[2]/div[2]/table/tbody/tr[3]/td/label'
    # 用户名输入提示
    USER_TIP = 'x,//*[@id="account"]'
    USER_TIP_ATTRIBUTE = 'placeholder'
    # 密码输入提示
    PASSWORD_TIP = 'i,password'
    PASSWORD_TIP_ATTRIBUTE = 'placeholder'

    def enter_login(self):
        """进入登录界面"""
        # 获取driver
        driver = self.base_driver
        # 跳转ranzhi首页
        driver.navigate(self.RANZHI_PAGE)
        # 最大化窗口
        driver.maximize_window()
        sleep(2)

    def login(self,data):
        """用户登录
        @:param data
        """
        # 获取driver
        driver = self.base_driver
        # 输入用户名，密码
        driver.type(self.LOGIN_USER, data['username'])
        driver.type(self.LOGIN_PWD, data['password'])
        # 点击登录
        driver.click(self.LOGIN_SUBMIT)
        sleep(2)

    def login_success_get_name(self, data):
        """登陆成功，获取用户名
        @:param data
        @:return name
        """
        driver = self.base_driver
        # 登录成功，获取用户名
        name = driver.get_text(self.USER_INFOR)
        self.log.info(data['username'] + '登录成功！')
        # 截屏
        driver.save_window_snapshot(data['username'] + '登录成功')
        return name

    def login_fail_get_wrong_msg(self, data):
        """登陆失败，获取错误提示信息
        @:param data
        @:return text
        """
        # 登录失败
        driver = self.base_driver
        # 获取提示框信息
        text = driver.get_text(self.LOGIN_ERRORMSG)
        # 将登录信息写入log日志,  # 截屏
        if data['username'] == '':
            self.log.info('用户名为空登录失败！')
            driver.save_window_snapshot('用户名为空登录失败')
        else:
            self.log.info(data['username'] + '登录失败!')
            driver.save_window_snapshot(data['username'] + '登录失败')
        return text

    def wrong_confirm(self):
        # 登陆失败，点击确定，返回登录页面
        self.base_driver.click(self.LOGIN_FAIL_CONFIRM)
        sleep(2)

    def logout(self):
        # 签退，重新进入登录页面
        self.base_driver.click(self.LOGOUT_BUTTON)
        sleep(3)

    def language_before_login(self, language):
        """登录之前验证语言
        @:param language
        @:return language_list
        """
        # 获取继承自BasePage的base_driver
        driver = self.base_driver
        # 点击语言类型
        driver.click(self.LANGUAGE_TYPE)
        language_list = []
        # 切换语言
        if language == 'chinese1':
            driver.click(self.CHINESE_EASY)
            sleep(1)
            language_list = self.get_lists()
            self.log.info('切换简体成功！')
            driver.save_window_snapshot('简体中文')
        elif language == 'chinese2':
            driver.click(self.CHINESE_HARD)
            sleep(1)
            language_list = self.get_lists()
            self.log.info('切换繁体成功！')
            driver.save_window_snapshot('繁体中文')
        elif language == 'english':
            driver.click(self.ENGLISH)
            sleep(1)
            language_list = self.get_lists()
            self.log.info('切换英文成功！')
            driver.save_window_snapshot('英文')
        return language_list

    def get_lists(self):
        """获取页面内容"""
        driver = self.base_driver
        # 获取模块名称
        system_name = driver.get_text(self.SYSTEM_NAME)
        # 获取语言类型
        type = driver.get_text(self.TYPE)
        # 获取用户名
        user = driver.get_text(self.USER)
        # 获取密码
        password = driver.get_text(self.PASSWORD)
        # 获取登录按钮文本
        login = driver.get_text(self.LOGIN)
        # 获取保持登录文本
        keep_login = driver.get_text(self.KEEP_LOGIN)
        # 获取用户名提示文本
        user_tip = driver.get_attribute(self.USER_TIP, self.USER_TIP_ATTRIBUTE)
        # 获取密码提示文本
        password_tip = driver.get_attribute(self.PASSWORD_TIP, self.PASSWORD_TIP_ATTRIBUTE)
        # 把文本信息放入list
        language_list = [system_name, type, user, password, login, keep_login, user_tip, password_tip]
        return language_list

    # 我的地盘
    MY_PLACE = 'i,s-menu-dashboard'
    # 客户管理
    CRM = 'i,s-menu-1'
    CRM_IFRAME = 'i,iframe-1'
    # 日常办公
    OA = 'i,s-menu-2'
    OA_IFRAME = 'i,iframe-2'
    # 项目
    PROJ = 'i,s-menu-3'
    PROJ_IFRAME = 'i,iframe-3'
    # 我的文档
    DOC = 'i,s-menu-4'
    DOC_IFRAME = 'i,iframe-4'
    # 现金记账
    CASH = 'i,s-menu-5'
    CASH_IFRAME = 'i,iframe-5'
    # 团队
    TEAM = 'i,s-menu-6'
    TEAM_IFRAME = 'i,iframe-6'
    # 后台管理
    BACK_MANAGE = 'i,s-menu-superadmin'
    BACK_MANAGE_IFRAME = 'i,iframe-superadmin'
    # 标题定位
    # 我的地盘标题定位
    TITLE_FIRST_MY = 'x,//*[@id="mainNavbar"]/div/ul[1]/li/a'
    # 我的标题标题内容定位
    TITLE_REST_MY = 'x,//*[@id="mainNavbar"]/div/ul[2]/li/a'
    # 其他模块标题定位
    TITLE_FIRST = 'x,//*[@id="mainNavbar"]/div/a'
    # 其他模块标题内容定位
    TITLE_REST = 'x,//*[@id="mainNavbar"]/ul/li/a'
    # 左侧底部按钮用户功能按钮
    START = 'i,start'
    # 当前语言
    CURRENT_LANGUAGE = 'x,//*[@id="startMenu"]/li[3]/a'
    # 顶部模块地址
    TOP_MODULE = 'x,/html/body/div[1]/div[1]/ul/li[3]/a'

    def click_module(self, module):
        """点击模块，获取模块标题内容
        @:param module
        @:return title_rest
        """
        driver = self.base_driver
        # 点击模块，进入iframe
        if module == 'MY_PLACE':
            driver.click(self.MY_PLACE)
            sleep(2)
            # 日志，截图
            self.log.info('成功进入我的地盘模块')
            driver.save_window_snapshot("我的地盘")
        elif module == 'CRM':
            driver.click(self.CRM)
            sleep(2)
            # 日志，截图
            self.log.info('成功进入客户管理模块')
            driver.save_window_snapshot("客户管理")
        elif module == 'OA':
            driver.click(self.OA)
            sleep(2)
            # 日志，截图
            self.log.info('成功进入日常办公模块')
            driver.save_window_snapshot("日常办公")
        elif module == 'PROJ':
            driver.click(self.PROJ)
            sleep(2)
            # 日志，截图
            self.log.info('成功进入项目模块')
            driver.save_window_snapshot("项目")
        elif module == 'DOC':
            driver.click(self.DOC)
            sleep(2)
            # 日志，截图
            self.log.info('成功进入文档模块')
            driver.save_window_snapshot("文档")
        elif module == 'CASH':
            driver.click(self.CASH)
            sleep(2)
            # 日志，截图
            self.log.info('成功进入现金记账模块')
            driver.save_window_snapshot("现金记账")
        elif module == 'TEAM':
            driver.click(self.TEAM)
            sleep(2)
            # 日志，截图
            self.log.info('成功进入团队模块')
            driver.save_window_snapshot("团队")
        elif module == 'BACK_MANAGE':
            driver.click(self.BACK_MANAGE)
            sleep(2)
            # 日志，截图
            self.log.info('成功进入后台管理模块')
            driver.save_window_snapshot("后台管理")
        else:
            raise NameError('输入模块不存在！！')

    def enter_iframe(self, module):
        """进入模块窗体"""
        driver = self.base_driver
        if module == 'MY_PLACE':
            pass
        elif module == 'CRM':
            driver.switch_to_frame(self.CRM_IFRAME)
        elif module == 'OA':
            driver.switch_to_frame(self.OA_IFRAME)
        elif module == 'PROJ':
            driver.switch_to_frame(self.PROJ_IFRAME)
        elif module == 'DOC':
            driver.switch_to_frame(self.DOC_IFRAME)
        elif module == 'CASH':
            driver.switch_to_frame(self.CASH_IFRAME)
        elif module == 'TEAM':
            driver.switch_to_frame(self.TEAM_IFRAME)
        elif module == 'BACK_MANAGE':
            driver.switch_to_frame(self.BACK_MANAGE_IFRAME)
        else:
            raise NameError('输入模块不存在！！')

    def get_module_title(self, module):
        """获取模块标题"""
        driver = self.base_driver
        title_first = ''
        title_rest = []
        # 获取模块标题，内容文本信息
        if module == 'MY_PLACE':
            title_first = driver.get_text(self.TITLE_FIRST_MY)
            title_rest = driver.get_text_list(self.TITLE_REST_MY)
        else:
            title_first = driver.get_text(self.TITLE_FIRST)
            title_rest = driver.get_text_list(self.TITLE_REST)
        # 拼接标题和内容
        title_rest.insert(0, title_first)
        return title_rest

    def switch_out_iframe(self):
        """退出窗体"""
        # 退出iframe
        self.base_driver.switch_to_default()

    def click_left_buttom_user(self):
        """点击左侧底部用户功能按钮"""
        self.base_driver.click(self.START)
        sleep(1)

    def get_current_language(self):
        text = self.base_driver.get_text(self.CURRENT_LANGUAGE)
        return text

    def click_current_language(self):
        """点击当前语言"""
        self.base_driver.click(self.CURRENT_LANGUAGE)
        sleep(1)

    def choose_language(self, language):
        """选择语言
        @:param language('简体','繁体','english')
        """
        text = self.base_driver.get_text(self.CURRENT_LANGUAGE)
        self.base_driver.click('l,%s' % language)
        sleep(2)
        # 日志，截图
        self.log.info('登陆后切换%s成功！' % language)
        self.base_driver.save_window_snapshot('登陆后切换%s' % language)

    def get_myplace_title_language(self):
        # 获取顶部信息，看是否以对应的语言显示
        top_texts = self.base_driver.get_text_list(self.TOP_MODULE)
        return top_texts
