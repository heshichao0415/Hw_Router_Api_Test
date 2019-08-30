"""
# @Time    : 2019/8/29 19:30
# @Author  : 谢超
# @File    : contants.py
# @Function: 文件路径的拼接
"""

import os, time

"""
目录结构不变，都可以运行
os.path.abspath(__file__)，获取当前路径，且包含当前位置，定位到真实位置
os.path.dirname(__file__)，获取当前路径，不包含当前文件，定位到目录所在位置
os.path.split(path)  切割路径，返回元组
os.path.join()   拼接路径
"""

# 获取当前时间
now_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

# 项目的基本路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# base_dir1=os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]


# excel的路径
case_file = os.path.join(base_dir, 'Testdata', 'case.xlsx')

# 存放日志文件的路径
log_storage_file = os.path.join(base_dir, 'Logs')

# 日志命名
log_file = os.path.join(log_storage_file, '{}.log'.format(now_time))
# log_file = os.path.join(log_storage_file, '{}.log'.format(time.strftime('%Y-%m-%d')))


global_file = os.path.join(base_dir, 'Conf', 'global.Conf')

staging_file = os.path.join(base_dir, 'Conf', 'staging.Conf')

test_file = os.path.join(base_dir, 'Conf', 'test.Conf')
