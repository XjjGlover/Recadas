#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 20:05
# @Author  : xujiajun
# @Site    : 
# @File    : handle_excel.py
# @Software: PyCharm
# @contact: 924207089@qq.com
from collections import namedtuple
import xlrd
import xlwt
from xlutils.copy import copy


class HandleExcel:
    def __init__(self, filename, sheetname=None):
        self.filename = filename
        self.sheetname = sheetname
        self.file = xlrd.open_workbook(self.filename)
        self.sheet = self.file.sheet_by_index(0) if self.sheetname is None else self.file.sheet_by_name(self.sheetname)
        index_tuple = self.sheet.row_values(0)
        self.case_tuple = namedtuple("case_tuple", index_tuple)
        self.case_list = []

    def get_cases(self):
        """
        Gain all test cases by moudle xlrd
        :return:list
        """
        for row in range(1, self.sheet.nrows):
            self.case_list.append(self.case_tuple._make(self.sheet.row_values(row)))
        return self.case_list

    def get_case(self, row):
        """
        Gain all a single test case by moudle xlrd
        :return:list
        """
        if isinstance(row, int) and row <= self.sheet.nrows:
            return self.case_list.append(self.case_tuple._make(self.sheet.row_values(row)))
        else:
            print("your parameter is incorrect!")

    def write_res(self, row, actual, result):
        """
        Put result an actual to data(excel) after case executed.
        :param row:
        :param actual:
        :param result:
        :return:
        """
        wb = copy(self.file)
        sheet = wb.get_sheet(0)
        sheet.write(row, 5, actual)
        sheet.write(row, 6, result)
        wb.save(self.filename)


do_excel = HandleExcel(r"..\data\cases.xls")


if __name__ == '__main__':
    do_excel = HandleExcel(r"..\data\cases.xls")
    print(do_excel.get_cases()[0])
    print(list(do_excel.get_cases()[0]))
    print(len(do_excel.get_cases()))
