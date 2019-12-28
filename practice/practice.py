# import unittest
#
#
# class IntegerArithmeticTestCase(unittest.TestCase):
#     def testAdd(self):
#     # test method names begin 'test*'
#         self.assertEqual((1 + 2), 3)
#         print("通过")
#         self.assertEqual(0 + 1, 1)
#
#
#     def testMultiply(self):
#         self.assertEqual((0 * 10), 0)
#         self.assertEqual((5 * 8), 40)
#         print("通过")
#
#     def testMinus(self):
#         """测试减法"""
#         # 实际结果
#         resulf = 6-5
#         # 期望结果
#         hoep = 2
#         self.assertEqual(resulf, hoep, "实际结果%s不等于2" % resulf)
#         print("通过")
#
#     def testDivide(self):
#         """测试除法"""
#         resulf = 9/3
#         hope = 2
#         self.assertEqual(resulf, hope, "实际结果%s不等于2" % resulf)
#         print("通过")
#
# if __name__ == '__main__':
#     unittest.main()

from selenium import webdriver
import  time

driver = webdriver.Chrome()
print(driver.get_cookies())
driver.get("https://home.cnblogs.com/u/1432839/")
data = driver.get_cookies()
print(data)
for i in data:
    print(i)
    for a in i:
        print(a)
