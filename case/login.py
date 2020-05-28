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
from util.handle_requests import HttpRequest
from util.handle_excel import do_excel


@ddt
class TestLogin(unittest.TestCase):
    """
    Test login of Recadas Platform .
    """
    cases = do_excel.get_cases()

    @classmethod
    def setUpClass(cls):
        """
        Gain the captcha and token for logining.
        :return:
        """
        captcha_url = 'http://119.23.49.157/vmp/common/captcha/string'
        cls.send_request = HttpRequest()
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
        res = self.send_request(value.method, login_url, value.data, is_json=True)
        try:
            self.assertEqual(200, eval(res.text)["code"])
            self.assertIn(r"操作成功", res.text)
        except Exception as e:
            do_excel.write_res(row, res.text, "Fail")
            raise e
        else:
            do_excel.write_res(row, res.text, "success")


if __name__ == '__main__':
    unittest.main()


