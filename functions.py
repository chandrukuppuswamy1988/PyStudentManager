students = []
def add_student(name):
    students.append(name)


def print_student():
    for student in students:
        print(student)

add_student('Veera Manikandan')
add_student('Hari Hara Sudan')

print_student()
