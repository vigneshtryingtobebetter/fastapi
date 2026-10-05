from fastapi import FastAPI
import random

app = FastAPI()

tasks = []

@app.get("/")
def read_get():
    return {"message" : "hello from python fastapi"} 

@app.get("/api/tasks")
def get_tasks():
    return{"total":len(tasks), "tasks": tasks}

@app.post("/api/tasks")
def post_task(task : dict):
    task["id"] = random.randint(1000,9999)
    tasks.append(task)
    return{"message": "task successfully added", "task": task}

@app.put("/api/tasks/{task_id}")
def update_task(task_id: int, updated_task: dict):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task)
            task["id"] = task_id
            return{"message": f"the task {task_id} has been updated", "task": task}
        return{"error": "task not found"}
    
@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]

    return{"message": f"task {task_id} deleted"}