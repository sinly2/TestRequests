# -*- coding: utf-8 -*-
'''
Created on Sep 28, 2016

@author: guxiwen
'''
import sys
sys.path.append('/root/project/TestRequests')
from addRequests import addRequests

def add_requests():
    addRequests.init_redis()
    to_do_list = addRequests.update_svn()
    print len(to_do_list)
    if len(to_do_list) <> 0:
        addRequests.update_redis(to_do_list)
        addRequests.insert_req_into_db(to_do_list)
add_requests()