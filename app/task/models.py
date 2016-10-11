# -*- coding: utf-8 -*-
'''
Created on Sep 28, 2016

@author: guxiwen
'''

from sqlalchemy import *
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import *


Base = declarative_base()
class requirements_base(Base):
    __tablename__ = 'requirements_base'
    req_id = Column(Integer,primary_key=True)
    group_id = Column(Integer,default=1)
    name = Column(String(200),unique=False)
    raise_date = Column(Date)
    start_date = Column(Date)
    end_date = Column(Date)
    upline_date = Column(Date)
    raise_man = Column(String(100))
    test_man_id = Column(String(100))
    status = Column(Integer)
    assign_time = Column(Time)
    assign_id = Column(Integer)
    claim_time = Column(Time)
    claim_id = Column(Integer)
    leader_id = Column(Integer)