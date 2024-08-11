from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


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


@app.post("/create-student")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"message": "Student already exists"}
    else:
        students[student_id] = student.model_dump()
        return {"message": "Student created", "data": students[student_id]}


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"message": "Student not found"}
    if student.name != None:
        students[student_id].name = student.name
        return {"message": "Student updated", "data": students[student_id]}
    if student.age != None:
        students[student_id].age = student.age
        return {"message": "Student updated", "data": students[student_id]}
    if student.year != None:
        students[student_id].year = student.year
        return {"message": "Student updated", "data": students[student_id]}

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id in students:
        del students[student_id]
        return {"message": "Student deleted"}
    else:
        return {"message": "Student not found"}