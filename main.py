from src.testcase_runner.runner.ranzhi_runner import RanzhiRunner


class Main(object):
    """程序执行入口"""

    def run(self):
        """实例化RanzhiRunner,运行runner中的测试套件"""
        runner = RanzhiRunner()
        runner.run()


if __name__ == '__main__':
    main = Main()
    main.run()
