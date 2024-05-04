from fastapi import Request, APIRouter
from pydantic import BaseModel
from database.taskservice import (get_exact_task_comment_db, public_comment_db,
                                  change_comment_text_db, delete_comment_db)
comment_router = APIRouter(prefix="/comments", tags=["Управление комментариями"])

class Task(BaseModel):
    user_id: int
    UserTask_id: int
    main_text: str
@comment_router.post("/api/comment")
async def public_comment(task_model: Task):
    all_info = dict(task_model)
    user_id = task_model.user_id
    main_text = task_model.main_text
    if user_id and main_text:
        public_comment_db(user_id=user_id, main_text=main_text)
        return {"status": 1, "message": "Успешно опубликовано"}
    return {"status": 0, "message": "Ошибка"}

# получение комментов определенного поста
@comment_router.get("/api/comment")
async def get_exact_task_comments(UserTask_id: int):
    comments = get_exact_task_comment_db(UserTask_id)
    return {"status": 1, "message": comments}

# изменить комментарий
@comment_router.put("/api/comment")
async def change_exact_user_comment(new_text: str, comment_id: int):
    if comment_id and new_text:
        change_comment_text_db(comment_id=comment_id, new_text=new_text)
        return {"status": 1, "message": "Успешноо изменено"}
    return {"status": 0, "message": "Ошибка"}

# удалить комментарии
@comment_router.delete("/api/comment")
async def delete_exact_user_comment(comment_id: int):
    if comment_id:
        delete_comment_db(comment_id=comment_id)
        return {"status": 1, "message": "Успешно удалено"}
    return {"status": 0, "message": "Ошибка удаления"}
