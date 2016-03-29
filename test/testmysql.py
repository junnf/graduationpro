#!/usr/bin/env python
# encoding: utf-8

import sqlalchemy

class User(object):

    """Docstring for User. """

    def __init__(self, id, name, passwd, profession_id,
            sex, grade, _class, tel, old):
        """TODO: to be defined1. """
        self.id = id
        self.name = name
        self.passwd = passwd
        self.profession_id = profession_id
        self.sex = sex
        self.grade = grade
        self._class = _class
        self.tel = tel
        self.old = old



