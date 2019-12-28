from time import sleep

from common.base.box_driver import BoxDriver, BoxBrowser
class BasePage(object):
    """基础页面类，所有的页面都继承该类"""
    def __init__(self, base_driver: BoxDriver):
        """传入一个实例化的BoxDriver，保证不同的页面可以使用同一个driver"""
        self.base_driver = base_driver
if __name__ == '__main__':
    # 定义浏览器
    driver = BoxDriver(BoxBrowser.Chrome)
    # 输入富元汇网址
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
    sleep(1)
    # 进入徙木系统
    driver.click('x,//*[@id="app"]/div[1]/main/div/div/div[3]/div/div/div/img')

