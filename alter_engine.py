#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 11:31
# @Author  : wuuu__
# @File    : alter_engine.py
# @Software: PyCharm
import   pymysql
import  time



def  get_connetion():
    db = pymysql.connect(host='192.168.106.134',
                         port=3306,
                         user='axe',
                         password='root.2018')
    cursor = db.cursor()
    cursor.close()
    db.close()
def get_tables():
    # db=pymysql.connect(host='192.168.106.134',
    #                port=3306,
    #                user='axe',
    #                password='root.2018')
    # cursor=db.cursor()
    sql=''' select  table_name  from information_schema.tables where table_schema='axe'; '''
    cursor.execute(sql)
    data =cursor.fetchall()
    return  data
    print(data)
    cursor.close()
    db.close()

def alter_tables(table_name):
    db=pymysql.connect(host='192.168.106.134',
                   port=3306,
                   user='axe',
                   password='root.2018',
                   database='axe')
    cursor=db.cursor()

    sql=''' alter table  %s engine=innodb ; '''
    cursor.execute(sql%table_name)
    print(sql%(table_name))
    # time.sleep(30)
    db.commit()
    cursor.close()
    db.close()

# a=alter_tables('axe')
def main():
    a=get_tables()
    for i, in a :
        # print(i)
        alter_tables(i)
        time.sleep(5)

if __name__ == '__main__':
    main()
