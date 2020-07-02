#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 20:43
# @Author  : xujiajun
# @Site    : 
# @File    : handle_conf.py
# @Software: PyCharm
# @contact: 924207089@qq.com


from configparser import ConfigParser
from util.handle_dir import CONF_FILE


class HandleConf(ConfigParser):
    """
    Wrap handle-config moudle.
    """
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.read(self.filename)

    def get_value(self, section, option):
        """
        Gain data from config file.
        :param section:
        :param option:
        :return:
        """
        return self.get(section, option)

    def get_int(self, section, option):
        """
        Gain type:int data from config file.
        :param section:
        :param option:
        :return:
        """
        return self.getint(section, option)

    def get_float(self, section, option):
        """
        Gain type:float data from config file.
        :param section:
        :param option:
        :return:
        """
        return self.getfloat(section, option)

    def get_eval_data(self, section, option):
        """
        Gain raw data from config file,then user method "eval()"
        :param section:
        :param option:
        :return:
        """
        return eval(self.get(section, option))

    def write_conf(self, data, filename=None):
        """
        Write data into config file.
        :param data:
        :param filename:
        :return:
        """
        filename = filename if filename else self.filename
        if isinstance(data, dict):
            for _ in data:
                self[_] = data[_]
            with open(filename, "w") as file:
                self.write(file)
        else:
            raise TypeError("Data type is error!")


do_conf = HandleConf(CONF_FILE)


if __name__ == '__main__':
    do_conf = HandleConf(r"..\conf\conf.ini")
    captcha_url = do_conf.get_value("url", "captcha_url")
    SQL = do_conf.get_value("sql", "identity_sql")
    print(captcha_url, type(captcha_url))
