
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from model.model import tasks

app = FastAPI()
templates = Jinja2Templates(directory="view")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})

@app.post("/add_task")
async def add_task(new_task: str = Form(...)):
    tasks.append(new_task)
    return {"task": new_task, "status": "Adicionada com sucesso"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
