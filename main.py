def add_student():
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()

    with open("students.txt", "a") as file:
        file.write(f"{student_id},{name},{age},{course}\n")

    print("Student added successfully!\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            print("\n--- All Students ---")
            for line in file:
                student_id, name, age, course = line.strip().split(",")
                print(f"ID: {student_id} -- Name: {name} -- Age: {age} -- Course: {course}")
            print()
    except FileNotFoundError:
        print("No student data found.\n")

def seach_student():
    search_id = input("enter student_id:-").strip()
    found = False
    try:
        with open("students.txt","r") as file :
            for line in file:
                student_id, name, age, course = line.strip().split(",")
                if student_id == search_id:
                    print(f"ID: {student_id} -- Name: {name} -- Age: {age} -- Course: {course}")
                    found = True
                    break
                if not found:
                    print("student not found")
    except FileNotFoundError:
        print("file not found")
def update_data():
    update_id = input("enter student_id to update:-").strip()
    updated = False
    students = []
    
    
    try :
        with open("students.txt","r") as file:
            for line in file:
                student_id, name, age, course = line.strip().split(",")
                if student_id == update_id:
                    print("student data already stored")
                    new_name = input("enter new name:-") or name
                    new_age = input("enter your new age:-") or age 
                    new_course = input("enter new course:-") or course
                    students.append(f"{student_id},{new_name},{new_age},{new_course}\n")
                    updated = True
                else:
                    students.append(line)
                if updated:
                    with open("students.txt","w") as file:
                        file.writelines(students)
                    print("students data store successfully")
                else:
                    print("no data store")
    except FileNotFoundError:
        print("student id not found")

def delete_student():
    delete_id = input("Enter Student ID to update: ").strip()
    deleted = False
    students = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_id =  line.strip().split(",")[0]

                if student_id != delete_id :
                                        
                    students.append(line)
                else:
                    deleted = True


                if deleted:
                    with open("students.txt", "w") as file:
                        file.writelines(students)
                    print(" Student data deleted successfully!\n")
                else:
                    print("❌ Student ID not found.\n")

    except FileNotFoundError:
        print("❌ No student data file exists.\n")


while True:
    print("----Student Data Management System----")
    print("1. add student")
    print("2. view student")
    print("3. search student")
    print("4. update data")
    print("5. deleted data")
    print("6. exit")
    menu = input("enter what you wnat:-").strip()
    if menu == "1":
        add_student()
    elif menu == "2" :
        view_students()
    elif menu == "3" :
        seach_student()
    elif menu == "4":
        update_data()
    elif menu == "5":
        delete_student()
    elif menu == "6":
        print("exiting from system")
    else:
        print("invalid choice")
        break
