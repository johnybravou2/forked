from typing import Annotated
from fastapi import FastAPI
from account import User




class System:
    def __init__(self):
        self.__list_user = []
    
    @property
    def list_user(self):
        return self.__list_user
    
    @list_user.setter
    def list_user(self,user):
        self.__list_user = user
        
    def add_user (self,user):
        self.__list_user.append(user)



