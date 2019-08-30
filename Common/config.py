"""
# @Time    : 2019/8/29 19:28
# @Author  : 谢超
# @File    : Conf.py
# @Function: 配置文件的读取
"""

import configparser
from Common import contants


class ReadConfig:
    """
    通过global配置文件来控制环境
    初始化：
    1.读取global配置文件的值
    2.判断布尔值是True或者False来读取其他配置文件
    方法：
    设定一个方法来返回得到其他配置文件的值
    """

    def __init__(self):

        # 实例化对象
        self.config = configparser.ConfigParser()

        # 读取配置文件
        self.config.read(contants.global_file, encoding='utf-8')

        # 根据section和option获取值
        switch = self.config.getboolean('switch', 'on')

        # 获取到的值为True,就读取测试环境配置文件
        if switch:
            self.config.read(contants.test_file, encoding='utf-8')

        # 获取到的值为False,就读取预发布环境配置文件
        else:
            self.config.read(contants.staging_file, encoding='utf-8')

    # 获取配置文件的方法
    def get_value(self, section, option):
        return self.config.get(section, option)


if __name__ == '__main__':
    pass
