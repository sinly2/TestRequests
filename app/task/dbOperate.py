# -*- coding: utf-8 -*-
'''
Created on Sep 28, 2016

@author: guxiwen
'''
import datetime

from app.config import Util
from models import *


class dbOperate(object):
    def __init__(self):
        self.engine = create_engine(Util.db_task,echo=True)
        DB_Session = sessionmaker(bind=self.engine)
        self.session = DB_Session()
    def init_db(self):
        Base.metadata.create_all(self.engine)
        
    def drop_db(self):
        Base.metadata.drop_all(self.engine)
        
    def query_db(self,db):
        query = self.session.query(db)
        return query
    
    def insert_db(self,lists):
        #参数举例[[日期,需求],[日期，需求]]
        for req in lists:
            tmp = requirements_base()
            tmp.raise_date = datetime.datetime.strptime(req[0],'%Y%m%d').date()
            tmp.name = req[1]
            tmp.raise_man = req[2]
            self.session.add(tmp)
            self.session.commit()
# query = session.query(requirements_base)
# print query.filter(requirements_base.req_id==1).first().name
if __name__ == '__main__':
    db = dbOperate()
    db.init_db()
    qy = db.query_db(requirements_base)
    print 'ok'
    print type(qy)
    print qy.first().name