def createStudent(name, age, grades=None):
    if grades == None:
        grades = []
        return {
        "name": name,
        "age": age,
        "grades": grades
    }

chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)
matias = createStudent('Matias', 18)

def addGrade(student, grade):
    student["grades"].append(grade)
    print(student)

addGrade(chrisley, 90)
addGrade(dallas, 100)
addGrade(matias, 110)


print(id(chrisley['grades']))
print(id(dallas['grades']))