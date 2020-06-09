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


@ddt
class TestLogin(unittest.TestCase):
    """
    Test login of Recadas Platform .
    """
    cases = do_excel.get_cases()
    send_request = HttpRequest()

    @classmethod
    def setUp(self):
        """
        Gain the captcha and token for logining.
        :return:
        """
        captcha_url = 'http://119.23.49.157/vmp/common/captcha/string'
        res = self.send_request(method="GET", url=captcha_url, data={})
        self.captcha = eval(res.text)["data"]["captcha"]

    @classmethod
    def tearDown(self):
        """
        Close HTTP link after cases executed.
        :return:
        """
        self.send_request.close()
        do_mysql.close()

    @data(*cases)
    def test_login(self, value):
        """
        :param value:
        :return:
        """
        row = value.case_id
        login_url = 'http://119.23.49.157' + value.url

        # replace captcha
        login_data = do_re.sub(value.data, self.captcha)

        # Replace expected data from database,then gain expected data
        if do_re.matchdata(value.temp):
            user = eval(value.data)["username"]
            sql = "SELECT t2.org_name as company_name,t.company_no,t1.id as user_id,t.org_name,t1.real_name,t3.id as role_id,t3.role_name,t3.role_type\
                FROM t_ascs_vmp_org t,t_ascs_vmp_user t1,t_ascs_vmp_org t2,t_ascs_vmp_role t3,t_ascs_vmp_account_role_relationship t4\
                WHERE t.id = t1.org_id and t.id = t2.id and t2.parent_org_id = 0 and t.id = t3.company_id and t.id = t4.company_id and t4.account_id = t1.id and t4.role_id = t3.id and t1.company_no = 'csb' and t1.username = %s;"
            expect_data = dict(zip_longest(["companyName", "companyNo", "id", "orgName", "realName", "roleId", "roleName",
                                       "roleType", "token"], do_mysql(sql, user)[0]))
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


