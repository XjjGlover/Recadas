#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 19:04
# @Author  : xujiajun
# @Site    : 
# @File    : login.py
# @Software: PyCharm
# @contact: 924207089@qq.com
import os

from ddt import ddt, data
import unittest
import json
from util.handle_requests import HttpRequest
from util.handle_excel import do_excel
from util.handle_re import do_re
from util.handle_assert import do_assert
from util.get_data import GetToken


@ddt
class TestLogin(unittest.TestCase):
    """
    Test login of Recadas Platform .
    """
    cases = do_excel.get_cases()
    send_request = HttpRequest()

    @classmethod
    def setUpClass(cls):
        """
        Gain the captcha and token for logining.
        :return:
        """
        captcha_url = 'http://119.23.49.157/vmp/common/captcha/string'
        res = cls.send_request(method="GET", url=captcha_url, data={})
        cls.captcha = eval(res.text)["data"]["captcha"]

    @classmethod
    def tearDownClass(cls):
        """
        Close HTTP link after cases executed.
        :return:
        """
        cls.send_request.close()

    @data(*cases)
    def test_login(self, value):
        """
        :param value:
        :return:
        """
        row = value.case_id
        login_url = 'http://119.23.49.157' + value.url
        login_data = do_re.sub(value.data, self.captcha)
        res = self.send_request(value.method, login_url, login_data, is_json=True)
        try:
            token = json.loads(res.text)["data"]["token"]
            setattr(GetToken, "token", token)
        except Exception as e:
            raise e

        actual = res.text
        expect = value.expect
        try:
            do_assert.Assert(actual, expect)
        except Exception as e:
            do_excel.write_res(row, actual, "Fail")
            raise e
        else:
            do_excel.write_res(row, actual, "success")


if __name__ == '__main__':
    unittest.main()


