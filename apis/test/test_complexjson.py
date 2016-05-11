#!/usr/bin/env python
# encoding: utf-8
import torndb
import json

conn = torndb.Connection('127.0.0.1','course','root','ljn7168396')

jsondata = '{"week_num":1,"course_id":1110001,"content":\
[{"week_day":0,"time":1,"location":"西十二 N201","class_id":"1110001"}\
,{"week_day":0,"time":2,"location":"西十二 N203","class_id":"1110002"}]}'

obj = json.loads(jsondata)
weeknum = obj['week_num']
course_id = obj['course_id']
_content = obj['content']
for course in _content:
    try:
        conn.execute('INSERT INTO class_table VALUES\
                ({},{},{},{},"{}",{})'.format(
                    course_id,
                    weeknum,
                    course['week_day'],
                    course['time'],
                    course['location'].encode('utf-8'),
                    course['class_id'])
                )
    except Exception,e:
        print tuple(e)[0]



