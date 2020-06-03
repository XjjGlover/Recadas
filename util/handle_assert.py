#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 10:03
# @Author  : xujiajun
# @Site    : 
# @File    : handle_assert.py
# @Software: PyCharm
# @contact: 924207089@qq.com


# 断言方法，比较两个list或dict的不同之处

a = 'abc'
b = 'abc'


class HandleAssert:
    """
    Wrap assert moudle.
    """
    def __init__(self):
        pass

    def _compare_json_data(self, act, exp):
        """
        Compare json data.
        :return:
        """
        if isinstance(exp, dict) and isinstance(act, dict):
            for i in act:
                if i == ("token" or "total"):
                    continue
                try:
                    exp[i]
                except Exception:
                    raise AssertionError
                if isinstance(act[i], dict) and isinstance(exp[i], dict):
                    _ = self._compare_json_data(act[i], exp[i])
                    if not _:
                        raise AssertionError
                elif act[i] != exp[i]:
                    raise AssertionError
            return True

    def Assert(self, actual, expect):
        result = self._compare_json_data(actual, expect)
        return result


do_assert = HandleAssert()


if __name__ == '__main__':
    expect = {
        'code': 200,
        'data': {
            'companyName': "嘉俊和他的小伙伴集团",
            'companyNo': "csb",
            'id': 873073596974882,
            'orgName': "嘉俊和他的小伙伴集团",
            'realName': "企业管理员",
            'roleId': 873073596974881,
            'roleName': "企业管理员",
            'roleType': "COMPANY_ADMIN",
            'token': ""
        },
        'message': "操作成功",
        'total': 0
    }
    actual = {
        'code': 200,
        'data': {
            'companyName': "嘉俊和他的小伙伴集团",
            'companyNo': "csb",
            'id': 873073596974882,
            'orgName': "嘉俊和他的小伙伴集团",
            'realName': "企业管理员",
            'roleId': 873073596974881,
            'roleName': "企业管理员",
            'roleType': "COMPANY_ADMIN"
        },
        'message': "操作成功"
    }
    do_assert = HandleAssert()
    result = do_assert.Assert(actual, expect)
    print(result)