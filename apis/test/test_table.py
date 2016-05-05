#!/usr/bin/env python
# encoding: utf-8

import torndb
import json

conn = torndb.Connection("127.0.0.1","course","root","ljn7168396")



def main(course_id, weeknum):
    _course_set = conn.query("SELECT * from \
            class_table a NATURAL JOIN class b \
            WHERE a.week_num = {} AND a.course_id = {}".format(weeknum, course_id))
    for x in _course_set:
        print x
        print "\n"
    #  print json.dumps(_course_set)



if __name__ == "__main__":
    main(1110001,1)

