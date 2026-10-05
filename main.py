from fastapi import FastAPI
import random


app = FastAPI()
tasks=[]

@app.get("/")
def read():
    return {"message": "Welcome to my server!"}

@app.get("/api/tasks")
def get():
    return{"total": len(tasks), "tasks": tasks}

@app.put("/api/tasks")
def put(task: dict):
    task["id"] = random.randint(1000,9999)
    return{"message": "task added", "task": task}

@app.update("/api/tasks/{task_id}")
def update(task_id: int, updated_task: dict):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task)
            task["id"] = task_id
         
            return{"message": f"Task {task_id} updated", "task": task}
        
        return{"message": "task not found"}


@app.delete("/api/tasks/{task_id}")
def delete_ele(task_id:int):
    global tasks

    tasks = [ t for t in tasks if t["id"]!=task_id]
    return {"message": f"Task{task_id} deleted"}

    


