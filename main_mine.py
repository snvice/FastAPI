from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, admin, users, address

app = FastAPI()
models.Base.metadata.create_all(bind=engine)  # run only when the db doesn't exist

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(address.router)


