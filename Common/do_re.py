"""
# @Time    : 2019/8/29 19:33
# @Author  : 谢超
# @File    : do_re.py
# @Function: 正则表达式
"""


import re
from Common.config import config
import configparser
from Common.do_log import MyLog


class Context:
    """
    设定反射的类
    """
    borrow_loanid = None


def DoRe(data):
    """
    1.用正则表达式来匹配测试数据中的指定字符
    2.根据指定字符获取到配置文件中对应的值
    3.然后进行替换
    """
    pattern = '#(.*?)#'  # 正则表达式   匹配组当中多次或者最多一次单个字符

    while re.search(pattern, data):
        search = re.search(pattern, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None

        group = search.group(1)  # 拿到参数化的KEY

        try:
            value = config.get_value('data', group)  # 根据KEY取配置文件里面的值
        except configparser.NoOptionError as e:  # 如果配置文件里面没有的时候，去do_re模块中类Context里面取
            if hasattr(Context, group):  # 判断类属性名是否在Context中
                value = getattr(Context, group)  # 获取类属性值
            else:
                MyLog(__name__).my_log().error('找不到参数化的值。报错：{}'.format(e))
                raise e

        """
        记得替换后的内容，继续用data接收
        """
        data = re.sub(pattern, value, data, count=1)  # 查找替换,count查找替换的次数

    return data


if __name__ == '__main__':
    pass
    # a = DoRe('{"id":"#534564#","status":4}')
    # print(a)
