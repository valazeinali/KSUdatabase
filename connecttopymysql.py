#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
#                                                          #
# Simple script to connect to a remote mysql database      #
#                                                          #
#                                                          #
############################################################

import pymysql as db

# HOST = "dbdev.cs.kent.edu"
# PORT = 3306
# USER = "mhossai2"
# PASSWORD = ""
# DB = "university"

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = "root"
DB = "university"

connection = db.Connection(host=HOST, port=PORT, user=USER, passwd="", db=DB) # create database connecition
try:
    dbhandler = connection.cursor() # create a cursor object
    dbhandler.execute("select * from instructor;") # exceute the query
    result = dbhandler.fetchall() # fetch all data from the cursor area
    for item in result:  # result is a two dimensional array now, print using two loops.
        for it in item:
            print (it, " ",)
        print ("\n")

except Exception as e:
    print (e)

finally:
    connection.close()
