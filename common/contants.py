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

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# base_dir=os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]

case_file = os.path.join(base_dir, 'Testdata', 'case.xlsx')

report_file = os.path.join(base_dir, 'Testresult', 'html_report.html')

# log_file = os.path.join(base_dir, 'Testresult', 'api_test.log')

log_storage_file = os.path.join(base_dir, 'Testresult')

log_file = os.path.join(log_storage_file, '{}.log'.format(time.strftime('%Y-%m-%d')))

global_file = os.path.join(base_dir, 'Conf', 'global.Conf')

staging_file = os.path.join(base_dir, 'Conf', 'staging.Conf')

test_file = os.path.join(base_dir, 'Conf', 'test.Conf')

discover_file = os.path.join(base_dir, 'Testcase')
