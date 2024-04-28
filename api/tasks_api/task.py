from urllib import request
from fastapi import Request, Body, UploadFile, APIRouter
from database.taskservice import (get_all_or_exact_task_db, change_task_text_db, delete_exact_task_db, public_comment_db, get_exact_task_comment_db,
                                  change_comment_text_db, delete_comment_db)
tasks_router = APIRouter(prefix="/tasks", tags=["Управление задачами"])

# получить определенные или все посты
@tasks_router.post("/api/tasks")
async def get_all_or_exact_post(task_id:int=0):
    if task_id:
        exact_task = get_all_or_exact_task_db(task_id)
        return {"status": 1, "message": exact_task}
    return {"status": 0, "message": "Ошибка"}

# изменить пост
@tasks_router.put("/api/tasks")
async def change_user_task(request:Request):
    data = request.json()
    task_id = data.get('task_id')
    text = data.get('text')
    if task_id and text:
        change_task_text_db(post_id=task_id, text=text)
        return {"status": 1, "message": "Успешно изменено"}
    return {"status": 0, "message": "Ошибка"}

# удаление поста
@tasks_router.delete("/api/tasks")
async def delete_user_task(request:Request):
    data = await request.json()
    task_id = data.get('task_id')
    if task_id:
        delete_exact_task_db(post_id=task_id)
        return {"status": 1, "message": "Фото успешно удалено"}
    return {"status": 0, "message": "Ошибка"}