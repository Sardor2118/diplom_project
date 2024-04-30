from fastapi import Request, APIRouter
from pydantic import BaseModel
from typing import List, Dict
from database.userservice import register_user_db, check_user_db, check_user_password_db, change_user_data, \
    profile_info_db

# import re

user_router = APIRouter(prefix="/users", tags=["Управление пользователями"])


# regex = re.compile(r'([A-za-z0-9]+[.-_])*[A-za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z]a-z]{2,})+')

# def mail_checker(email, regex):
#     if re.fullmatch(regex, email):
#         return True
#     return False
class User(BaseModel):
    username: str
    email: str
    phone_number: str
    password: str


@user_router.post("/api/registration")
async def register_user(user_model: User):
    user_data = dict(user_model)
    # regex = re.compile(r'([A-za-z0-9]+[.-_])*[A-za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z]a-z]{2,})+')
    # mail_validation = mail_checker(regex, user_model.email)
    check = check_user_db(email=user_model.email,
                          phone_number=user_model.phone_number)
    if check:
        reg_user = register_user_db(**user_data)
        if reg_user is not None:
            return {"status": 1, "user_id": reg_user}
        else:
            return {"status": 0, "message": "Failed to register user"}
    else:
        return {"status": 0, "message": "Invalid email or phone number"}
    # if mail_validation:
    #     if check:
    #         try:
    #             reg_user = register_user_db(**user_data)
    #             return {"status": 1, "user_id": reg_user}
    #         except Exception as e:
    #             return {"status": 0, "message":  e}
    # return {"status": 0, "message": "Invalid email or phone number"}


# получение данных о пользователе
@user_router.get("/api/user")
async def get_user(user_id: int):
    exact_user = profile_info_db(user_id=user_id)
    return {"status": 1, "message": exact_user}


# вход в аккаунт
@user_router.post("/api/user")
async def login_user(email: str, password: str):
    # mail_validator = mail_checker(email)
    if True:
        login_checker = check_user_password_db(email=email, password=password)
        if login_checker:
            return {"status": 1, "message": login_checker}
        return {"status": 0, "message": login_checker}
    return {"status": 0, "message": "Invalid email"}


# запрос на изменение информации о юзере
@user_router.put("/api/change_profile")
async def change_user_profile(user_id: int, changeable_info: str, new_data: str):
    data = change_user_data(user_id=user_id, changeble_info=changeable_info, new_data=new_data)
    return {"status": 1, "message": data}

# @user_router.put("/api/change_profile")
# async def change_user_profile(user_id: int, changeable_info: str, new_data: str):
#     data = change_user_data(user_id=user_id, changeable_info=changeable_info, new_data=new_data)
#     if data:
#         try:
#             change_user = change_user_data(user_id, changeable_info, new_data=new_data)
#             return {"status": 1, "user_id": change_user or "Успешно изменени"}
#         except Exception:
#             return {"status": 0, "message":  "Ошибка"}
#     return {"status": 0, "message": "Invalid email or phone number"}
