#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import datetime
from functools import wraps


def timestamp():
    """timestamp"""
    return time.time()


def dt_strftime(fmt="%Y%m"):
    """
    datetime format
    :param fmt "%Y%m%d %H%M%S
    """
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """
    sleep time
    """
    time.sleep(seconds)


def running_time(func):
    """function running time"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        print("Data inspection done! Use %.3f seconds!" % (timestamp() - start))
        return res

    return wrapper


if __name__ == '__main__':
    print(dt_strftime("%Y%m%d%H%M%S"))