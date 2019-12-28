from common.base.box_driver import BoxBrowser,BoxDriver
from src.page.sys_add_user_page import SysAddUserPage
from src.page.sys_main_page import SysMainPage


driver = BoxDriver(BoxBrowser.Chrome)
driver.implicitly_wait(6)
driver.navigate("http://localhost:81/ranzhi/www")
driver.maximize_window()
sys_main_page = SysMainPage(driver)
driver.forced_wait(3)
sys_main_page.select_lang(sys_main_page.LANG_SIMPLE_CHINESE)
sys_main_page.login('admin', 'admin', True)
sys_add_user_page = SysAddUserPage(driver)

driver.click('x,//*[@id="s-menu-superadmin"]/button')
driver.switch_to_frame('id,iframe-superadmin')
driver.forced_wait(2)
driver.click('l,应用')
driver.forced_wait(2)
driver.click('l,WEB应用')
driver.forced_wait(3)


# 以下两种js方法都可滑动滚动条至底部
# js = "var action=document.documentElement.scrollTop=10000"
# js = "window.scrollTo(0,document.body.scrollHeight);"
# driver.execute_js(js)

# 使用scrollTo设置位置
js = "window.scrollTo(100,4500);"
driver.execute_js(js)

# 滚动条拖动到最顶端
driver.forced_wait(3)
js = "window.scrollTo(0,0);"
driver.execute_js(js)

# 为了点击到下面的页面未完整显示的元素
# driver.click('x,//*[@id="useapp11"]')