students = []


# Documents required for every student
documents_list = [
    "Aadhaar Card",
    "10th Marksheet",
    "12th Marksheet",
    "Transfer Certificate",
    "Migration Certificate",
    "Passport Size Photo",
    "Medical Certificate"
]


# Add Student
def add_student():

    print("\n--- Add Student ---")

    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    branch = input("Enter branch: ")

    documents = {}

    for document in documents_list:
        documents[document] = False

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": {},
        "attendance": {},
        "documents": documents
    }

    students.append(student)

    print("Student added successfully!")


# View all students
def view_students():

    print("\n--- All Students ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:

        print("Roll No:", student["roll"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("--------------------")


# Search student
def search_student():

    print("\n--- Search Student ---")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            print("\nStudent Found!")
            print("Roll No:", student["roll"])
            print("Name:", student["name"])
            print("Branch:", student["branch"])

            return

    print("Student not found.")


# Update student
def update_student():

    print("\n--- Update Student ---")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            print("1. Update Name")
            print("2. Update Branch")

            choice = input("Enter choice: ")

            if choice == "1":

                student["name"] = input("Enter new name: ")
                print("Name updated.")

            elif choice == "2":

                student["branch"] = input("Enter new branch: ")
                print("Branch updated.")

            else:
                print("Invalid choice.")

            return

    print("Student not found.")


# Delete student
def delete_student():

    print("\n--- Delete Student ---")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            students.remove(student)

            print("Student deleted.")

            return

    print("Student not found.")


# Add marks
def add_marks():

    print("\n--- Add Marks ---")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            subject = input("Enter subject: ")
            marks = float(input("Enter marks: "))

            student["marks"][subject] = marks

            print("Marks added.")

            return

    print("Student not found.")


# Attendance Manager
def attendance_manager():

    print("\n--- Attendance Manager ---")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            subject = input("Enter subject: ")

            print("\n1. Present")
            print("2. Absent")
            print("3. View Attendance")

            choice = input("Enter choice: ")

            if subject not in student["attendance"]:

                student["attendance"][subject] = {
                    "present": 0,
                    "absent": 0
                }

            if choice == "1":

                student["attendance"][subject]["present"] += 1

                print("Attendance marked Present.")

            elif choice == "2":

                student["attendance"][subject]["absent"] += 1

                print("Attendance marked Absent.")

            elif choice == "3":

                present = student["attendance"][subject]["present"]
                absent = student["attendance"][subject]["absent"]

                total = present + absent

                if total > 0:
                    percentage = (present / total) * 100
                else:
                    percentage = 0

                print("\nSubject:", subject)
                print("Present:", present)
                print("Absent:", absent)
                print("Attendance:", round(percentage, 2), "%")

            else:

                print("Invalid choice.")

            return

    print("Student not found.")


# Document Manager
def document_manager():

    print("\n--- Document Manager ---")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            print("\nDocuments:")

            number = 1

            for document in student["documents"]:

                if student["documents"][document] == True:
                    print(number, document, "✓ Submitted")
                else:
                    print(number, document, "✗ Not Submitted")

                number += 1

            print("\nEnter document number to update.")
            print("Enter 0 to go back.")

            choice = int(input("Enter choice: "))

            if choice == 0:
                return

            if choice >= 1 and choice <= len(documents_list):

                document = documents_list[choice - 1]

                print("\nSelected:", document)
                print("1. Submitted")
                print("2. Not Submitted")

                status = input("Enter choice: ")

                if status == "1":

                    student["documents"][document] = True

                    print("Document marked as Submitted ✓")

                elif status == "2":

                    student["documents"][document] = False

                    print("Document marked as Not Submitted ✗")

                else:

                    print("Invalid choice.")

            else:

                print("Invalid document number.")

            return

    print("Student not found.")


# Complete Student Report
def student_report():

    print("\n--- Student Report ---")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            print("\n==============================")
            print("       STUDENT REPORT")
            print("==============================")

            print("Roll No:", student["roll"])
            print("Name:", student["name"])
            print("Branch:", student["branch"])


            # Marks

            print("\n--- Marks ---")

            if len(student["marks"]) == 0:

                print("No marks available.")

            else:

                for subject in student["marks"]:

                    print(subject, ":", student["marks"][subject])


            # Attendance

            print("\n--- Attendance ---")

            if len(student["attendance"]) == 0:

                print("No attendance available.")

            else:

                for subject in student["attendance"]:

                    present = student["attendance"][subject]["present"]
                    absent = student["attendance"][subject]["absent"]

                    total = present + absent

                    if total > 0:
                        percentage = (present / total) * 100
                    else:
                        percentage = 0

                    print("\nSubject:", subject)
                    print("Present:", present)
                    print("Absent:", absent)
                    print("Attendance:", round(percentage, 2), "%")


            # Documents

            print("\n--- Documents ---")

            submitted = 0

            for document in student["documents"]:

                if student["documents"][document] == True:

                    print("✓", document, "- Submitted")
                    submitted += 1

                else:

                    print("✗", document, "- Not Submitted")


            print("\nDocuments Submitted:",
                  submitted, "/", len(documents_list))

            if submitted == len(documents_list):

                print("Document Status: COMPLETE ✓")

            else:

                print("Document Status: PENDING ✗")

            print("==============================")

            return

    print("Student not found.")


# Main Program

while True:

    print("\n================================")
    print("     COLLEGE STUDENT MANAGER")
    print("================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add Marks")
    print("7. Attendance Manager")
    print("8. Document Manager")
    print("9. Student Report")
    print("10. Exit")

    choice = input("\nEnter your choice: ")


    if choice == "1":

        add_student()


    elif choice == "2":

        view_students()


    elif choice == "3":

        search_student()


    elif choice == "4":

        update_student()


    elif choice == "5":

        delete_student()


    elif choice == "6":

        add_marks()


    elif choice == "7":

        attendance_manager()


    elif choice == "8":

        document_manager()


    elif choice == "9":

        student_report()


    elif choice == "10":

        print("\nThank you for using College Student Manager!")
        break

    else:

        print("Invalid choice. Try again.")