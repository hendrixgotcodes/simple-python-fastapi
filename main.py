from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    }
}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you wish to get", gt=0, lt=3)):
    return students[student_id]


@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: str):
    for student_id in students:
        print("student_id", student_id)
        if students[student_id]["name"] == name:
            return students[student_id]
        else:
            return {"message": "Student not found"}


@app.get("/hello/{name}")
async def say_hello(name: Optional[str] = None):
    return {"message": f"Hello {name}"}
