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

from tornado.options import options
from modle import decorators
import handler
from handler import *
from setting import *
import torndb

_dic = {}

class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
               (r'/register',RegisterHandler),
               (r'/login',LoginHandler),
               (r'/check',CheckStuHandler),
               (r'/checkdep',CheckDepHandler),
               (r'/gettable',StudentGetCourseTableHandler),
               (r'/searchcourse',SearchCourseHandler),
               (r'/dep/addcourse',CourseaddDepHandler),
               (r'/dep/delcourse',CoursedelDepHandler),
               (r'/passwd',StudentPasswdeditHandler),
               (r'/student/info/(\w+)',StudentInfoHandler),
               (r'/student/editinfo',StudentInfoHandler)
                ]
        settings = {
            "cookie_secret":"d2oEZ8T3TOqr1vhqDK2iIEilDgJ9OUO9lWyA+fGJ7tA=",
            "login_url":"/login",
            "template_path":os.path.join(os.path.dirname(__file__), "templates"),
            "static_path":os.path.join(os.path.dirname(__file__), "static"),
            "debug":True,
        }
        super(Application, self).__init__(handlers, **settings)
        self.db = torndb.Connection(options.host, options.dbname, options.user, options.password)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
