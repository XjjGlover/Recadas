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
from threading import Lock


class HandleLog:
    """
    Wrap logging moudle.
    """
    def __init__(self):
        self.mutex = Lock()
        self.formatter = "%(asctime)s - [%(levelname)s] - %(module)s - %(name)s - %(lineno)d - [日志信息]：%(message)s"

    def _creat_logger(self):
        """
        Create Logger
        :return:
        """
        _logger = logging.getLogger(__name__)
        _logger.setLevel(logging.INFO)
        return _logger

    def _console_handler(self):
        """
        Create console handler
        :return:
        """
        _console_handler = logging.StreamHandler()
        _console_handler.setFormatter(logging.Formatter(self.formatter))
        _console_handler.setLevel(logging.INFO)
        return _console_handler

    def _file_handler(self):
        """
        Create file handler
        :return:
        """
        _file_handler = TimedRotatingFileHandler(filename="..\logs\case.log",
                                                 when="d",
                                                 interval=1,
                                                 backupCount=5,
                                                 encoding="utf-8"
                                                 )
        _file_handler.setFormatter(logging.Formatter(self.formatter))
        _file_handler.setLevel(logging.INFO)
        return _file_handler

    def pub_logger(self):
        logger = self._creat_logger()
        self.mutex.acquire()
        logger.addHandler(self._console_handler())
        logger.addHandler(self._file_handler())
        self.mutex.release()
        return logger


do_log = HandleLog().pub_logger()


if __name__ == '__main__':
    logger = HandleLog().pub_logger()
    while True:
        logger.warning("info")
        logger.warning("warning")