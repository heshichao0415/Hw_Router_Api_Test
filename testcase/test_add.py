"""
@Time    : 2019/4/21 19:51
@Author  : Cooper
@File    : test_add.py
@Function: 完成加标模块用例
"""

import json, pytest

from Common.do_excel import DoExcel
from Common import contants
from Common.do_log import MyLog
from Common.do_re import DoRe


class TestAdd:
    doexcel_ob = DoExcel(contants.case_file, 'add')
    log_ob = MyLog(__name__).my_log()

    @pytest.mark.parametrize("case", doexcel_ob.get_cases())
    def test_add(self, before_after_request, case):
        case.data = DoRe(case.data)

        # 请求之前查询数据库，查询加标之前的id
        if case.sql is not None:
            sql = json.loads(case.sql)["sql_1"]
            before_loanid = before_after_request[1].fetch_one(sql)[0]

        self.log_ob.debug('第 {} 条用例'.format(case.case_id))
        self.log_ob.debug('用例名称：{}'.format(case.case_name))
        resp = before_after_request[0].http_request(case.method, case.url, case.data)
        self.log_ob.debug('预期结果：{}'.format(case.expected))
        try:
            assert case.expected == resp.text
            self.doexcel_ob.write_case(case.case_id + 1, resp.text, 'PASS')

            # 请求之后查询数据库，查询加标之后的id
            if case.sql is not None:
                sql = json.loads(case.sql)['sql_1']
                after_loanid = before_after_request[1].fetch_one(sql)[0]

                # 因为id自增，判断加标后的id大于加标前id
                assert before_loanid < after_loanid

        except AssertionError as e:
            self.doexcel_ob.write_case(case.case_id + 1, resp.text, 'FAIL')
            self.log_ob.error('接口请求出错啦!{}'.format(e), exc_info=True)
            raise e
