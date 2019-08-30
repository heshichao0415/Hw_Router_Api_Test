"""
# @Time    : 2019/8/30 11:52
# @Author  : 谢超
# @File    : conftest.py
# @Function: 测试前置后置等
"""

import pytest
from Common.http_request import HttpRequests_1
from Common.do_log import MyLog

log_ob = MyLog(__name__).my_log()


@pytest.fixture(scope="class")
def before_after_request():
    log_ob.info("--------------------开始执行用例--------------------")
    request_ob = HttpRequests_1()
    yield request_ob
    request_ob.close()
    log_ob.info("--------------------用例执行完毕--------------------")
