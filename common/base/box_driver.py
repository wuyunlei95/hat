import time
from enum import Enum, unique

import pymysql
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from common.base.log import Log
from common.util.mysql_connect import MysqlConnect


@unique
class BoxBrowser(Enum):
    """
    定义支持的浏览器，支持Chrome，Firefox，Ie
    """
    Chrome = 0
    Firefox = 1
    Ie = 2


class BoxDriver(object):
    """
    a simple demo of selenium framework tool
    """
    """
    日志记录
    """
    # 日志保存路径
    LOG_PATH = 'results\\log'
    # 实例化日志
    log = Log(LOG_PATH)

    """
    私有全局变量
    """
    _base_driver = None
    _by_char = None

    """
    构造方法
    """

    def __init__(self, browser_type=0, by_char=",", profile=None):
        """
        构造方法：实例化 BoxDriver 时候使用
        :param browser_type: 浏览器类型
        :param by_char: 分隔符，默认使用","
        :param profile:
            可选择的参数，如果不传递，就是None
            如果传递一个 profile，就会按照预先的设定启动火狐
            去掉遮挡元素的提示框等
        """
        self._by_char = by_char
        if browser_type == BoxBrowser.Chrome:
            profile = webdriver.ChromeOptions()
            profile.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            driver = webdriver.Chrome(chrome_options=profile)

        elif browser_type == BoxBrowser.Firefox:
            if profile is not None:
                profile = FirefoxProfile(profile)

            driver = webdriver.Firefox(firefox_profile=profile)

        elif browser_type == BoxBrowser.Ie:
            driver = webdriver.Ie()
        else:
            driver = webdriver.PhantomJS()
        try:
            self._base_driver = driver
            self._by_char = by_char
        except Exception:
            raise NameError("Browser %s Not Found! " % browser_type)

    """
    私有方法
    """

    def _convert_selector_to_locator(self, selector):
        """
        转换自定义的 selector 为 Selenium 支持的 locator
        :param selector: 定位字符，字符串类型，"i, xxx"
        :return: locator
        """
        if self._by_char not in selector:
            return By.ID, selector

        selector_by = selector.split(self._by_char)[0].strip()
        selector_value = selector.split(self._by_char)[1].strip()
        if selector_by == "i" or selector_by == 'id':
            locator = (By.ID, selector_value)
        elif selector_by == "n" or selector_by == 'name':
            locator = (By.NAME, selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            locator = (By.CLASS_NAME, selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            locator = (By.LINK_TEXT, selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            locator = (By.TAG_NAME, selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            locator = (By.XPATH, selector_value)
        elif selector_by == "s" or selector_by == 'css_selector':
            locator = (By.CSS_SELECTOR, selector_value)
        else:
            raise NameError("Please enter a valid selector of targeting elements.")

        return locator

    def _locate_element(self, selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        locator = self._convert_selector_to_locator(selector)
        if locator is not None:
            element = self._base_driver.find_element(*locator)
        else:
            raise NameError("Please enter a valid locator of targeting elements.")

        return element

    def _locate_elements(self, selector):
        """
        to locate element by selector
        :arg
        selector should be passed by an example with "i,xxx"
        "x,//*[@id='langs']/button"
        :returns
        DOM element
        """
        locator = self._convert_selector_to_locator(selector)
        if locator is not None:
            elements = self._base_driver.find_elements(*locator)
        else:
            raise NameError("Please enter a valid locator of targeting elements.")

        return elements

    """
    cookie 相关方法
    """

    def get_cookies(self):
        '''
        获取所有cookie信息
        :return:
        '''
        return self._base_driver.get_cookies()

    def clear_cookies(self):
        """
        clear all cookies after driver init
        """
        self._base_driver.delete_all_cookies()

    def add_cookies(self, cookies):
        """
        Add cookie by dict
        :param cookies:
        :return:
        """
        self._base_driver.add_cookie(cookie_dict=cookies)

    def add_cookie(self, cookie_dict):
        """
        Add single cookie by dict
        添加 单个 cookie
        如果该 cookie 已经存在，就先删除后，再添加
        :param cookie_dict: 字典类型，有两个key：name 和 value
        :return:
        """
        cookie_name = cookie_dict["name"]
        cookie_value = self._base_driver.get_cookie(cookie_name)
        if cookie_value is not None:
            self._base_driver.delete_cookie(cookie_name)

        self._base_driver.add_cookie(cookie_dict)

    def remove_cookie(self, name):
        """
        移除指定 name 的cookie
        :param name: 
        :return: 
        """
        # 检查 cookie 是否存在，存在就移除
        old_cookie_value = self._base_driver.get_cookie(name)
        if old_cookie_value is not None:
            self._base_driver.delete_cookie(name)

    """
    浏览器本身相关方法
    """

    def refresh(self, url=None):
        """
        刷新页面
        如果 url 是空值，就刷新当前页面，否则就刷新指定页面
        :param url: 默认值是空的
        :return:
        """
        if url is None:
            self._base_driver.refresh()
        else:
            self._base_driver.get(url)

    def maximize_window(self):
        """
        最大化当前浏览器的窗口
        :return:
        """
        self._base_driver.maximize_window()

    def navigate(self, url):
        """
        打开 URL
        :param url:
        :return:
        """
        self._base_driver.get(url)

    def quit(self):
        """
        退出驱动
        :return:
        """
        self._base_driver.quit()

    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self._base_driver.close()

    """
    基本元素相关方法
    """

    def type(self, selector, text):
        """
        Operation input box.

        Usage:
        driver.type("i,el","selenium")
        """
        el = self._locate_element(selector)
        el.clear()
        el.send_keys(text)



    def type_enter(self, selector, string):
        '''
        回车
        :param selector: 定位元素
        :param string:
        :return:
        '''
        self._locate_element(selector).clear()
        self._locate_element(selector).send_keys(string + Keys.ENTER)

    def click(self, selector):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("i,el")
        """
        el = self._locate_element(selector)
        el.click()

    def click_by_enter(self, selector):
        """
        It can type any text / image can be located  with ENTER key

        Usage:
        driver.click_by_enter("i,el")
        """
        el = self._locate_element(selector)
        el.send_keys(Keys.ENTER)

    def click_by_text(self, text):
        """
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        """
        self._locate_element('p,' + text).click()

    def submit(self, selector):
        """
        Submit the specified form.

        Usage:
        driver.submit("i,el")
        """
        el = self._locate_element(selector)
        el.submit()

    def move_to(self, selector):
        """
        to move mouse pointer to selector
        :param selector:
        :return:
        """
        el = self._locate_element(selector)
        ActionChains(self._base_driver).move_to_element(el).perform()

    def right_click(self, selector):
        """
        to click the selector by the right button of mouse
        :param selector:
        :return:
        """
        el = self._locate_element(selector)
        ActionChains(self._base_driver).context_click(el).perform()

    def count_elements(self, selector):
        """
        数一下元素的个数
        :param selector: 定位符
        :return:
        """
        els = self._locate_elements(selector)
        return len(els)

    def drag_element(self, source, target):
        """
        拖拽元素
        :param source:
        :param target:
        :return:
        """

        el_source = self._locate_element(source)
        el_target = self._locate_element(target)

        if self._base_driver.w3c:
            ActionChains(self._base_driver).drag_and_drop(el_source, el_target).perform()
        else:
            ActionChains(self._base_driver).click_and_hold(el_source).perform()
            ActionChains(self._base_driver).move_to_element(el_target).perform()
            ActionChains(self._base_driver).release(el_target).perform()

    def lost_focus(self):
        """
        当前元素丢失焦点
        :return:
        """
        ActionChains(self._base_driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()

    """
    <select> 元素相关
    """

    def select_by_index(self, selector, index):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self._locate_element(selector)
        Select(el).select_by_index(index)

    def get_selected_text(self, selector):
        """
        获取 Select 元素的选择的内容
        :param selector: 选择字符 "i, xxx"
        :return: 字符串
        """
        el = self._locate_element(selector)
        selected_opt = Select(el).first_selected_option()
        return selected_opt.text

    def select_by_visible_text(self, selector, text):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self._locate_element(selector)
        Select(el).select_by_visible_text(text)

    def select_by_value(self, selector, value):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self._locate_element(selector)
        Select(el).select_by_value(value)

    """
    JavaScript 相关
    """

    def execute_js(self, script):
        """
        Execute JavaScript scripts.
        滑动滚动条

        Usage:
        # 使用scrollTop滑动到底部
        js = "var action=document.documentElement.scrollTop=10000"
        driver.execute_js(js)

        # 使用scrollTo滑动到指定位置
        js = "window.scrollTo(100,4500);"
        driver.execute_script(js)

        # scrollTo活动到最顶端
        js = "window.scrollTo(0,0);"

        第1个数字：X坐标（横坐标）
        第2个数字：Y坐标（纵坐标）
        """
        self._base_driver.execute_script(script)

    """
    元素属性相关方法
    """

    def get_value(self, selector):
        """
        返回元素的 value
        :param selector: 定位字符串
        :return:
        """
        el = self._locate_element(selector)
        return el.get_attribute("value")

    def get_attribute(self, selector, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("i,el","type")
        """
        el = self._locate_element(selector)
        return el.get_attribute(attribute)

    def get_attributes(self, selector, attribute):
        """获取一组元素的属性值"""
        eles = self._locate_elements(selector)
        list = []
        for ele in eles:
            list.append(ele.get_attribute(attribute))
        return list

    def get_text(self, selector):
        """
        Get element text information.

        Usage:
        driver.get_text("i,el")
        """
        el = self._locate_element(selector)
        return el.text

    def get_displayed(self, selector):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("i,el")
        """
        el = self._locate_element(selector)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self._base_driver.title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self._base_driver.current_url

    def get_selected(self, selector):
        """
        to return the selected status of an WebElement
        :param selector: selector to locate
        :return: True False
        """
        el = self._locate_element(selector)
        return el.is_selected()

    def get_text_list(self, selector):
        """
        根据selector 获取多个元素，取得元素的text 列表
        :param selector:
        :return: list
        """

        el_list = self._locate_elements(selector)
        results = []
        for el in el_list:
            results.append(el.text)

        return results

    """
    窗口相关方法
    """

    def accept_alert(self):
        '''
            Accept warning box.

            Usage:
            driver.accept_alert()
            '''
        self._base_driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismissAlert()
        '''
        self._base_driver.switch_to.alert.dismiss()

    def switch_to_frame(self, selector):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("i,el")
        """
        el = self._locate_element(selector)
        self._base_driver.switch_to.frame(el)

    def switch_to_default(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self._base_driver.switch_to.default_content()

    def switch_to_window_by_title(self, title):
        for handle in self._base_driver.window_handles:
            self._base_driver.switch_to.window(handle)
            if self._base_driver.title == title:
                break

            self._base_driver.switch_to.default_content()

    def open_new_window(self, selector):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''
        original_windows = self._base_driver.current_window_handle
        el = self._locate_element(selector)
        el.click()
        all_handles = self._base_driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self._base_driver._switch_to.window(handle)

    def save_window_snapshot(self, file_name):
        """
        save screen snapshot
        :param file_name: the image file name and path
        :return:
        """
        driver = self._base_driver
        file_name = 'results/screenshot/%s_%s.png' % (time.strftime('%Y-%m-%d_%H-%M-%S'), file_name)
        driver.save_screenshot(file_name)

    """
    等待方法
    """

    def forced_wait(self, seconds):
        """
        强制等待
        :param seconds:
        :return:
        """
        time.sleep(seconds)

    def implicitly_wait(self, seconds):
        """
        Implicitly wait. All elements on the page.
        :param seconds 等待时间 秒
        隐式等待

        Usage:
        driver.implicitly_wait(10)
        """
        self._base_driver.implicitly_wait(seconds)

    def explicitly_wait(self, selector, seconds):
        """
        显式等待
        :param selector: 定位字符
        :param seconds: 最长等待时间，秒
        :return:
        """
        locator = self._convert_selector_to_locator(selector)

        WebDriverWait(self._base_driver, seconds).until(expected_conditions.presence_of_element_located(locator))

    def get_sql_data(self, sqlfile_path, ip, user, pwd, database):
        # 读取sql数据
        self.sql_file = open(sqlfile_path, mode="r", encoding="utf8")
        # 仅读到sql语句，还没读取到数据
        sql_scripts = self.sql_file.read()
        # 连接数据库，要选择cmd模式下用命令导入pymysql包，pip install pymysql
        # 数据库所在机器的地址
        self.mysql_connect = pymysql.connect(host=ip, user=user, password=pwd,
                                             db=database, port=3306, charset="utf8")
        # 创建游标并读取数据库数据
        self.mysql_cursor = self.mysql_connect.cursor()
        # 执行sql语句
        self.mysql_cursor.execute(sql_scripts)
        # 接收全部的返回结果行
        mysql_data = self.mysql_cursor.fetchall()
        return mysql_data

    def close_sql(self):
        # 关闭sql文件和连接
        self.sql_file.close()
        self.mysql_connect.close()
        self.mysql_cursor.close()

    def get_screenshot(self, path):
        '''
        获取截图
        :param path: 
        :return: 
        '''
        self._base_driver.get_screenshot_as_file(
            '%s/%s.png' % (path, time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))))

    def is_element_enabled(self,selector):
        '''
        判断页面元素是否可点击
        :param selector: 元素定位
        :return: 布尔值
        '''
        if self._locate_element(selector).is_enabled():
            return True
        else:
            return False

    def is_element_selected(self,selector):
        '''
        判断页面元素是否已被选中
        :param selector: 元素定位
        :return: 布尔值
        '''
        if self._locate_element(selector).is_selected():
            return True
        else:
            return False

    def is_element_displayed(self,selector):
        '''
        比如，点击“请登录”，需要判断一下这个弹出框到底弹了没有，这样就需要判断某个元素是否存在，使用is_displayed函数只能用于该元素存在去判断此元素是否出现，而不能判断某个元素是否存在
        :param selector: 元素定位
        :return: 布尔值
        '''
        if self._locate_element(selector).is_displayed():
            return True
        else:
            return False


    def is_element_exist(self, selector):
        '''
        该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
        :param self:
        :param selector: 元素定位，如'id,account'
        :return: 布尔值
        '''
        flag = True
        try:
            self._locate_element(selector)
            return flag
        except:
            flag = False
            return flag

    def del_edit_choose_the_row(self, selector_of_next_page, selector_of_tds,selector_of_del_edit_choose,expected_td_value):
        '''
        页面表单，选中/编辑/删除 指定内容的行
        :param selector_of_tds: 所有列的定位，如：'x,/html/body/div/div[2]/div/div[1]/div/table/tbody//tr/td[2]'
        :param selector_of_del_edit_choose: 指定要操作的列，如：'x,/html/body/div/div[2]/div/div[1]/div/table/tbody/tr[%d]/td[10]/a[2]'
        :param selector_of_next_page: 下一页定位，如：'l,下页'
        :param expected_td_value: 期望的列内容
        :return:无
        '''
        # 两种打印List的方法，都是可以的
        # （1）
        # list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # for i in range(len(list)):
        #     print(list[i])
        # （2）
        # list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # for i in list:
        #     print(i)

        td_values = self.get_text_list(selector_of_tds)
        for i in range(len(td_values)):
            if td_values[i] == expected_td_value:
                self.log.info('%s在第%d行显示1' % (td_values[i], i + 1))
                self.forced_wait(3)
                self.click(selector_of_del_edit_choose %(i + 1))
                break
        try:
            while (self.is_element_enabled(selector_of_next_page)):
                self.click(selector_of_next_page)
                self.forced_wait(2)
                td_values = self.get_text_list(selector_of_tds)
                for i in range(len(td_values)):
                    if td_values[i] == expected_td_value:
                        self.log.info('%s在第%d行显示N' % (td_values[i], i + 1))
                        self.forced_wait(3)
                        self.click(selector_of_del_edit_choose % (i + 1))
                continue
        except Exception as e:
            self.log.error('%s处理OK！'%expected_td_value)


    def assert_new_add_record_exist_in_table(self,selector_of_next_page,selector_of_real_records,expect_new_record):
        '''
        此方法针对页面列表（无论是否有翻页），都可以判断新增记录是否添加成功！
        若新增成功，则返回 True 布尔值；否则返回 False 布尔值
        :param selector_of_next_page: 网页列表中“下一页”元素定位
        :param selector_of_real_record: 网页列表中想要断言的td记录的元素定位（建议：xpath方式）
        :param expect_new_record: 期待的新增记录（csv中的原始数据）
        :return: 布尔值
        '''
        # first_count_per_page = self.count_elements(selector_of_real_record)
        # print('当前设置为每页显示 %s 条记录' % first_count_per_page)
        real_records = self.get_text_list(selector_of_real_records)
        for real_record in real_records:
            if real_record == expect_new_record:
                # self.log.info('记录新增成功！新增记录 %s 在第一页就被找到！'%expect_new_record)
                return True
        # count_per_page_whiles = 0
        try:
            while(self.is_element_enabled(selector_of_next_page)):
                self.click(selector_of_next_page)
                self.forced_wait(2)
                # count_per_page_while = driver.count_elements("x,//tbody//tr/td[2]")
                # count_per_page_whiles += count_per_page_while
                next_page_real_records = self.get_text_list(selector_of_real_records)
                for next_page_real_record in next_page_real_records:
                    if next_page_real_record == expect_new_record:
                        # self.log.info('记录新增成功！新增记录 %s 不是在第一页被找到！'%expect_new_record)
                        return True
                continue

        except Exception as e:
            # count_page_real_show = count_per_page_whiles + first_count_per_page
            # print("页面实际显示记录条数：%s" % count_page_real_show)
            # 页面统计总数 VS 页面实际显示记录总数
            # assert count_page_real_show == int(total_num)
            # print("‘页面实际显示记录总数’ 与 ‘页面统计显示记录总数’ 相同！")
            # self.log.error('新增记录 %s 在列表中没有被找到！'%expect_new_record)
            return False

    def get_new_record_add_success_by_mysql(self, expert_sql, expect_data):
        """
        新增记录，与数据库比对校验
        :param sql: SQL语句（第一个字段为与expect_data对比的数据库字段）
        :param expect_data: 将要比对的字段
        :return: 布尔值，True，表示数据库中有该新增记录字段
        """
        all_query_data = MysqlConnect().query(expert_sql)
        MysqlConnect().close()
        expect_assert_datas = []
        # 可一次性查询出数据库中多个字段，进行数据库测试断言
        # sys_user_genders = []
        for i in range(len(all_query_data)):
            expect_assert_datas.append(all_query_data[i][0])
            # sys_user_genders.append(sys_user_accounts_and_genders[i][1])
        # 可返回多个值
        # return sys_user_accounts,sys_user_genders
        try:
            for i in expect_assert_datas:
                if i == expect_data:
                    return True
        except Exception:
            return False





if __name__ == '__main__':
    driver = BoxDriver(BoxBrowser.Chrome)
    driver.navigate('https://www.baidu.com/')
    driver.type_enter('kw', '北京')
    time.sleep(2)
    # driver.quit()
    # driver.close_browser()
