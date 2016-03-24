#!/usr/bin/env python
# encoding: utf-8

"""
File: apis.py
Author: junnliu
Email: junningliu@hustunique.com
Github: https://github.com/junnf
Description: graduation-project
"""

import os.path
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options

import modle
from tornado.options import options, define


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
               (r'/',Handler),
                ]
        settings = {
            "cookie_secret":"d2oEZ8T3TOqr1vhqDK2iIEilDgJ9OUO9lWyA+fGJ7tA=",
            "xsrf_cookies":True,
            "login_url":"/login",
            "template_path":os.path.join(os.path.dirname(__file__), "templates"),
            "static_path":os.path.join(os.path.dirname(__file__), "static"),
            "debug":True,
        }
        super(Application, self).__init__(handlers, **settings)
        self.db = torndb.Connection('127.0.0.1','blog','root','ljn7168396123')


class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return self.get_secure_cookie("user")

    @property
    def db(self):
        return self.application.db


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()

