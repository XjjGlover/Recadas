#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/29 1:41
# @Author  : xujiajun
# @Site    : 
# @File    : handle_log.py
# @Software: PyCharm
# @contact: 924207089@qq.com


import logging
from logging.handlers import TimedRotatingFileHandler


class HandleLog:
    """
    Wrap logging moudle.
    """
    def __init__(self):
        self.log = logging.getLogger("case")
        self.log.setLevel("INFO")

        if not self.log.handlers:
            file_handle = TimedRotatingFileHandler(
                "case",

            )




