"""
# @Time    : 2019/8/29 19:31
# @Author  : 谢超
# @File    : do_db.py
# @Function: 完成数据库的读取
"""

import pymysql
from Common.config import ReadConfig

config = ReadConfig()


class DoMysql:
    """
    初始化：
    1.从配置文件获取到数据库的连接信息
    2.建立光标
    方法：
    1.执行sql语句，获取一个或者全部数据
    2.关闭光标和数据库
    """

    def __init__(self):
        # 设置连接数据库的参数，还是从配置文件读取
        self.mysql = pymysql.connect(host=config.get_value('testdb', 'host'),
                                     port=int(config.get_value('testdb', 'port')),
                                     user=config.get_value('testdb', 'user'),
                                     password=config.get_value('testdb', 'password'),
                                     db=config.get_value('testdb', 'db'),
                                     charset=config.get_value('testdb', 'charset'))

        # 查询的数据以键值对返回
        # self.cursor = self.mysql.cursor(cursor=pymysql.cursors.DictCursor)

        # 查询的数据以元组返回
        self.cursor = self.mysql.cursor()

        # 匹配一条数据

    def fetch_one(self, sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()

    # 匹配所有数据
    def fetch_all(self, sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()

    # 关闭数据库
    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    pass
