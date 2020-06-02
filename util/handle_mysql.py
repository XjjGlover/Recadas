#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 12:11
# @Author  : xujiajun
# @Site    : 
# @File    : handle_mysql.py
# @Software: PyCharm
# @contact: 924207089@qq.com


import pymysql


class HandleMysql:
    """
    Wrap mysql moudle.
    """
    def __init__(self):
        self.conn = pymysql.connect(host='119.23.49.157',
                                    port=3306, user='root',
                                    passwd='Reconova$123',
                                    db='vehicle-test'
                                    )
        self.cursor = self.conn.cursor()

    def __call__(self, sql, arg=None, more=None):
        """
        Execute sql statement,then return the result needed.
        :param sql:sql statement
        :param arg:arguments
        :param more: return all results or not
        :return:The result of sql statement executed.
        """
        self.cursor.execute(sql, arg)
        try:
            _ = bool(more)
        except Exception as e:
            print("Incorrect argument.")
            raise e
        if _:
            result = self.cursor.fetchone()
        else:
            result = self.cursor.fetchall()
        return result

    def close(self):
        """
        Close connection.
        :return:
        """
        self.cursor.close()
        self.conn.close()


do_mysql = HandleMysql()


if __name__ == '__main__':
    do_mysql = HandleMysql()
    sql = "SELECT t2.org_name as company_name,t.company_no,t1.id as user_id,t.org_name,t1.real_name,t3.id as role_id,t3.role_name,t3.role_type\
            FROM t_ascs_vmp_org t,t_ascs_vmp_user t1,t_ascs_vmp_org t2,t_ascs_vmp_role t3,t_ascs_vmp_account_role_relationship t4\
            WHERE t.id = t1.org_id and t.id = t2.id and t2.parent_org_id = 0 and t.id = t3.company_id and t.id = t4.company_id and t4.account_id = t1.id and t4.role_id = t3.id and t1.company_no = 'csb' and t1.username = 'admin';"
    print(do_mysql(sql))

