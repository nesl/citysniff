#!/usr/bin/env python

import pysos
import time
import struct
import sqlite3
import os
import math

dbfile = "/home/thomas/citysniff.db"
MSG_OZONE = 115
MSG_SOUND = 116

class SosReceiver():

    def __init__(self):
        self.srv = pysos.sossrv(host="lcavpool63.epfl.ch")

        self.srv.register_trigger(self.soundDataMsgTrigger, 
                did=128,
                sid=128,
                type=MSG_SOUND)

        self.srv.register_trigger(self.ozoneDataMsgTrigger, 
                did=128,
                sid=128,
                type=MSG_OZONE)

        while 1:
            time.sleep(1)

    def soundDataMsgTrigger(self, m):
        (value,) = struct.unpack("<L", m['data'])
        db = sqlite3.connect(dbfile)
        cur = db.cursor()
        print time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()), math.log(value/512)
        cur.execute("insert into sound (time, value) values ('%s', %d)"%(time.strftime("%d %b %Y %H:%M:%S", time.localtime()), math.log(value/512)))
        db.commit()

    def ozoneDataMsgTrigger(self, m):
        (value,) = struct.unpack("<H", m['data'])
        db = sqlite3.connect(dbfile)
        cur = db.cursor()
        print 'ozone', time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()), value 
        cur.execute("insert into ozone (time, value) values ('%s', %d)"%(time.strftime("%d %b %Y %H:%M:%S", time.localtime()), value))
        db.commit()


if __name__ == "__main__":
    db = sqlite3.connect(dbfile)
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS sound (o_id INTEGER PRIMARY KEY AUTOINCREMENT, time TEXT, value REAL)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS ozone (o_id INTEGER PRIMARY KEY AUTOINCREMENT, time TEXT, value REAL)""")
    db.commit()
    db.close()
    sr = SosReceiver()
