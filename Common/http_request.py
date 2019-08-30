"""
# @Time    : 2019/8/29 19:34
# @Author  : 谢超
# @File    : http_request.py
# @Function: 完成http请求
"""


import requests
from Common.config import config
from Common.do_log import MyLog


class HttpRequests_1:
    """
    1.通过http_request方法来完成http请求，并得到返回结果
    2.同一个session对象调用request方法才会自动传入cookies到下一个请求中
    3.不同对象中，cookies不共享
    4.这种方式不需要获取登录后的cookies，自动收集cookies
    """
    log_ob = MyLog(__name__).my_log()

    def __init__(self):
        # 打开一个session
        self.session = requests.sessions.session()

    def http_request(self, method, url, data=None, json=None):

        if type(data) == str:
            data = eval(data)

        # 拼接url地址
        url = config.get_value('api', 'base_url') + url

        self.log_ob.debug('请求的方式：{}'.format(method))
        self.log_ob.debug('请求的地址：{}'.format(url))
        self.log_ob.debug('请求的数据：{}'.format(data))

        if method.upper() == 'GET':
            resp = self.session.request(method=method, url=url, params=data)
        elif method.upper() == 'POST':
            if json is not None:  # 或者 if json:
                resp = self.session.request(method=method, url=url, json=data)
            else:
                resp = self.session.request(method=method, url=url, data=data)
        else:
            self.log_ob.error('不支持的请求方式')
        self.log_ob.info('返回的结果：{}'.format(resp.text))
        return resp

    def close(self):
        self.session.close()


# class HttpRequests_2:
#     """
#     1.通过http_request方法来完成http请求，并得到返回结果
#     2.不同对象中，cookies不共享，需要自己传递cookies
#     """
#
#     def http_request(self, method, url, data=None, json=None, cookies=None):
#
#         if type(data) == str:
#             data = eval(data)
#
#         # 拼接url地址
#         url = config.get_value('api', 'base_url') + url
#
#         if method.upper() == 'GET':
#             resp = requests.get(url, params=data, cookies=cookies)
#         elif method.upper() == 'POST':
#             if json is not None:  # 或者 if json:
#                 resp = requests.post(url, json=data, cookies=cookies)
#             else:
#                 resp = requests.post(url, data=data, cookies=cookies)
#         else:
#             return 'Unsupport method'
#
#         return resp


if __name__ == '__main__':
    a=HttpRequests_1()
    b=a.http_request('post','/api/v1/xyhw/GetBlackBlackLIst',{})


