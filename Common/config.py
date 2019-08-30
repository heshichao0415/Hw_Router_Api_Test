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
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_file, encoding='utf-8')
        switch = self.config.getboolean('switch', 'on')
        if switch:
            self.config.read(contants.test_file, encoding='utf-8')
        else:
            self.config.read(contants.staging_file, encoding='utf-8')

    def get_value(self, section, option):
        return self.config.get(section, option)


config = ReadConfig()
