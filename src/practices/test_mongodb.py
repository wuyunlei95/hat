from common.util.mongodb_connect import MongodbConnect
import unittest
from common.base.log import Log

class TestMongoDB(unittest.TestCase):
      # MongoDB YAML配置文件路径
      # main.py中运行，路径
      YAML_PATH = 'common/config/mongo.yaml'
      # 本文件中调试运行，路径
      # YAML_PATH = '../../common/config/mongo.yaml'
      # MongoDB 查询参数
      QUERY_ARGS = {'q_find': ({}, {'by_user': 'runoob.com'}),
                    'q_sort': ('by_user', -1),
                    'q_limit': 4, 'q_skip': None}

      # 日志保存路径
      # LOG_PATH = '..\\..\\results\\log'
      LOG_PATH = 'results\\log'
      # 实例化日志
      log = Log(LOG_PATH)

      def setUp(self):

            pass

      def tearDown(self):
            pass

      def test_mongo_query(self):
            mongodb_connect = MongodbConnect(self.YAML_PATH)
            query_results = mongodb_connect.query(self.QUERY_ARGS)
            for query_result in query_results:
                self.log.info(query_result)
                # self.log.info(query_result['by_user'])
            mongodb_connect.close()

if __name__ == '__main__':
    unittest.main()