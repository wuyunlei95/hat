import pymongo
import yaml


class MongodbConnect:

    def __init__(self,yaml_path):
        """
        建立数据库连接
        (有认证方式 & 无认证方式 )
        :param mongo_host: MongoDB服务器IP
        :param mongo_port: MongoDB服务器端口
        :param database:   MongoDB数据库
        :param collection: MongoDB集合（表）
        :param user: （有认证方式，默认授权admin数据库）用户名
        :param pwd: （有认证方式，默认授权admin数据库）用户名
        """
        # 本文件中调试路径：
        file = open(yaml_path, encoding='utf8')
        # 读取数据库参数
        # main.py主入口调用路径如下：
        # file = open('common/config/mongo.yaml', encoding='utf8')
        ydata = yaml.load(file)
        file.close()
        mongo_host = ydata['mongo_database']['mongo_host']
        mongo_port = ydata['mongo_database']['mongo_port']
        database = ydata['mongo_database']['database']
        collection = ydata['mongo_database']['collection']
        user = ydata['mongo_database']['user']
        pwd = ydata['mongo_database']['pwd']

        mongo_host = mongo_host
        mongo_port = mongo_port
        self.client = pymongo.MongoClient('%s:%d' % (mongo_host, mongo_port))
        # 连接到数据库myDatabase
        database = database
        db = self.client[database]
        # 连接到集合(表):database.collection
        collection = collection
        self.db_col = db[collection]
        # mongoDB有不同的认证机制，3.0版本以后采用的是’SCRAM-SHA-1’, 之前的版本采用的是’MONGODB-CR’
        # user,pwd,针对的是 admin 数据库的认证
        if user != None and pwd != None:
            self.client.admin.authenticate(user, pwd, mechanism='SCRAM-SHA-1')

    def query(self,query_args):
        '''
        根据查询参数，返回查询结果
        :param q_find: MongoDB查询参数—find-查找
        :param q_sort: MongoDB查询参数—sort-排序,无此参数时，则输入为 None
        :param q_limit: MongoDB查询参数—limit-前几条,无此参数时，则输入为 None
        :param q_skip: MongoDB查询参数—skip-跳过第几条,无此参数时，则输入为 None
        :return: 数据库查询结果，字典形式
        '''
        try:
            # 字符串方式连接
            # a1 = ["db_col", "find({}, {'by_user': 1})", "sort('likes', -1)", "limit(2)"]
            # b1 = '.'.join(a1)
            # print(b1)

            if query_args['q_find'] != None and query_args['q_sort'] == None and query_args['q_limit'] == None and query_args['q_skip'] == None:
                self.search_result = self.db_col.find(*query_args['q_find'])
            elif query_args['q_find'] != None and query_args['q_sort'] != None and query_args['q_limit'] == None and query_args['q_skip'] == None:
                self.search_result = self.db_col.find(*query_args['q_find']).sort(*query_args['q_sort'])
            elif query_args['q_find'] != None and query_args['q_sort'] == None and query_args['q_limit'] != None and query_args['q_skip'] == None:
                self.search_result = self.db_col.find(*query_args['q_find']).limit(query_args['q_limit'])
            elif query_args['q_find'] != None and query_args['q_sort'] == None and query_args['q_limit'] != None and query_args['q_skip'] != None:
                self.search_result = self.db_col.find(*query_args['q_find']).limit(query_args['q_limit']).skip(query_args['q_skip'])
            elif query_args['q_find'] != None and query_args['q_sort'] != None and query_args['q_limit'] != None and query_args['q_skip'] == None:
                self.search_result = self.db_col.find(*query_args['q_find']).sort(*query_args['q_sort']).limit(query_args['q_limit'])
            elif query_args['q_find'] != None and query_args['q_sort'] != None and query_args['q_limit'] != None and query_args['q_skip'] != None:
                self.search_result = self.db_col.find(*query_args['q_find']).sort(*query_args['q_sort']).limit(query_args['q_limit']).skip(query_args['q_skip'])
            else:
                raise NameError("查询条件输入错误！")
            return self.search_result

        except:
            raise NameError('MongoDB认证方式，数据库查询失败！')

    def close(self):
        """关闭数据库连接，释放资源"""
        self.client.close()
        self.search_result.close()


if __name__ == '__main__':
    yaml_path = '../config/mongo.yaml'
    mongodb_connect = MongodbConnect(yaml_path)
    query_args = {'q_find':({}, {'by_user': 'runoob.com'}),'q_sort':('by_user',-1),
                  'q_limit':4,'q_skip':None}
    query_results = mongodb_connect.query(query_args)
    for query_result in query_results:
        print(query_result)
        print((query_result['by_user']))
    mongodb_connect.close()

