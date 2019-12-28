import sys
import os

from common.base.html_email_attachment import HtmlEmailAttachment
from src.practices.test_paramunitest2 import TestDemo
from src.testcase_runner.case.add_user_fields_testcase import AddUserFieldsTestcast
from src.testcase_runner.case.add_user_scenes_testcase import AddUserScencesTestcast

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import time
import unittest

from common.base.html_test_runner import HtmlTestRunner


class RanzhiRunner():
    '''生成用户登录测试报告'''

    def run(self):
        # 测试存放文件夹位置
        # cases_path = 'src\\practices'
        cases_path = 'src\\testcase_runner\\case'
        test_suite = unittest.TestSuite()

        # 自动搜索目录下所有测试用例文件并添加到test_suite中
        discover = unittest.defaultTestLoader.discover(start_dir=cases_path,pattern='add_user*.py',top_level_dir=None)
        for dir in discover:
            for suite in dir:
                test_suite.addTests(suite)

        # 往测试套件中添加测试用例
        # 测试添加用户成功的用例
        # test_suite.addTest(AddUserScencesTestcast('test_add_user_success'))
        # test_suite.addTest(TestDemo('test_case'))
        # test_suite.addTest(AddUserScencesTestcast('test_del_success'))
        # test_suite.addTest(AddUserFieldsTestcast('test_add_user_failure'))
        # 登录测试用例
        # test_suite.addTest(LoginTest('test_login_success'))
        # 创建测试报告文件路径
        report_path = 'results/report/ranzhi_test_%s.html' % time.strftime('%Y-%m-%d_%H%M%S')
        # 创建并打开测试报告文件
        report_file = open(report_path, 'wb')
        # 引入测试报告框架，传入参数
        testRunner = HtmlTestRunner(stream=report_file, verbosity=2,title='然之测试', description='登陆，语言，模块标题，添加用户')
        # 运行测试套件，在测试报告中写入测试结果
        testRunner.run(test_suite)
        # 关闭打开的file,释放资源
        report_file.close()
        # 发送邮件
        HtmlEmailAttachment().email_attachment(report_path)


if __name__ == '__main__':
    runner = RanzhiRunner()
    runner.run()
