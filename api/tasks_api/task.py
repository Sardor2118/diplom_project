from urllib import request
from pydantic import BaseModel
from database.models import UserTask
from fastapi import Request, Body, UploadFile, APIRouter
from database.taskservice import (get_all_or_exact_task_db, change_task_text_db, delete_exact_task_db, public_comment_db, get_exact_task_comment_db,
                                  change_comment_text_db, delete_comment_db, public_task_db)
tasks_router = APIRouter(prefix="/tasks", tags=["Управление задачами"])

class Task(BaseModel):
    user_id: int
    UserTask_id: int
    main_text: str

# публикация задачи
@tasks_router.post("/api/tasks")
async def public_comment(task_model: Task):
    all_info = dict(task_model)
    user_id = task_model.user_id
    main_text = task_model.main_text
    if user_id and main_text:
        public_task_db(user_id=user_id, main_text=main_text)
        return {"status": 1, "message": "Успешно опубликовано"}
    return {"status": 0, "message": "Ошибка"}

# получить определенные или все посты
@tasks_router.get("/api/tasks")
async def get_all_or_exact_task(UserTask_id: int):
    exact_task = get_all_or_exact_task_db(UserTask_id)
    return {"status": 1, "message": exact_task}

# изменить пост
@tasks_router.put("/api/tasks")
async def change_user_task(UserTask_id: int, new_text: str):
    if UserTask_id and new_text:
        change_task_text_db(UserTask_id=UserTask_id, new_text=new_text)
        return {"status": 1, "message": "Успешно изменено"}
    return {"status": 0, "message": "Ошибка"}

# удаление поста
@tasks_router.delete("/api/tasks")
async def delete_user_task(UserTask_id: int):
    if UserTask_id:
        delete_exact_task_db(UserTask_id=UserTask_id)
        return {"status": 1, "message": "Успешно удалено"}
    return {"status": 0, "message": "Ошибка"}