#!/usr/bin/env python
# encoding: utf-8

from tornado.options import define

define("port",default=8000,help="nothing",type=int)
define("host",default='127.0.0.1',help="nothing",type=str)
define("dbname",default="course",help="nothing",type=str)
define("user",default="root",help="nothing",type=str)

define("password",default="ljn7168396",help="nothing",type=str)

