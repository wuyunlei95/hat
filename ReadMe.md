# ReadMe


```
【 代码结构说明 】
'''
Author: 刘林杰
Date: 2018-06-01
Desc: 代码结构说明
'''

hat # 项目名称
	common
		base
			base_page.py # 继承 base.box_driver.BoxDriver
			box_driver.py # 封装常用方法（如打开浏览器，定位元素等）
			html_email_attachment.py # 将测试报告发送邮件
			html_test_runner.py # 第三方生成html测试报告的模板
			log.py # 生成日志的方法
		config
			ranzhi.yaml # 配置ranzhi数据库库			
		util
			csv_file.py # 打开关闭csv文件的方法
			mysql_connect.py # 连接关闭mysql数据库的方法
	results
		log # 如：2018_05_29.log 安装日期记录所有的操作日志
		report # 如：ranzhi_test_login2018-05-28_172010.html 按照当前时间生成测试报告
		screenshot # 如： 2018-05-28_17-38-58_admin登录成功.png 截图并标题附加图片说明
	src
		data # 造数据，存放csv数据
		page # 如：sys_main_page.py 写业务流程，最好是以page结尾
		testcase_runner
			case # 如：add_user_testcase.py 写测试场景用例，最好是以test或testcase结尾
			runner # 测试套件，指定将要运行的测试用例
	main.py # 程序主入口，每次测试用例运行，都运行此入口
		
```

```buildoutcfg
[ D1 ] 具体代码见: d1_test_data_type_csv_mysql.py  d1_test_class_def.py
```
```buildoutcfg
[ D1 ]
注释：
    单行注释
        # 
        快捷键 ctrl + /
    多行注释
        '''
        '''
        
        """
        """
路径：
    绝对路径
        c:\Users\tester\Desktop\Jet-W2\D3\hat\common\config\ranzhi.yaml
    相对路径
        代码里，建议都使用相对路径
        if __name__ == '__main__': 调试情况下读取csv文件路径
        main.py 主函数入口（unittest框架运行）运行情况下读取csv路径
常用数据类型介绍：
    数字
    字符串
    布尔值
    List(数组）
    Dict(字典）
    tuple(元组)
循环：
    for 
    while
判断：
    if .. elif ..else  
与、或、非
    and
    or
    !=
数据读取：
    csv 
    mysql 
配置文件：
    yaml
理解面向对象编程思想：
    类
    方法
    类方法的调用
```


```buildoutcfg
[ D2 ]
项目结构介绍
box_driver 常用方法介绍
page 页面业务逻辑
Pycharm 常用快捷键
Python 类、方法、变量、常量命名规则介绍
```

```buildoutcfg
[ D3 ]
data 数据准备
test_case 测试用例介绍
其它介绍(如：log,report,runner,config等）
```

```buildoutcfg
[ W2 ]
做一个自动化迭代项目（ranzhi为例）
编写4个Page：
    sys_main_page.py (登录+主页）
    sys_admin_page.py（后台管理主页）
    sys_user_admin_page(组织，用户列表）
    sys_user_create_page.py(添加用户页面）
针对 sys_user_create_page.py(添加用户页面），编写测试用例testcase(包括字段用例&场景用例）
编写自动化测试计划
编写自动化结项报告
```

