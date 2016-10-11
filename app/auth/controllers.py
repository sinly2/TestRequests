'''
Created on Oct 2, 2016

@author: guxiwen
'''
from app.models import *

class authControllers(object):
    @staticmethod
    def get_id_by_username(username):
        cu = user_info.query.filter(user_info.user_name==username).first()
        if cu is None:
            return None
        return str(cu.user_id)

    @staticmethod
    def get_username_by_id(user_id):
        cu = user_info.query.filter(user_info.user_id==user_id).first()
        if cu is None:
            return None
        return str(cu.user_name)
    @staticmethod
    def get_user_info_id(user_id):
        return user_info.query.filter(user_info.user_id==user_id).first()
    
    
    @staticmethod
    def verify_password(username,password):
        cu = user_info.query.filter(user_info.user_name==username,user_info.password==password).first()
        if cu is None:
            return False
        return cu
        
if __name__ == "__main__":
    authControllers.get_id_by_username('xixi')