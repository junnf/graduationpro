#!/usr/bin/env python
# encoding: utf-8

import tornado.web
import modle
import ujson as json
import md5
import traceback
import torndb

_dic = {}
_dep_dic = {}
_tea_dic = {}


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
        #test identity
        #get self.get_argument("identity")
        _user = self.get_argument("user")
        _pass = self.get_argument("password")
        _course = self.get_argument("course")
        _sex = self.get_argument("sex")
        try:
            self.db.execute("INSERT INTO user VALUES(NULL,'{}','{}','{}','{}');".format(_user,_pass,_course,_sex))
            self.write({"code":0,"information":"Register Successful"})
        except Exception, e:
            if tuple(e)[0] == 1062:
                self.write({"code":2,"information":"用户名不能重复"})


class CheckHandler(BaseHandler):

    def post(self):
        """
         {'check':'not found'}
        """
        _token = self.get_argument("token")
        #self.write("{'check','{}'}".format(_dic.get(_token,'not found')))
        #self.write("{'check':'{0}'}".format(_dic.get(_token,'not found')))
        if _dic.has_key(_token):
            self.write('{"code":"0"}')
        else:
            self.write('{"code":"1"}')


class LoginHandler(BaseHandler):

    def post(self):
        _user = self.get_argument("user")
        _pass = self.get_argument("password")
        #use rsa
        _t = md5.md5(_pass)
        token = _t.hexdigest()
        _dic[token] = _user
        self.write({"id":0,"information":"{}".format(token)})


class CourseDepHandler(BaseHandler):

    #教务处使用
    def post(self):
        _token = self.get_argument("token")
        if _dep_dic.has_key(_token):
            _course_name = self.get_argument("course_name")
            _teacher_num = self.get_argument("teacher_num")
            _detail = self.get_argument("detail")
            try:
                self.db.execute("INSERT INTO class VALUES(NULL,'{}','{}','{}');".format(_course_name, _teacher_num, _detail))
                self.write({"code":0,"information":"Add Course Successful"})
            except Exception, e:
                self.write('{"code":1,"information":"Add Course Fail!"}')
        else:
            self.write('{"code":2,"information":"Check identity Fail!"}')


class TeacherHandler(BaseHandler):

    def check_teacher(self):
        if _tea_dic.has_key("token"):
            return True
        else:
            return False


class StudentHandler(BaseHandler):

    def check_student(token):
        if _dic.has_key("token"):
            return True
        else:
            return False


class StudentPasswdHandler(StudentHandler):
    pass


class StudentGetCourse(StudentHandler):
    pass


class StudentInfoHandler(StudentHandler):

    def post(self):
        #student personal info edit
        _token = self.get_argument("token")
        if self.check_student(_token):
            _sex = self.get_argument("sex")
            _course_id = self.get_argument("course_id")
            _student_code = self.get_argument("student_code")
            try:
                pass
                #修改个人信息
                #self.db.excute("")
            except Exception, e:
                self.write('{"code":2,"information":"Edit Information Fail!"}')

    def get(self):
        ##Get Student Info
        _name = self.get_argument("name")
        _sex = self.get_argument("sex")
        _course_id = self.get_argument("course_id")
        _student_code = self.get_argument("student_code")




