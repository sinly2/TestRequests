# -*- coding: utf-8 -*-
'''
Created on Sep 27, 2016

@author: guxiwen
'''
import os
import datetime
import time
import redis
from  app.config import Util
from  models import *
from  dbOperate import dbOperate

class addRequests(object):
    @staticmethod
    def connect_db():
        db = dbOperate()
        db.init_db()
        return db
    @staticmethod
    def update_svn():
        #更新svn目录，检查是否有需求新增加
        #第一次使用需要先手动把svn路径checkout到本地
        #os.system('svn update')
        pwds = Util.svn_path.split(",")
        now_date = addRequests.get_nowdate()
        to_do_list = []
        for pwd in pwds:
            os.system('svn update '+pwd)
            dirs = os.listdir(pwd)
            for dirname in dirs:
                if dirname == ".svn":
                    continue
                else:
                    tmp = dirname.split("-")
                    date = datetime.datetime.strptime(tmp[0],'%Y%m%d').date()
                    if str(date) < str(now_date):
                        continue
                    elif addRequests.is_exists_in_redis(tmp[1]):
    #                     print 'ooooooooooooo'
                        continue
                    elif addRequests.is_exists_in_db(tmp[1]):
                        print tmp[1]
    #                     print 'sssssssssssss'
                        addRequests.update_redis([tmp])
                    else:
                        svn_cmd = 'svn info "' + pwd.encode('utf8') + "/"+ dirname.encode('utf8') + '"|grep Author'
                        print svn_cmd
                        result = os.popen(svn_cmd)
                        result = result.readlines()
                        print result
                        if result is not None:
                            tmp.append(result[0].split(':')[1].strip())
    #                     print 'pppppppppppppppppp'
                        to_do_list.append(tmp)
        return to_do_list
    
    @staticmethod
    def init_redis():
        #从数据库取当天的需求，存入redis
        #当天只需最早的时候操作一次，后面的改动会实时同步redis
        r = redis.Redis(Util.redis_host,Util.redis_port,db=Util.redis_db)
        r.flushdb()
        query = addRequests.connect_db().query_db(requirements_base)
        nowdate = addRequests.get_nowdate()
        nowdate_reqs = query.filter(requirements_base.raise_date == nowdate).all()
        #如果数据库中不存在当天需求，则无需处理redis；如果存在，则需写入redis
        if len(nowdate_reqs) == 0:
            print '111'
        else:
            for req in nowdate_reqs:
                r.set(req.name,req.raise_date)
        
    @staticmethod
    def is_exists_in_redis(key):
        #判断是否在redis中存在，如果存在返回true
        r = redis.Redis(Util.redis_host,Util.redis_port,db=Util.redis_db)
        if r.get(key) is None:
            return False
        else:
            return True
   
    @staticmethod
    def is_exists_in_db(key):
        if addRequests.connect_db().query_db(requirements_base).filter(requirements_base.name == key).all() is not None and \
        len(addRequests.connect_db().query_db(requirements_base).filter(requirements_base.name == key).all()) <>0:
            return True
        else:
            return False

    @staticmethod
    def update_redis(lists):
        #将本日新增的需求插入redis
        #参数举例[[日期,需求],[日期，需求]]
        r = redis.Redis(Util.redis_host,Util.redis_port,db=Util.redis_db)
        for key in lists:
            r.set(key[1],key[0])
   
    @staticmethod
    def get_nowdate():
        return time.strftime('%Y-%m-%d',time.localtime(time.time()))
    
    @staticmethod
    def insert_req_into_db(lists):
        #将本日新增需求插入数据库
        #参数举例[[日期,需求],[日期，需求]]
        addRequests.connect_db().insert_db(lists)
        
if __name__ == "__main__":
#     a = addRequests.update_svn()
#     addRequests.update_redis(a)
#     addRequests.init_redis()
#     addRequests.is_exists_in_redis('gu')
#     addRequests.is_exists_in_redis('gi')
#     addRequests.update_redis([[20110101,12],[20138723,33]])
    print addRequests.is_exists_in_db(u'O2O技术年费退费定位')