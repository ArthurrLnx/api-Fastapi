from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

#Inicializa a API
app = FastAPI(title="Task Manager API", description="Uma API simples para gerenciar tarefas.")

#Modelo de Dados
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

#Banco de Dados em memória
tasks_db: List[Task] = []

#rotas
@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    # Verifica se o ID já existe
    if any(t.id == task.id for t in tasks_db):
        raise HTTPException(status_code=400, detail="Task com este ID já existe.")
    
    tasks_db.append(task)
    return task

@app.get("/tasks", response_model=List[Task])
def get_all_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
def get_task_by_id(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task não encontrada.")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    global tasks_db
    tasks_db = [t for t in tasks_db if t.id != task_id]
    return