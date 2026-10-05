from fastapi import FastAPI
import random

student_info = FastAPI()

students = []


@student_info.get("/")
def read():
    return{"message": "Students information"}

@student_info.get("/api/students")
def get():
    return{"total": len(students), "students": students}

@student_info.post("/api/students")
def put(student:dict):
    student["id"] = random.randint(1,100)
    students.append(student)

    return{"message": "Stuent infor added"}

@student_info.put("/api/students/{student_id}")
def update(student_id: int, updated_studentinfo: dict):
    for student in students:
        if student["id"] == student_id:
            student.update(updated_studentinfo)
            student["id"] = student_id
            return{"message": f"Student info of {student_id} has been updated", "student": student}
    return{"message": "error student not found"}


@student_info.delete("/api/students/{student_id}")
def delete(student_id: int):
    global students
    students = [s for s in students if s["id"]!= student_id]
    return{"message": "Student's info has been deleted"}