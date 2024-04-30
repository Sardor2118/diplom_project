from urllib import request
from pydantic import BaseModel
from fastapi import Request, Body, UploadFile, APIRouter
from database.taskservice import (get_all_or_exact_task_db, change_task_text_db, delete_exact_task_db, public_comment_db, get_exact_task_comment_db,
                                  change_comment_text_db, delete_comment_db, public_task_db)
tasks_router = APIRouter(prefix="/tasks", tags=["Управление задачами"])

class User(BaseModel):
    username: str
    email: str
    phone_number: str
    password: str
    user_city: str

# публикация задачи
@tasks_router.post("/api/tasks")
async def public_comment(user: str, text: str):
    data = await request.json()
    task_id = data.get("task_id")
    user_id = data.get("user_id")
    text = data.get("main_text")
    if user_id and text and task_id:
        public_task_db(user_id=user_id, task_id=task_id, text=text)
        return {"status": 1, "message": "Успешно опубликовано"}
    return {"status": 0, "message": "Ошибка"}


# получить определенные или все посты
@tasks_router.get("/api/tasks")
async def get_all_or_exact_task(task_id:int=0):
    if task_id:
        exact_task = get_all_or_exact_task_db(task_id)
        return {"status": 1, "message": exact_task or "Ошибка"}
    return {"status": 0, "message": "Ошибка"}

# изменить пост
@tasks_router.put("/api/tasks")
async def change_user_task(request:Request):
    data = request.json()
    task_id = data.get('task_id')
    text = data.get('text')
    if task_id and text:
        change_task_text_db(task_id=task_id, text=text)
        return {"status": 1, "message": "Успешно изменено"}
    return {"status": 0, "message": "Ошибка"}

# удаление поста
@tasks_router.delete("/api/tasks")
async def delete_user_task(request:Request):
    data = await request.json()
    task_id = data.get('task_id')
    if task_id:
        delete_exact_task_db(task_id=task_id)
        return {"status": 1, "message": "Успешно удалено"}
    return {"status": 0, "message": "Ошибка"}