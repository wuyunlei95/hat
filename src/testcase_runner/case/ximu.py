import time
import unittest
from asyncio import sleep

from common.base.box_driver import BoxDriver, BoxBrowser



class LanguageTest(unittest.TestCase):
    """
        TC-Language: 语言测试
    """

    def setUp(self):

        self.driver = BoxDriver(BoxBrowser.Chrome)

    def tearDown(self):
        # pass
        sleep(5)
        self.driver.quit()

    def test_ximu(self):
        driver = self.driver
        driver.navigate('http://ximu.sit.fjf.com/')

        # 最大化窗口
        driver.maximize_window()
        # 输入账号
        driver.type('x,//*[@id="app"]/div[2]/div/form/div[1]/div/div/input', "13888888888")
        # 输入密码
        driver.type('x,//*[@id="app"]/div[2]/div/form/div[2]/div/div[1]/input', "123456")
        # 输入验证码
        driver.type('x,//*[@id="app"]/div[2]/div/form/div[3]/div[1]/div/div/div/input', "123456")
        sleep(2)
        driver.click('x,//*[@id="app"]/div[2]/div/form/div[4]/div/button[1]/span')
        sleep(2)
        # 进入徙木系统
        driver.click('x,//*[@id="app"]/div[1]/main/div/div/div[3]/div/div/div/img')
        sleep(5)


if __name__ == '__main__':
    # main是错的，要main()
    # unittest.main
    unittest.main()
