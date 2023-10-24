from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models import BancoDeDados


# app = FastAPI()
# templates = Jinja2Templates(directory="view")

# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})


app = FastAPI()
templates = Jinja2Templates(directory="view")


@app.get("/")
def todo(request: Request):
    banco = BancoDeDados("dbsqlite")
    return templates.TemplateResponse(
        "todo_list.html", {"request": request, "banco": banco}
    )
