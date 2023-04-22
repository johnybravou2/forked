from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from account import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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

    def get_user(self,username: str):
        for user in self.__list_user:
            if user._contact_username == username:
                return user
        
    def check_user (self,username,password):
        for user in self.__list_user:
            if user._contact_username == username:
                if user._contact_password == password:
                    return True
        return False


    def fake_decode_token(self,token):
        # This doesn't provide any security at all
        # Check the next version
        user = self.get_user(token)
        return user


    async def get_current_user(self,token: Annotated[str, Depends(oauth2_scheme)]):
        user = self.fake_decode_token(token)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return 