#!/usr/bin/env python
# encoding: utf-8
from functools import wraps
import ujson as json
import copy

class LoginMessage(object):
    """
        code:,message
        return json_stirng
    """

    def __init__(self,code,message):
        self.login_message = {
            "login_code":code,
            "login_message":message
        }

    def __repr__(self):
        return json.dumps(self.login_message)

def json_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args,**kwargs))
    return wrapper

def main():
    ob = LoginMessage(1,"nihao")
    print ob

if __name__ == "__main__":
    main()

