from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from models import BancoDeDados
from datetime import datetime, date, timedelta


app = FastAPI()
templates = Jinja2Templates(directory="view")


@app.get("/")
def todo(request: Request):
    banco = BancoDeDados("dbsqlite")
    tarefas = banco.mostrar_tarefas()
    data_de_hoje = datetime.now().strftime("%d/%m/%Y")
    data_de_amanha = datetime.now() + timedelta(1)
    data_de_amanha_formatada = data_de_amanha.strftime("%d/%m/%Y")
        # for data in tarefas:
        #     data_de_hoje = datetime.now().strftime("%d/%m/%Y")
        #     if data[2] == data_de_hoje:
        #         print("Hoje")

    return templates.TemplateResponse(
        "todo_list.html",
        {
            "request": request,
            "tarefas": tarefas,
            "data_de_hoje": data_de_hoje,
            "data_de_amanha_formatada": data_de_amanha_formatada,
        },
    )


@app.post("/tarefas")
def teste(request: Request, tarefa: str = Form(...), data: str = Form(...)):
    banco = BancoDeDados("dbsqlite")
    banco.salvar_alteracao(tarefa, data)
    return RedirectResponse("/", status_code=303)
