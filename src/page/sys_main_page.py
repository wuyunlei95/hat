from common.base.base_page import BasePage
from common.base.log import Log

class SysMainPage(BasePage):
    '''
    作者：Jet
    时间：2018-05-31
    描述：系统主页（包括登录，以及登录后的首页
    '''

    '''
    首页登录区域元素定位
    '''
    LOCATE_BY_XPATH_LANG_SELECT = 'x,//*[@id="langs"]/button'
    LOCATE_BY_XPATH_SIMPLE_CHINESE = 'x,//*[@id="langs"]/ul/li[1]/a'
    LOCATE_BY_XPATH_TRADITIONAL_CHINESE = 'x,//*[@id="langs"]/ul/li[2]/a'
    LOCATE_BY_XPATH_ENGLISH = 'x,//*[@id="langs"]/ul/li[3]/a'
    LANG_SIMPLE_CHINESE = '简体'
    LANG_TRADITIONAL_CHINESE = '繁体'
    LANG_ENGLISH = 'English'
    ERROR_MSG_FOR_LANG = '语言选择错误！'
    LOCATE_BY_ID_LOGIN_USER = 'id,account'
    LOCATE_BY_ID_LOGIN_PWD = 'id,password'
    KEEP_LOGIN = True
    LOCATE_BY_XPATH_KEEP_LOGIN = 'x,//*[@id="keepLoginon"]'
    LOCATE_BY_ID_LOGIN_SUBMIT = 'id,submit'
    LOCATE_BY_XPATH_ERROR_MSG = 'x,/html/body/div[2]/div/div/div[1]/div'

    '''
    其它区域元素定位
    '''
    WAIT_TIME = 3

    # 日志保存路径(if __main__ 调试运行）
    # LOG_PATH = '..\\..\\results\\log'
    # main.py 主入口运行
    LOG_PATH = 'results\\log'

    # 实例化日志
    log = Log(LOG_PATH)

    def select_lang(self, lang_select):
        '''
        登录界面，语言选择
        :param lang_select: 语言选择
        :return: 无返回值
        '''
        driver = self.base_driver
        self.log.info('开始点击登录界面的语言选择')
        driver.click(self.LOCATE_BY_XPATH_LANG_SELECT)
        if lang_select == self.LANG_SIMPLE_CHINESE:
            driver.click(self.LOCATE_BY_XPATH_SIMPLE_CHINESE)
            self.log.info('成功选择简体中文')
            driver.save_window_snapshot('简体中文')
        elif lang_select == self.LANG_TRADITIONAL_CHINESE:
            driver.click(self.LOCATE_BY_XPATH_TRADITIONAL_CHINESE)
            self.log.info('成功选择繁体中文')
            driver.save_window_snapshot('繁体中文')
        elif lang_select == self.LANG_ENGLISH:
            driver.click(self.LOCATE_BY_XPATH_ENGLISH)
            self.log.info('成功选择English')
            driver.save_window_snapshot('English')
        else:
            raise NameError(self.ERROR_MSG_FOR_LANG)
        driver.forced_wait(self.WAIT_TIME)

    def login(self, user, pwd, keep_login):
        '''
        :param user: 登录的用户名
        :param pwd: 登录的密码
        :param keep_login: 是否保持登录（默认True：保持登录）
        :return: 无返回值
        '''
        driver = self.base_driver
        driver.type(self.LOCATE_BY_ID_LOGIN_USER, user)
        self.log.info('输入用户名')
        driver.type(self.LOCATE_BY_ID_LOGIN_PWD, pwd)
        self.log.info('输入密码')
        # 默认“保持登录”是没有被选中的
        if keep_login == self.KEEP_LOGIN:
            driver.click(self.LOCATE_BY_XPATH_KEEP_LOGIN)
            self.log.info('点击“保持登录”')
            driver.click(self.LOCATE_BY_ID_LOGIN_SUBMIT)
            self.log.info('点击“登录”按钮')
            driver.save_window_snapshot('登录系统')
        else:
            driver.click(self.LOCATE_BY_ID_LOGIN_SUBMIT)
            self.log.info('点击“登录”按钮')
            driver.save_window_snapshot('登录系统')
        driver.forced_wait(self.WAIT_TIME)

    '''
    其它方法
    '''

if __name__ == '__main__':
    # 代码调试用，别的人调用者里面的方法，不会被运行
    print('test debug')
