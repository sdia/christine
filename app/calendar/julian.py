#!/usr/bin/env python
#-*- coding:utf-8 -*-




import convertdate
from _common import Calendar




class Julian(Calendar):

    calendar = convertdate.julian
    debug = False


if __name__ == '__main__':
    b=Julian()
    b.insert()
