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
from itertools import zip_longest
from util.handle_requests import HttpRequest
from util.handle_excel import do_excel
from util.handle_re import do_re
from util.handle_assert import do_assert
from util.get_data import GetToken
from util.handle_mysql import do_mysql
from util.handle_log import do_log
from util.handle_conf import do_conf


@ddt
class TestLogin(unittest.TestCase):
    """
    Test login of Recadas Platform .
    """
    cases = do_excel.get_cases()
    send_request = HttpRequest()

    @classmethod
    def setUp(cls):
        """
        Gain the captcha and token for logining.
        :return:
        """
        captcha_url = do_conf.get_value("url", "captcha_url")
        res = cls.send_request(method="GET", url=captcha_url, data={})
        cls.captcha = eval(res.text)["data"]["captcha"]

    @classmethod
    def tearDownClass(cls):
        """
        Close HTTP link after cases executed.
        :return:
        """
        cls.send_request.close()
        do_mysql.close()

    @data(*cases)
    def test_login(self, value):
        """
        :param value:
        :return:
        """
        row = value.case_id
        login_url = do_conf.get_value("url", "ip") + value.url

        # replace captcha
        login_data = do_re.sub(value.data, self.captcha)

        # Replace expected data from database,then gain expected data
        if do_re.matchdata(value.temp):
            user = eval(value.data)["username"]
            sql = do_conf.get_value('sql', "user_data")
            expect_data = dict(zip_longest(["companyName", "companyNo", "id", "orgName", "realName", "roleId",
                                            "roleName", "roleType", "token"], do_mysql(sql, user)[0]))
            expect = do_re.sub(value.temp, "{}".format(expect_data))
        else:
            expect = value.temp

        # Send http request
        res = self.send_request(value.method, login_url, login_data, is_json=True)
        actual = res.text
        print('*' * 10 + actual + '*' * 10)

        # Parse http response,then gain token's value
        try:
            token = json.loads(res.text)["data"]["token"]
            setattr(GetToken, "token", token)
        except Exception as e:
            pass

        try:
            do_assert.Assert(eval(actual), eval(expect))
        except Exception as e:
            do_excel.write_res(row, actual, expect, "Fail")
            do_log.error("*" * 5 + value.title + "执行失败" + "*" * 5)


            raise e
        else:
            do_excel.write_res(row, actual, expect, "success")
            do_log.info("*" * 5 + value.title + "执行成功" + "*" * 5)


if __name__ == '__main__':
    unittest.main()


