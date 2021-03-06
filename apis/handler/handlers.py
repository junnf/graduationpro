#!/usr/bin/env python
#decoding:utf-8
import tornado.web
import modle
import ujson as json
import md5
import traceback
import torndb

_dic = {}
_dep_dic = {}
#  _tea_dic = {}


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
        _uid = self.get_argument("uid")
        _user = self.get_argument("user")
        _pass = self.get_argument("password")
        _course = self.get_argument("course")
        _sex = self.get_argument("sex")
        try:
            self.db.execute("INSERT INTO user_student VALUES({},'{}',MD5('{}'),'{}','{}');".format(_uid,_user,_pass,_sex,_course))
            self.write({"code":0,"information":"Register Successful"})
        except Exception, e:
            if tuple(e)[0] == 1062:
                self.write({"code":2,"information":"用户名或学号不能重复"})


class CheckStuHandler(BaseHandler):
    """
        get method check
    """

    def post(self):
        """
         {'check':'not found'}
        """
        _token = self.get_argument("token")
        if _dic.has_key(_token):
            self.write('{"code":"0"}')
        else:
            self.write('{"code":"1"}')

class CheckDepHandler(BaseHandler):
    def post(self):
        _token = self.get_argument("token")
        if _dep_dic.has_key(_token):
            self.write('{"code":"0"}')
        else:
            self.write('{"code":"1"}')



class LoginHandler(BaseHandler):
    """
    code 0 成功
    code 1 密码错误
    code 2 未知错误
    code 3 不存在该用户
    """

    def post(self):
        _user = self.get_argument("user")
        _pass = self.get_argument("password")
        _ty = self.get_argument("ty")
        print type(_ty)
        if _ty == "0":
            try:
                _get = self.db.query("SELECT passwd FROM user_student WHERE name = '{}';".format(_user))
                _passmd5 = self.db.query("SELECT MD5('{}');".format(_pass))
                if _get == []:
                    self.write(json.dumps({"code":3,"information":"不存在该用户"}))
                    return
                else:
                    _get_paswdmd5 = _get[0]['passwd']
                    if _get_paswdmd5 == _passmd5[0].values()[0]:
                        _t = md5.md5(_pass)
                        token = _t.hexdigest()
                        _dic[token] = _user
                        #json_code 10 学生信息
                        self.write(
                            json.dumps({"code":10,"information":"{}".format(token)})
                            )
                    else:
                        self.write(
                            json.dumps({"code":1,"information":"密码错误"})
                            )
            except Exception, e:
                self.write(
                        json.dumps({"code":2,"information":"存在未知的错误"})
                        )
        elif _ty == "1":
            try:
                _get = self.db.query("SELECT passwd FROM user_dep WHERE name = '{}';".format(_user))
                _passmd5 = self.db.query("SELECT MD5('{}');".format(_pass))
                if _get == []:
                    self.write(json.dumps({"code":3,"information":"不存在该用户"}))
                    return
                else:
                    _get_paswdmd5 = _get[0]['passwd']
                    if _get_paswdmd5 == _passmd5[0].values()[0]:
                        _t = md5.md5(_pass)
                        token = _t.hexdigest()
                        _dep_dic[token] = _user
                        self.write(
                            json.dumps({"code":11,"information":"{}".format(token)})
                            )
                    else:
                        self.write(
                            json.dumps({"code":1,"information":"密码错误"})
                            )
            except Exception, e:
                self.write(
                        json.dumps({"code":2,"information":"存在未知的错误"})
                        )


class CoursedelDepHandler(BaseHandler):
    """
        教务处使用，删除课程信息
    """

    def post(self):
        _token = self.get_argument("token")
        _class_id = self.get_argument("class_id")
        if _dep_dic.has_key(_token):
            try:
                self.db.execute("DELETE FROM class WHERE class_id = {};".format(_class_id))
                self.db.execute("DELETE FROM class_table WHERE class_id = {};".format(_class_id))
                self.write(
                        json.dumps({"code":0,"information":"Delete Course Successful"})
                        )
            except Exception, e:
                self.write(
                        json.dumps({"code":1,"information":"Delete Course Fail!"})
                        )
        else:
            self.write(
                    json.dumps({"code":2,"information":"Check identity Fail!"})
                    )


class CourseaddDepHandler(BaseHandler):
    """
        教务处使用，增加课程信息
    """
    def post(self):
        _token = self.get_argument("token")
        if _dep_dic.has_key(_token):
            _course_name = self.get_argument("course_name").encode('utf-8')
	    print _course_name
	    print type(_course_name)
            _teacher_num = self.get_argument("teacher_name").encode('utf-8')
            _detail = self.get_argument("detail").encode('utf-8')
	    _course_id = self.get_argument("course_id").encode('utf-8')
            try:

                self.db.execute("INSERT INTO class VALUES({},'{}','{}','{}');".format(_course_id,_course_name, _teacher_num, _detail))
		self.write(
                        json.dumps({"code":0,"information":"Add Course Successful"})
                        )
            except Exception, e:
		print e
                self.write(
                        json.dumps({"code":1,"information":"Add Course Fail!"})
                        )
        else:
            self.write(
                    json.dumps({"code":2,"information":"Check identity Fail!"})
                    )

class CourseeditDepHandler(BaseHandler):
    """
        教务处使用，修改课程信息
    """

    def post(self):
        """
            根据class_id修改课程信息
        """
        _token = self.get_argument("token")
        if _dep_dic.has_key(_token):
            _class_id = self.get_argument("class_id")
            _class_name = self.get_argument("class_name")
            _teacher_name = self.get_argument("teacher_name")
            _other = self.get_argument("other")
            try:
                self.db.execute("UPDATE class SET class_name = '{}', \
                        teacher_name = '{}',other = '{}' WHERE  \
                        class_id = {};".format(_class_name, _teacher_name, _other,_class_id))

            except Exception, e:
                self.write(
                        json.dumps({"code":1,"information":"Add Course Fail!"})
                        )
        else:
            self.write(
                    json.dumps({"code":2,"information":"Check identity Fail!"})
                    )


class StudentHandler(BaseHandler):

    def check_student(self, token):
        if _dic.has_key(token):
            return True
        else:
            return False


class StudentPasswdeditHandler(StudentHandler):
    """
        学生修改密码
    """

    def check_student(self, token):
        if _dic.has_key(token):
            return _dic[token]
        else:
            return None

    def post(self):
        _token = self.get_argument("token")
        _passwd = self.get_argument("passwd")
        _get = self.check_student(_token)
        if _get == None:
            self.write(
                    json.dumps({"code":"2","information":"Please Login First!"})
                    )
        else:
            try:
                self.db.execute("UPDATE user_student set \
                        passwd = MD5('{}') where name = '{}'".format(_passwd,_dic[_token]))
            except Exception, e:
                self.write(
                        json.dumps({"code":"1","information":"修改密码失败"})
                        )


class StudentGetCourseTableHandler(StudentHandler):
    """
        得到教务处课表信息
    """

    def post(self):
        _course_id = self.get_argument("course_id")
        _week_num = self.get_argument("week_num")
	print _course_id,_week_num
        #  m = {}
        try:
            _get = self.db.query("select class_name, location, week_day, time \
                    from class a NATURAL JOIN class_table b WHERE week_num = {} \
                    AND course_id = {} ".format(_week_num,_course_id))
            if _get == []:
                self.write(json.dumps({"code":"1","information":"Table is null"}))
                return
            #  if len(_get) > 0:
                #  for x in _get:
                    #  m[(str(x['week_day'])+str(x['time']))] = x
            print _get
            self.write(json.dumps({"code":"0","information": _get}))

        except Exception, e:
            self.write(
                    json.dumps({"code":"2","information":"未知错误"})
                    )


class SearchCourseHandler(BaseHandler):
    """
        code 0 get class_info
        code 1 class not exists
        code 2 error
    """
    def post(self):
        _class_id = self.get_argument("class_id")
        try:
            _get = self.db.query("SELECT * FROM class WHERE class_id = '{}'".format(_class_id))
            if _get == []:
                self.write(
                        json.dumps({"code":1,"information":"课程号不存在"})
                        )
                return
            else:
                return_json = {
                        "code":0,
                        "information":
                                {
                                    "class_id":_get[0]['class_id'], "class_name": _get[0]['class_name'].encode('utf-8'),
                                    "teacher_name":_get[0]['teacher_name'].encode('utf-8'), "other":_get[0]['other'].encode('utf-8')
                                }
                            }
                self.write(
                        json.dumps(return_json)
                        )
        except Exception ,e:
            self.write(
                    json.dumps({"code":2,"information":"未知错误"})
                    )


class StudentInfoHandler(StudentHandler):
    """
        学生用户得到个人信息，修改个人信息

    """

    def post(self):
        #student personal info edit
        _token = self.get_argument("token")
       #_user 用来在SQL语句中的WHERE条件中起到作用
        _sex = self.get_argument("sex")
        _course_id = self.get_argument("course_id")
        _student_code = self.get_argument("student_code")

        if self.check_student(_token):
            _user = _dic[_token]
            #_user 用来在SQL语句中的WHERE条件中起到作用
            try:
                #修改个人信息
                self.db.execute("UPDATE user_student SET sexuality = {}, \
                        course_id = {}, uid = {} where name = '{}'".format(_sex,_course_id,_student_code,_user))
                self.write(
                        json.dumps({"code":0,"information":"修改信息成功"})
                        )
            except Exception, e:
                self.write(
                        json.dumps({"code":3,"information":"修改信息失败"})
                        )
        else:
            #Login Fail
            self.write(
                    json.dumps({"code":"2","information":"验证超时,请先登录"})
                    )

    def get(self, token):
        ##Get Student Info
        if self.check_student(token):
            _user = _dic[token]
            try:
                _get = self.db.query("SELECT uid,name,sexuality,course_id from user_student where name = '{}'".format(_user))
                if len(_get) > 0:
                    self.write(
			    json.dumps({"code":0,"information":{"uid":_get[0]['uid'],
				"name":_get[0]['name'],
				"sexuality":_get[0]['sexuality'],
				"course_id":_get[0]['course_id']}})
                        )
            except Exception, e:
                self.write(
                        json.dumps({"code":4,"information":"Query Fail"})
                        )
        else:
            self.write(
                    json.dumps({"code":"2","information":"Please Login First!"})
                    )

class DelCourseTableHandler(BaseHandler):
    def post(self):
        _token = self.get_argument("token")
        _delete_course_id = self.get_argument("course_id")
        _delete_week_num = self.get_argument("week_num")
        if _dep_dic.has_key(_token):
            try:
                self.db.execute("DELETE FROM class_table WHERE week_num = {} \
                    and course_id = {};".format(_delete_week_num,_delete_course_id))
                self.write(
                        json.dumps({"code":"0","information":"删除成功"})
                        )
            except Exception,e:
                self.write(
                        json.dumps({"code":"2","information":"未知错误"})
                        )



class AddCourseTableHandler(BaseHandler):
    """
        添加课表信息
    """

    def post(self):
        """
            教务处添加课表信息
        """
        #  _course_id = self.get_argument("course_id")
        #  _week_num = self.get_argument("week_num")
        #test data
        jsondata = '{"week_num":1,"course_id":1110001,"content":\
        [{"week_day":0,"time":1,"location":"西十二 N201","class_id":"1110001"}\
        ,{"week_day":0,"time":2,"location":"西十二 N203","class_id":"1110002"}]}'

        _token = self.get_argument("token")
        _json = self.get_argument("json")
        if _dep_dic.has_key(_token):
            obj = json.loads(_json)
            weeknum = obj['week_num']
            course_id = obj['course_id']
            _content = obj['content']
            for course in _content:
                try:
                    self.db.execute('INSERT INTO class_table VALUES\
                            ({},{},{},{},"{}",{})'.format(
                                course_id,
                                weeknum,
                                course['week_day'],
                                course['time'],
                                course['location'].encode('utf-8'),
                                course['class_id'])
                            )
                except Exception, e:
                    if tuple(e)[0] == 1062:
                        self.write(
                            json.dumps({"code":"2","information":"{} 课程添加重复".format(course['class_id'])})
                            )
                    else:
                        self.write(
                                json.dumps({"code":"3","information":"未知错误"})
                                )


class TestHandler(BaseHandler):
    def post(self):
        course_name = self.get_argument("course_name")
        print "test"
        self.write(
                json.dumps({"code":"2","information":course_name})
                )

class TestCourseaddDepHandler(BaseHandler):

    """
        教务处使用，增加课程信息
    """
    def post(self):
        _course_name = self.get_argument("course_name")
        print _course_name
        _teacher_num = self.get_argument("teacher_name")
        _detail = self.get_argument("detail")
        _course_id = self.get_argument("course_id")
        try:
            self.write(
                json.dumps({"code":0,"information":"Add Course Successful"})
            )
        except:
            pass


class StudentFriendListHandler(StudentHandler):
    """
        获得学生列表

    """

    def post(self):
        #student personal info edit
        _token = self.get_argument("token")
        #_user = self.get_argument("user")
       #_user 用来在SQL语句中的WHERE条件中起到作用

        if self.check_student(_token):
            _user = _dic[_token]
            #_user 用来在SQL语句中的WHERE条件中起到作用
            try:
                #修改个人信息
                _json = self.db.query("select friend_name from user_friend where name = '{}'".format(_user))
            	self.write(
                    json.dumps({"code":"0","information": _json})
                    )


            except Exception, e:
                self.write(
                        json.dumps({"code":3,"information":"修改信息失败"})
                        )
        else:
            #Login Fail
            self.write(
                    json.dumps({"code":"2","information":"未知错误"})
                    )


class StudentFriendAddHandler(StudentHandler):
    """
        添加好友

    """

    def post(self):
        #student personal info edit
        _token = self.get_argument("token")
        _friend = self.get_argument("friend")
       #_user 用来在SQL语句中的WHERE条件中起到作用

        if self.check_student(_token):
            _user = _dic[_token]
            #_user 用来在SQL语句中的WHERE条件中起到作用
            try:
                _temp = self.db.query("select * from user_friend where name = '{}' and friend_name = '{}'".format(_user,_friend))
                if _temp != []:
                    self.write(
                        json.dumps({"code":1,"information":"该好友已经在您好友列表中"})
                        )
                else:
                    if self.db.query("select * from user_student where name = '{}'".format(_friend)) == []:
                        self.write(
                            json.dumps({"code":2,"information":"该用户不存在"})
                        )
                    else:
                        self.db.execute("insert into user_friend values(null,'{}','{}')".format(_user, _friend))
                        self.write(
                            json.dumps({"code":0,"information":"添加好友成功"})
                        )


            except Exception, e:
                self.write(
                        json.dumps({"code":3,"information":"存在未知错误"})
                        )
        else:
            #Login Fail
            self.write(
                    json.dumps({"code":"2","information":"未知错误"})
                    )


class StudentFriendDelHandler(StudentHandler):
    """
       删除好友

    """

    def post(self):
        #student personal info edit
        _token = self.get_argument("token")
        _friend = self.get_argument("friend")
       #_user 用来在SQL语句中的WHERE条件中起到作用

        if self.check_student(_token):
            _user = _dic[_token]
            #_user 用来在SQL语句中的WHERE条件中起到作用
            try:
                self.db.execute("delete from user_friend where name = '{}' \
                        and friend_name = '{}'".format(_user, _friend))
                self.write(
                    json.dumps({"code":0,"information":"删除好友成功"})
                )
            except Exception, e:
                self.write(
                        json.dumps({"code":3,"information":"存在未知错误"})
                        )
        else:
            self.write(
                    json.dumps({"code":"2","information":"未知错误"})
                    )

class SendMessageHandler(StudentHandler):
    """
        发送信息
    """

    def post(self):
        _token = self.get_argument("token")
        _friend = self.get_argument("friend")
        _content = self.get_argument("content")

        if self.check_student(_token):

            _user = _dic[_token]
	    print _user, _friend, _content
            try:
                self.db.execute("insert into message values(null,\
                        '{}','{}','{}',null)".format(_user, _friend, _content.encode('utf-8')))
                self.write(
                    json.dumps({"code":0,"information":"发送成功"})
                )
            except Exception, e:
                self.write(
                        json.dumps({"code":3,"information":"存在未知错误"})
                        )



class GetMessageListHandler(StudentHandler):

    def post(self):
        _token = self.get_argument("token")
	_msg = []
        if self.check_student(_token):
            _user = _dic[_token]
            try:
                _get = self.db.query("select send, content, time from message where object \
                        = '{}' order by time DESC".format(_user))
                if _get == []:
                    #if no message
                    return
		else:
                    for x in _get:
			#_msg.append("发送自")
			
			_msg.append("发送自:{}  \t".format(x['send'])  
				+ "{}-{}-{} {}:{}".format(x['time'].year, x['time'].month, x['time'].day, 
				    (x['time'].hour+8)%24, x['time'].minute) + "  " +  x['content'].encode('utf-8')
				)
                self.write(
                    json.dumps({"code":0,"information":_msg})
                )
            except Exception, e:
                self.write(
                        json.dumps({"code":3,"information":"存在未知错误"})
                        )

class AHandler(BaseHandler):
    def get(self):
	pass
