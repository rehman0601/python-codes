#creating a list to store the student information
students=[]

#creating a fucntion to add student information
def add_student():
    rollno=int(input("enter the roll number: "))
    name=input("enter the name: ")
    marks=float(input("enter the marks: "))
    students.apend([rollno,name,marks])

#creating a function to display student information
def display_student():
    for student in students:
        if len(students)==0:
            print("no student information available")
        else:
            print("roll number:",student[0])
            print("name:",student[1])
            print("marks:",student[2])
            print("\n")
def search_student():
    rollno=int(input("enter the roll number to search: "))
    for student in students:
        if student[0]==rollno:
            print("roll number:",student[0])
            print("name:",student[1])
            print("marks:",student[2])
            print("\n")
        else:
            print("student not found")

def delete_student():
    rollno=int(input("enter the roll number to delete: "))
    for student in students:
        if student[0]==rollno:
            students.remove(student)
            print("student deleted successfully")
            break
        else
        print("student not found")
def main():
    while True:
        print("1.add student")
        print("2.display student")
        print("3.search student")
        print("4.delete student")
        print("5.exit")
choice=int(input("enter your choice: "))
match choice:
    case 1:
        add_student()
    case 2:
        display_student()
    case 3:
        search_student()
    case 4:
        delete_student()
    case 5:
        print("exit")
    case _:
        print("invalid choice")

    