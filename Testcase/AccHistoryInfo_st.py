"""
# @Time    : 2019/8/31 11:49
# @Author  : 贺世超
# @File    : AccHistoryInfo_st.py
# @Function: 获取节点列表
"""
import pytest
from Common.do_excel import DoExcel
from Common import contants
from Common.do_log import MyLog


class AccHistoryInfo_auth:
    doexcel_ob = DoExcel(contants.case_file, 'AccHistoryInfo')
    log_ob = MyLog(__name__).my_log()

    @pytest.mark.parametrize('case', doexcel_ob.get_cases())
    def test_auth_AccHistoryInfo(self, before_after_request, case):
        self.log_ob.debug('第 {} 条用例'.format(case.case_id))
        self.log_ob.debug('用例名称：{}'.format(case.case_name))
        resp = before_after_request.http_request(case.method, case.url, case.data)
        self.result = resp.json()
        row = case.case_id + 1
        result = str(self.result)
        try:
            assert self.result['code'] == eval(case.expected)['code']
            DoExcel(contants.case_file, 'AccHistoryInfo').write_case(row, result, 'pass')
            self.log_ob.debug("成功用例回写EXCEL成功")

        except:
            DoExcel(contants.case_file, 'AccHistoryInfo').write_case(row, result, 'failed')
            self.log_ob.debug("失败用例回写EXCEL成功")
            assert self.result['code'] == eval(case.expected)['code']

if __name__ == '__main__':
    AccHistoryInfo_auth().test_auth_AccHistoryInfo()