from database.models import Comment, UserPost, User
from database import get_db
from datetime import datetime

# получение всех или конкретного поста
def get_all_or_exact_post_db(post_id):
    db = next(get_db())
    if post_id == 0:
        return db.query(UserPost).all()
    return db.query(UserPost).filter_by(id=post_id).first()

# редактирование поста
def change_post_text_db(post_id, new_text):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(id=post_id).first()
    if exact_post:
        exact_post.main_text = new_text
        db.commit()
        return "Успешно изменено"
    return "Ошибка"

# удаление поста
def delete_exact_post_db(post_id):
    db = get_db()
    exact_post = db.query(UserPost).filter_by(id=post_id).first()
    if exact_post:
        db.delete(exact_post)
        db.commit()
        return "Успешно удалено"
    return "Ошибка"

def public_comment_db(post_id, user_id, text):
    db = next(get_db())
    new_comment = Comment(post_id=post_id, user_id=user_id, text=text, reg_date=datetime.now())
    db.add(new_comment)
    db.commit()
    return "Коментарии успешно опубликовано"
def get_exact_post_comment_db(post_id):
    db = next(get_db())
    exact_post_comments = db.query(UserPost).filter_by(post_id=post_id).all()
    if exact_post_comments:
        return exact_post_comments
    return []
def change_comment_text_db(comment_id, new_text):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(id=comment_id).first()
    if exact_post:
        exact_post.text = new_text
        db.commit()
        return "Текст успешно изменен"
    return "Ошибка"

def delete_comment_db(comment_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(id=comment_id).first()
    if exact_post:
        db.delete(exact_post)
        db.commit()
        return "Успешно удалено"
    return "Ошибка"















