import os

class NewestReport():
    # 如果方法中没有加self,则报错：TypeError: new_report() takes 1 positional argument but 2 were given
    def new_report(self,test_report):
        # 列出目录的下所有文件和文件夹保存到lists
        lists = os.listdir(test_report)
        print(list)
        # 按时间排序
        lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn))
        # 获取最新的文件保存到file_new
        file_new = os.path.join(test_report,lists[-1])
        # file_new带路径 ..\reports\ranzhi_report_20180424142831.html
        print(file_new)
        return file_new

if __name__=="__main__":
    # 目录地址
    test_report="..\\..\\results\\report"
    # 找出test_report目录下最新产生的文件名
    newest_file = NewestReport().new_report(test_report)
    # 打印文件的绝对路径
    file_abspath = os.path.abspath(newest_file)
    print(file_abspath)