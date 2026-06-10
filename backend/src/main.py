from fastapi import FastAPI
from models.student import Student

app = FastAPI()
student = Student()

@app.get("/")
def read_root():
    return {"Successfully": "Created" }

@app.get("/backend/{student_id}")
def read_item(student_id: int, q: str | None = None):
    return {"student_id": student_id, "q" : q}

@app.put("/backend/{student_id}")
def update_student():
    student1 = 123356
    return student1

