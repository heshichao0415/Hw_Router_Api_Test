"""
# @Time    : 2019/8/30 11:49
# @Author  : 谢超
# @File    : test_getgamebalcklist.py
# @Function: 测试获取游戏黑名单
"""

import json, pytest

from Common.do_excel import DoExcel
from Common import contants
from Common.do_log import MyLog
from Common.do_re import DoRe


class TestGetGameBlackList:
    doexcel_ob = DoExcel(contants.case_file, 'GetBlackBlackList')
    log_ob = MyLog(__name__).my_log()

    @pytest.mark.parametrize('case', doexcel_ob.get_cases())
    def test_getgameblacklist(self, before_after_request, case):
        self.log_ob.debug('第 {} 条用例'.format(case.case_id))
        self.log_ob.debug('用例名称：{}'.format(case.case_name))
        resp = before_after_request.http_request(case.method, case.url, case.data)
        print(resp)
