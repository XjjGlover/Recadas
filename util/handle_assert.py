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
                if i == "token":
                    continue
                try:
                    exp[i]
                except Exception:
                    return False
                if isinstance(act[i], dict) and isinstance(exp[i], dict):
                    _ = self._compare_json_data(act[i], exp[i])
                    if not _:
                        return False
                elif act[i] != exp[i]:
                    return False
            return True

    def Assert(self, actual, expect):
        result = self._compare_json_data(actual, expect)
        return result


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
            'token': "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJjb21wYW55SWRcIjo4NzMwNzM1OTY5NzQ4ODAsXCJjb21wYW55TmFtZVwiOlwi5ZiJ5L-K5ZKM5LuW55qE5bCP5LyZ5Ly06ZuG5ZuiXCIsXCJjb21wYW55Tm9cIjpcImNzYlwiLFwiaWRcIjo4NzMwNzM1OTY5NzQ4ODIsXCJsb2dpbklkZW50aXR5XCI6XCIyYzkyOTRlMTcyNmYxMWI5MDE3MjZmNzlkYmU1MDAwZFwiLFwib3JnSWRcIjo4NzMwNzM1OTY5NzQ4ODAsXCJyZWFsTmFtZVwiOlwi5LyB5Lia566h55CG5ZGYXCIsXCJyb2xlVHlwZVwiOlwiQ09NUEFOWV9BRE1JTlwiLFwidGVybWluYWxUeXBlXCI6XCJXRUJcIn0ifQ.f8dd5pQyQaCLO9rZAFChtOOldf4RBij8h7uMxGsvtXkht38Ss30DN7zR8hQOgxzxYapx6jFuGiXQNvcPiBLjbg"
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
            'roleId': 87307359697488,
            'roleName': "企业管理员",
            'roleType': "COMPANY_ADMIN",
            'token': "abc"
        },
        'message': "操作成功",
        'total': 0
    }
    do_assert = HandleAssert()
    result = do_assert.Assert(actual, expect)
    print(result)