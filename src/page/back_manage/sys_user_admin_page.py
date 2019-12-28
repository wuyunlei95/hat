from time import sleep

from src.page.sys_main_page_zl import SysMainPage


class SysUserAdminPage(SysMainPage):
    """后台管理主页"""
    # 后台管理按钮位置
    SUPERADMIN_BUTTON = "xpath,.//*[@id='s-menu-superadmin']/button"
    # 后台管理框体的位置
    SUPERADMIN_IFRAME = 'id,iframe-superadmin'

    def enter_module(self):
        driver = self.base_driver
        # 点击后台管理
        driver.click(self.SUPERADMIN_BUTTON)
        sleep(2)
        # 进入框体
        driver.switch_to_frame(self.SUPERADMIN_IFRAME)
