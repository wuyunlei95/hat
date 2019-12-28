import pymysql
import yaml
# pip install pyyaml


class MysqlConnect(object):
    """连接数据库，操作数据库"""

    def __init__(self,mysql_path):
        """建立数据库连接
        @:param host,port,user,passwd,db,charset
        @:return cursor
        """
        # 本文件中调试路径：
        file = open(mysql_path, encoding='utf8')
        # 读取数据库参数
        # main.py主入口调用路径如下：
        # file = open('common/config/ranzhi.yaml', encoding='utf8')
        ydata = yaml.load(file)
        file.close()
        host = ydata['database']['host']
        port = ydata['database']['port']
        user = ydata['database']['user']
        passwd = ydata['database']['passwd']
        db = ydata['database']['db']
        charset = ydata['database']['charset']
        self.connect = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        self.cursor = self.connect.cursor()

    def query(self, sql):
        """执行查询
        @:param sql
        @:return data
        """
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        # self.connect.commit()
        # user_accounts = []
        # for i in range(len(data)):
        #     user_accounts.append(data[i][1])
        # return user_accounts
        return data

    def close(self):
        """关闭数据库连接，释放资源"""
        self.cursor.close()
        self.connect.close()


if __name__ == '__main__':
    """测试入口"""
    # 本文件中调试路径：
    db_path = '../config/ranzhi.yaml'
    # main.py主入口调用路径如下：
    # db_path = 'common/config/ranzhi.yaml'
    connect = MysqlConnect(db_path)
    data = connect.query('select account,gender from sys_user;')
    print(data)
    user_accounts = []
    user_genders = []
    for i in range(len(data)):
        user_accounts.append(data[i][0])
        user_genders.append(data[i][1])
    print(user_accounts)
    print(user_genders)
    connect.close()

