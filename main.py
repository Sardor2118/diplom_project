from fastapi import FastAPI
from database import Base, engine
from api.users_api.users import user_router
from api.tasks_api.task import tasks_router
from api.comments_api.comments import comment_router
from fastapi.staticfiles import StaticFiles

# команда для создания всех таблиц в дб
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/")
app.mount("/static", StaticFiles(directory="static"))
app.include_router(user_router)
app.include_router(comment_router)
app.include_router(tasks_router)
