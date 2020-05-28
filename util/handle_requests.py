#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 0:17
# @Author  : xujiajun
# @Site    : 
# @File    : handle_requests.py
# @Software: PyCharm
# @contact: 924207089@qq.com


import requests, json

class HttpRequest:
    """
    处理请求
    """
    def __init__(self):
        """
        创建一个Session对象，赋值为HttpRequest对象的属性one_session
        """
        self.one_session = requests.Session()

    def __call__(self, method, url, data=None, is_json=False, header=None,**kwargs):
        method = method.lower()
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                print(e)
                data = eval(data)

        if method == 'get':
            res = self.one_session.request(method=method, url=url, params=data, headers=header, **kwargs)
        elif method == 'post':
            if is_json:  # 如果使用json数据来传参
                res = self.one_session.request(method=method, url=url, json=data, headers=header, **kwargs)
            else:
                res = self.one_session.request(method=method, url=url, data=data, headers=header, **kwargs)
                print(res.text)
        else:
            print('不支【{}】的请求方法'.format(method))
            res = None
        return res

    def close(self):
        self.one_session.close()


if __name__ == '__main__':
    # 获取验证码
    captcha_url = 'http://119.23.49.157/vmp/common/captcha/string'
    send_request = HttpRequest()
    res = send_request(method="GET", url=captcha_url, data={})
    captcha = eval(res.text)["data"]["captcha"]

    login_url = 'http://119.23.49.157/vmp/auth/login'
    login_params = {
      "companyNo": "csb",
      "customerGraphCode": captcha,
      "password": '123456',
      "username": "admin"
    }
    # 登录
    result1 = send_request(method='POST', url=login_url, json=login_params)
    dic = json.loads(result1.text)
    token = dic["data"]["token"]
    print(token)
    header = {
        "GET": "/vmp/org/user/list HTTP/1.1",
        "HOST": "119.23.49.157",
        "Authorization": token
    }

    account_url = 'http://119.23.49.157/vmp/org/user/list'
    _ = {}
    result2 = send_request("GET", account_url, _, header=header)
    print(result2.text)
