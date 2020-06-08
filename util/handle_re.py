#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 2:17
# @Author  : xujiajun
# @Site    : 
# @File    : handle_re.py
# @Software: PyCharm
# @contact: 924207089@qq.com


import re
from util.handle_mysql import do_mysql


class HandleRe:
    """
    Wrap re moudle.
    """
    captcha_pattern = re.compile(r"\${captcha\}")
    data_pattern = re.compile(r"\${data\}")

    def __init__(self):
        pass

    def _captcha(self, data, value):
        """
        Substitute captcha and return the data substituted.
        :return:
        """
        res = re.sub(self.captcha_pattern, value, data)
        return res

    def _data(self, data, value):
        """
        Substitute data and return the data substituted.
        :return:
        """
        res = re.sub(self.data_pattern, value, data)
        return res

    def sub(self, data, value):
        if re.search(self.captcha_pattern, data):
            res = self._captcha(data, value)
        elif re.search(self.data_pattern, data):
            res = self._data(data, value)
        else:
            res = data
        return res


do_re = HandleRe()


if __name__ == '__main__':
    data = '{\
      "companyNo": "csb",\
      "customerGraphCode": "${data}",\
      "password": "123456",\
      "username": "admin"\
    }'
    do_re = HandleRe()
    res = do_re.sub(data, "vjks")
    print(res)




