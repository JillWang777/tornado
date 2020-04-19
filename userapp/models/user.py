# -*- coding: utf-8 -*-
# Author：ala
# @Date   : 2020/4/19 10:34
# @Project : userapp
# @File    : user.py

#用户模型，通常会使用orm框架实现和数据库的交互
class UserModel(object):

    users = {
        1: {'name':'zhang','age':10},
        2: {'name': 'wang', 'age': 20},
        3: {'name': 'li', 'age': 30},
        4: {'name': 'zhao', 'age': 40},
    }

    @classmethod
    def get(cls,user_id):
        return cls.users[user_id]

    @classmethod
    def get_all(cls):
        return list(cls.users.values())

    @classmethod
    def create(cls,name,age):
        user_dict = {'name':name,'age':age}
        max_id = max(cls.users.keys()) + 1
        cls.users[max_id] = user_dict

    @classmethod
    def update(cls,user_id,age):
        cls.users[user_id]['age'] = age

    @classmethod
    def delete(cls,user_id):
        if user_id in cls.users:
            return cls.users.pop(user_id)