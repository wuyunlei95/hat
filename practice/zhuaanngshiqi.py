import unittest
import time


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start!")


    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print("end!")


    def test01(self):
        print("执行测试用例01")


    def test03(self):
        print("执行测试用例03")


    def test02(self):
        print("执行测试用例02")
        resulf = 9 / 3
        hope = 2
        self.assertEqual(resulf, hope, "实际结果%s不等于2" % resulf)
        print("通过")


    def addtest(self):
        print("add方法")



if __name__ == "__main__":
    unittest.main()

# import unittest
# import time
#
#
# class Test(unittest.TestCase):
#     def setUp(self):
#         print("start!")
#
#
#     def tearDown(self):
#         time.sleep(1)
#         print("end!")
#
#
#     def test01(self):
#         print("执行测试用例01")
#         resulf = 9 / 3
#         hope = 2
#         self.assertEqual(resulf, hope, "实际结果%s不等于2" % resulf)
#         print("通过")
#
#     def test03(self):
#         print("执行测试用例03")
#
#
#     def test02(self):
#         print("执行测试用例02")
#
#
#     def addtest(self):
#         print("add方法")
#
#
#
# if __name__ == "__main__":
#     unittest.main()