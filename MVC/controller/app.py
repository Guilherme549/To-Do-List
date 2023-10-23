
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


# app = FastAPI()
# templates = Jinja2Templates(directory="view")

# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})


app = FastAPI()
templates = Jinja2Templates(directory="view")

@app.get("/")
def todo(request: Request):
    return templates.TemplateResponse("todo_list.html", {"request": request})