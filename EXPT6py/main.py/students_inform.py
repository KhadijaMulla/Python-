# students/students_inform.py

student_info = {
    "roll_no": 101,
    "name": "Ananya",
    "age": 20,
    "course": "B.Tech",
    "branch": "Computer Science",
    "college": "ABC College"
}


def display_student_info():
    print("----- Student Information -----")
    print("Roll No :", student_info["roll_no"])
    print("Name    :", student_info["name"])
    print("Age     :", student_info["age"])
    print("Course  :", student_info["course"])
    print("Branch  :", student_info["branch"])
    print("College :", student_info["college"])