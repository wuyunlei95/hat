from common.base.box_driver import BoxDriver, BoxBrowser

# 实例化类（目的：调用类(class)里面的方法(def))
# __init__ 里面有几个变量，实例化类的时候，就要加几个变量
driver = BoxDriver(BoxBrowser.Chrome)
driver.navigate("https://www.baidu.com")
driver.forced_wait(3)
driver.quit()
