from src.page.sys_main_page import SysMainPage
from common.base.box_driver import BoxBrowser,BoxDriver

import unittest

class TestCookieKeepLogin(unittest.TestCase):

    def setUp(self):
        self.driver = BoxDriver(BoxBrowser.Chrome)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.navigate("http://localhost:81/ranzhi/www")
        self.sys_main_page = SysMainPage(self.driver)
        self.driver.forced_wait(2)

    def tearDown(self):
        self.driver.quit()

    def test_cookie_keep_login(self):
        self.sys_main_page.login("admin", "admin", True)
        # 遍历cookies中的name 和value信息打印
        for cookie in self.driver.get_cookies():
            print(("cookie['name']: %s  ->  cookie['value']: %s" % (cookie['name'], cookie['value'])))
        self.driver.forced_wait(2)
        self.driver.quit()

        driver = BoxDriver(BoxBrowser.Chrome)
        # 如果没有打开这个网址，直接add_cookie，则会报错：selenium.common.exceptions.WebDriverException: Message: unable to set cookie
        driver.navigate("http://localhost:81/ranzhi/www")
        # 向cookie的name 和value添加上面成功获取到的曾经会话信息（每次登录成功一次，cookie都会有新的产生）。
        # rp & rid 变化，其它的都不变
        driver.add_cookie({'name': 'keepLogin', 'value': 'on'})
        driver.add_cookie({'name': 'lang', 'value': 'zh-cn'})
        driver.add_cookie({'name': 'theme', 'value': 'default'})
        driver.add_cookie({'name': 'ra', 'value': 'admin'})
        driver.add_cookie({'name': 'rp', 'value': 'ab2af568d9e52826875f75db01aff8a7020579c2'})
        driver.add_cookie({'name': 'rid', 'value': 'fk1cj7cm47duf8gpq9fke4v5s3'})
        driver.forced_wait(4)
        # 如果不输入网址或者刷新，则不会进入登录后的页面
        driver.refresh()
        # driver.navigate("http://localhost:81/ranzhi/www")
        driver.forced_wait(2)

if __name__ == '__main__':
    unittest.main()