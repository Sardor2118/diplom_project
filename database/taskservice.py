from database.models import Comment, UserTask, User
from database import get_db
from datetime import datetime

# получение всех или конкретного поста
def get_all_or_exact_task_db(task_id):
    db = next(get_db())
    if task_id == 0:
        return db.query(UserTask).all()
    return db.query(UserTask).filter_by(id=task_id).first()

# редактирование поста
def change_task_text_db(task_id, new_text):
    db = next(get_db())
    exact_task = db.query(UserTask).filter_by(id=task_id).first()
    if exact_task:
        exact_task.main_text = new_text
        db.commit()
        return "Успешно изменено"
    return "Ошибка"

# удаление поста
def delete_exact_task_db(task_id):
    db = get_db()
    exact_task = db.query(UserTask).filter_by(id=task_id).first()
    if exact_task:
        db.delete(exact_task)
        db.commit()
        return "Успешно удалено"
    return "Ошибка"

def public_comment_db(task_id, user_id, text):
    db = next(get_db())
    new_comment = Comment(post_id=task_id, user_id=user_id, text=text, reg_date=datetime.now())
    db.add(new_comment)
    db.commit()
    return "Коментарии успешно опубликовано"
def get_exact_task_comment_db(task_id):
    db = next(get_db())
    exact_task_comments = db.query(UserTask).filter_by(post_id=task_id).all()
    if exact_task_comments:
        return exact_task_comments
    return []
def change_comment_text_db(comment_id, new_text):
    db = next(get_db())
    exact_task = db.query(UserTask).filter_by(id=comment_id).first()
    if exact_task:
        exact_task.text = new_text
        db.commit()
        return "Текст успешно изменен"
    return "Ошибка"

def delete_comment_db(comment_id):
    db = next(get_db())
    exact_task = db.query(UserTask).filter_by(id=comment_id).first()
    if exact_task:
        db.delete(exact_task)
        db.commit()
        return "Успешно удалено"
    return "Ошибка"















