#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 21:06
# @Author  : xujiajun
# @Site    : 
# @File    : run.py.py
# @Software: PyCharm
# @contact: 924207089@qq.com


import unittest
import os,sys
from case.login import TestLogin
from util.get_data import GetToken

# Add enviroment-virable.
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)
sys.path.append(r"C:\Users\86188\AppData\Local\Programs\Python\Python37\Lib\site-packages")

# result = unittest.TextTestResult(sys.stdout, 'test result', 1)
suite = unittest.TestSuite()
case = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
suite.addTests(case)
runner = unittest.TextTestRunner(verbosity=1)
runner.run(suite)
token = getattr(GetToken, "token", "a")
print(token)
