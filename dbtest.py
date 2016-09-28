#!/usr/bin/python
# -*- coding: utf-8 -*-
import readTest as r
import MySQLdb as mdb

mysqlAddress = 'localhost'
userName = 'root'
password = '123456'
dbName = 'trauma'


def insert_db(fileName):
    con = mdb.connect(mysqlAddress, userName, password, dbName)

    file = open(fileName)
    line = file.readline()

    while line:
        if(line !='' and line !='\n'):
            list = r.parse_front(line) # read every line, parse the line and insert into mysql
            dict = r.parse_rear(line)

            with con:
                for (k, v) in dict.items():
                    sql = "INSERT INTO data(lineNumber, AcctNo, lineNumberForEachAcctNo, TableName, TimeStamp, FieldName, FieldValue) " \
                       "VALUES (%s,%s,%s,%s,%s,%s,%s)", \
                       (list[0], list[1], list[2], list[3], list[4], k, v)
                    #print(sql)
                    cur = con.cursor()
                    cur.execute(*sql)
                con.commit()

        line = file.readline()
    file.close()
    print("*******************************")
    print("successful")
    print("*******************************")
    return



