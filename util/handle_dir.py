#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 15:25
# @Author  : xujiajun
# @Site    : 
# @File    : handle_dir.py
# @Software: PyCharm
# @contact: 924207089@qq.com


import os

# Diretory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASE_DIR = os.path.join(BASE_DIR, "case")
CONF_DIR = os.path.join(BASE_DIR, "conf")
DATA_DIR = os.path.join(BASE_DIR, "data")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
UTIL_DIR = os.path.join(BASE_DIR, "util")

# File_Path
CONF_FILE = os.path.join(CONF_DIR, "conf.ini")
CASE_FILE = os.path.join(DATA_DIR, "cases.xls")
LOG_FILE = os.path.join(LOGS_DIR, "case.log")
