import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

students = []

documents_list = [
    "Aadhaar Card",
    "10th Marksheet",
    "12th Marksheet",
    "Transfer Certificate",
    "Migration Certificate",
    "Passport Size Photo",
    "Medical Certificate"
]

root = tk.Tk()
root.title("College Student Manager")
root.geometry("1000x600")
root.configure(bg="#f2f4f7")

title = tk.Label(
    root,
    text="College Student Manager",
    font=("Arial", 22, "bold"),
    bg="#263b50",
    fg="white",
    pady=15
)
title.pack(fill="x")

main_frame = tk.Frame(root, bg="#f2f4f7")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Student table
columns = ("Roll No", "Name", "Branch")

table = ttk.Treeview(
    main_frame,
    columns=columns,
    show="headings",
    height=15
)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=200, anchor="center")

table.pack(fill="both", expand=True, pady=10)


def refresh_table():
    for item in table.get_children():
        table.delete(item)

    for student in students:
        table.insert(
            "",
            "end",
            values=(
                student["roll"],
                student["name"],
                student["branch"]
            )
        )


def get_student():
    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a student first."
        )
        return None

    roll = table.item(selected[0], "values")[0]

    for student in students:
        if student["roll"] == roll:
            return student

    return None


# Add student
def add_student():
    roll = simpledialog.askstring(
        "Add Student", "Enter roll number:"
    )

    if not roll:
        return

    for student in students:
        if student["roll"] == roll:
            messagebox.showerror(
                "Error", "Roll number already exists."
            )
            return

    name = simpledialog.askstring(
        "Add Student", "Enter student name:"
    )

    if not name:
        return

    branch = simpledialog.askstring(
        "Add Student", "Enter branch:"
    )

    if not branch:
        return

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
    refresh_table()

    messagebox.showinfo(
        "Success", "Student added successfully!"
    )


# Search student
def search_student():
    roll = simpledialog.askstring(
        "Search Student", "Enter roll number:"
    )

    if not roll:
        return

    for item in table.get_children():
        values = table.item(item, "values")

        if values[0] == roll:
            table.selection_set(item)
            table.focus(item)
            table.see(item)

            messagebox.showinfo(
                "Student Found",
                "Roll No: " + values[0] +
                "\nName: " + values[1] +
                "\nBranch: " + values[2]
            )
            return

    messagebox.showinfo(
        "Not Found", "Student not found."
    )


# Update student
def update_student():
    student = get_student()

    if student is None:
        return

    choice = simpledialog.askstring(
        "Update Student",
        "Enter 1 to update name\n"
        "Enter 2 to update branch:"
    )

    if choice == "1":
        name = simpledialog.askstring(
            "Update Name", "Enter new name:"
        )

        if name:
            student["name"] = name

    elif choice == "2":
        branch = simpledialog.askstring(
            "Update Branch", "Enter new branch:"
        )

        if branch:
            student["branch"] = branch

    else:
        messagebox.showwarning(
            "Warning", "Invalid choice."
        )
        return

    refresh_table()
    messagebox.showinfo(
        "Success", "Student details updated."
    )


# Delete student
def delete_student():
    student = get_student()

    if student is None:
        return

    confirm = messagebox.askyesno(
        "Delete Student",
        "Are you sure you want to delete this student?"
    )

    if confirm:
        students.remove(student)
        refresh_table()

        messagebox.showinfo(
            "Success", "Student deleted."
        )


# Add marks
def add_marks():
    student = get_student()

    if student is None:
        return

    subject = simpledialog.askstring(
        "Add Marks", "Enter subject:"
    )

    if not subject:
        return

    marks = simpledialog.askfloat(
        "Add Marks", "Enter marks:"
    )

    if marks is None:
        return

    student["marks"][subject] = marks

    messagebox.showinfo(
        "Success", "Marks saved successfully."
    )


# Attendance manager
def attendance_manager():
    student = get_student()

    if student is None:
        return

    subject = simpledialog.askstring(
        "Attendance", "Enter subject:"
    )

    if not subject:
        return

    if subject not in student["attendance"]:
        student["attendance"][subject] = {
            "present": 0,
            "absent": 0
        }

    choice = simpledialog.askstring(
        "Attendance",
        "1. Mark Present\n"
        "2. Mark Absent\n"
        "3. View Attendance"
    )

    record = student["attendance"][subject]

    if choice == "1":
        record["present"] += 1
        messagebox.showinfo(
            "Attendance", "Marked Present."
        )

    elif choice == "2":
        record["absent"] += 1
        messagebox.showinfo(
            "Attendance", "Marked Absent."
        )

    elif choice == "3":
        present = record["present"]
        absent = record["absent"]
        total = present + absent

        if total > 0:
            percentage = present / total * 100
        else:
            percentage = 0

        messagebox.showinfo(
            "Attendance Report",
            "Subject: " + subject +
            "\nPresent: " + str(present) +
            "\nAbsent: " + str(absent) +
            "\nAttendance: " + str(round(percentage, 2)) + "%"
        )

    else:
        messagebox.showwarning(
            "Warning", "Invalid choice."
        )


# Document manager
def document_manager():
    student = get_student()

    if student is None:
        return

    document_window = tk.Toplevel(root)
    document_window.title("Document Manager")
    document_window.geometry("500x400")
    document_window.configure(bg="white")

    tk.Label(
        document_window,
        text="Student Documents",
        font=("Arial", 16, "bold"),
        bg="white"
    ).pack(pady=10)

    doc_table = ttk.Treeview(
        document_window,
        columns=("Document", "Status"),
        show="headings",
        height=10
    )

    doc_table.heading("Document", text="Document")
    doc_table.heading("Status", text="Status")
    doc_table.column("Document", width=280)
    doc_table.column("Status", width=150)

    doc_table.pack(fill="both", expand=True, padx=10, pady=10)

    def refresh_documents():
        for item in doc_table.get_children():
            doc_table.delete(item)

        for document in documents_list:
            if student["documents"][document]:
                status = "Submitted"
            else:
                status = "Not Submitted"

            doc_table.insert(
                "",
                "end",
                values=(document, status)
            )

    def update_document():
        selected = doc_table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning", "Select a document."
            )
            return

        document = doc_table.item(
            selected[0], "values"
        )[0]

        choice = simpledialog.askstring(
            "Update Document",
            "1. Submitted\n2. Not Submitted",
            parent=document_window
        )

        if choice == "1":
            student["documents"][document] = True

        elif choice == "2":
            student["documents"][document] = False

        else:
            return

        refresh_documents()

    tk.Button(
        document_window,
        text="Update Document Status",
        command=update_document,
        bg="#287a55",
        fg="white",
        padx=10,
        pady=5
    ).pack(pady=10)

    refresh_documents()


# Student report
def student_report():
    student = get_student()

    if student is None:
        return

    report = (
        "STUDENT REPORT\n"
        "--------------------------\n"
        "Roll No: " + student["roll"] +
        "\nName: " + student["name"] +
        "\nBranch: " + student["branch"] +
        "\n\nMARKS\n"
    )

    if student["marks"]:
        for subject, marks in student["marks"].items():
            report += subject + ": " + str(marks) + "\n"
    else:
        report += "No marks available.\n"

    report += "\nATTENDANCE\n"

    if student["attendance"]:
        for subject, record in student["attendance"].items():
            present = record["present"]
            absent = record["absent"]
            total = present + absent

            if total > 0:
                percentage = present / total * 100
            else:
                percentage = 0

            report += (
                subject + ": " +
                str(round(percentage, 2)) + "%\n"
            )
    else:
        report += "No attendance available.\n"

    report += "\nDOCUMENTS\n"

    submitted = 0

    for document in documents_list:
        if student["documents"][document]:
            report += document + " - Submitted\n"
            submitted += 1
        else:
            report += document + " - Not Submitted\n"

    report += (
        "\nDocuments Submitted: " +
        str(submitted) + "/" +
        str(len(documents_list))
    )

    if submitted == len(documents_list):
        report += "\nDocument Status: COMPLETE"
    else:
        report += "\nDocument Status: PENDING"

    # Display report in a separate window
    report_window = tk.Toplevel(root)
    report_window.title("Student Report")
    report_window.geometry("500x550")

    text_box = tk.Text(
        report_window,
        font=("Arial", 11),
        wrap="word"
    )
    text_box.pack(fill="both", expand=True, padx=10, pady=10)
    text_box.insert("1.0", report)
    text_box.config(state="disabled")


# Buttons
button_frame = tk.Frame(main_frame, bg="#f2f4f7")
button_frame.pack(fill="x", pady=10)

buttons = [
    ("Add Student", add_student),
    ("View Students", refresh_table),
    ("Search Student", search_student),
    ("Update Student", update_student),
    ("Delete Student", delete_student),
    ("Add Marks", add_marks),
    ("Attendance", attendance_manager),
    ("Documents", document_manager),
    ("Student Report", student_report),
    ("Exit", root.destroy)
]

for i, (text, command) in enumerate(buttons):
    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        width=16,
        pady=7,
        bg="#263b50",
        fg="white",
        activebackground="#3b5875"
    )
    button.grid(
        row=i // 5,
        column=i % 5,
        padx=5,
        pady=5,
        sticky="ew"
    )

for i in range(5):
    button_frame.grid_columnconfigure(i, weight=1)

root.mainloop()
