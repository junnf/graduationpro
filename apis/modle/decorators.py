#!/usr/bin/env python
# encoding: utf-8
from functools import wraps
import ujson as json

def json_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args,**kwargs))
    return wrapper

def main():
    pass

if __name__ == "__main__":
    main()

