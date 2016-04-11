#!/usr/bin/env python
# encoding: utf-8

import tornado.web
import modle
import ujson as json
import md5
import traceback
import torndb

_dic = {}

class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("user")

    @property
    def db(self):
        return self.application.db


class RegisterHandler(BaseHandler):

    #test api
    def get(self):
        self.write("You get this message")

    def post(self):
        _user = self.get_argument("user")
        _pass = self.get_argument("password")
        _course = self.get_argument("course")
        _sex = self.get_argument("sex")
        try:
            self.db.execute("INSERT INTO user VALUES(NULL,'{}','{}','{}','{}');".format(_user,_pass,_course,_sex))
        except Exception, e:
            if tuple(e)[0] == 1062:
                self.write({"id":2,u"information":u"用户名不能重复"})



class LoginHandler(BaseHandler):

    def post(self):
        _user = self.get_argument("user")
        _pass = self.get_argument("password")
        #use rsa
        _t = md5.md5(_pass)
        token = _t.hexdigest()
        #  with open("data/token.txt","w+") as f:
            #  f.write(token)
        _dic[token] = _user
        self.write({"id":1,"information":"{}".format(token)})

class TableHandler(BaseHandler):

    def get(self,input):
        _temp = _dic.get(input,"")
        if _temp == "":
            self.write({"id":0,"information":"token is fault or not exist"})

    def post(self):
        """
            get class information use json
            0-6 weekday
            1-6 coursenum
            {
                "id":1,
                "data":{
                    "0":{
                       "1":{
                             "coursename":"xxx",
                             "courseid":int,
                             "teacher":"abc",
                             "extra":"是否存在其他课程"
                           }
                        }
                       }
            }
        """
        pass








