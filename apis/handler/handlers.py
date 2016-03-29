#!/usr/bin/env python
# encoding: utf-8
import tornado.web
import modle

class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("user")

    #  @property
    #  def db(self):
        #  return self.application.db

class LoginHandler(BaseHandler):

    def get(self):
        self.write("You get this message")

    def post(self):
        _user = self.get_argument("user")
        _pass = self.get_argument("pass")



