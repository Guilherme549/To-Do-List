from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from models import BancoDeDados

app = FastAPI()
templates = Jinja2Templates(directory="view")


@app.get("/")
def todo(request: Request):
    banco = BancoDeDados("dbsqlite")
    tarefas = banco.mostrar_tarefas()

    return templates.TemplateResponse(
        "todo_list.html",
        {
            "request": request,
            "tarefas": tarefas,
        },
    )


@app.post("/tarefas")
def teste(request: Request, tarefa: str = Form(...), data: str = Form(...)):
    banco = BancoDeDados("dbsqlite")
    banco.salvar_alteracao(tarefa, data)
    return RedirectResponse("/", status_code=303)
