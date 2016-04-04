#!/usr/bin/env python
# encoding: utf-8

import tornado.web
import modle
import md5


class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("user")

    @property
    def db(self):
        pass
        #  return self.application.db

class RegisterHandler(BaseHandler):

    def get(self):
        self.write("You get this message")

    def post(self):
        _user = self.get_argument("user")
        _pass = self.get_argument("pass")

class LoginHandler(BaseHandler):

    def post(self):
        _user = self.get_argument("user")
        _pass = self.get_argument("password")
        #use rsa
        _t = md5.md5(_pass)
        token = _t.hexdigest()
        with open("data/token.txt","w+") as f:
            f.write(token)
        self.write({"id":1,"information":"{}".format(token)})




