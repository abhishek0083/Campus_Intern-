import tkinter as tk
from tkinter import ttk
import sqlite3

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        # Create a database or connect to an existing one
        self.conn = sqlite3.connect("student.db")
        self.cur = self.conn.cursor()

        # Create table if not exists
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                roll_number TEXT,
                course TEXT,
                age INTEGER,
                gender TEXT,
                contact TEXT
            )
        """)
        self.conn.commit()

        # Student Information
        self.name_var = tk.StringVar()
        self.roll_number_var = tk.StringVar()
        self.course_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.contact_var = tk.StringVar()

        # Frames
        self.info_frame = ttk.LabelFrame(root, text="Student Information")
        self.info_frame.grid(row=0, column=0, padx=10, pady=10)

        self.table_frame = ttk.LabelFrame(root, text="Students")
        self.table_frame.grid(row=0, column=1, padx=10, pady=10)

        # Labels and Entries
        ttk.Label(self.info_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = ttk.Entry(self.info_frame, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.info_frame, text="Roll Number:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.roll_number_entry = ttk.Entry(self.info_frame, textvariable=self.roll_number_var)
        self.roll_number_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.info_frame, text="Course:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.course_entry = ttk.Entry(self.info_frame, textvariable=self.course_var)
        self.course_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.info_frame, text="Age:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.age_entry = ttk.Entry(self.info_frame, textvariable=self.age_var)
        self.age_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(self.info_frame, text="Gender:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.gender_entry = ttk.Combobox(self.info_frame, textvariable=self.gender_var, values=["Male", "Female", "Other"])
        self.gender_entry.grid(row=4, column=1, padx=5, pady=5)
        self.gender_entry.current(0)

        ttk.Label(self.info_frame, text="Contact:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.contact_entry = ttk.Entry(self.info_frame, textvariable=self.contact_var)
        self.contact_entry.grid(row=5, column=1, padx=5, pady=5)

        # Buttons
        self.add_button = ttk.Button(self.info_frame, text="Add Student", command=self.add_student)
        self.add_button.grid(row=6, columnspan=2, padx=5, pady=5)

        self.delete_button = ttk.Button(self.info_frame, text="Delete Student", command=self.delete_student)
        self.delete_button.grid(row=7, columnspan=2, padx=5, pady=5)

        # Treeview
        self.student_tree = ttk.Treeview(self.table_frame, columns=("name", "roll_number", "course", "age", "gender", "contact"), show="headings")
        self.student_tree.heading("name", text="Name")
        self.student_tree.heading("roll_number", text="Roll Number")
        self.student_tree.heading("course", text="Course")
        self.student_tree.heading("age", text="Age")
        self.student_tree.heading("gender", text="Gender")
        self.student_tree.heading("contact", text="Contact")
        self.student_tree.pack(expand=True, fill="both")
        
        self.update_treeview()

    def add_student(self):
        self.cur.execute("INSERT INTO students VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                         (self.name_var.get(), self.roll_number_var.get(), self.course_var.get(),
                          self.age_var.get(), self.gender_var.get(), self.contact_var.get()))
        self.conn.commit()
        self.clear_entries()
        self.update_treeview()

    def delete_student(self):
        selected_item = self.student_tree.selection()[0]
        student_id = self.student_tree.item(selected_item, "values")[0]
        self.cur.execute("DELETE FROM students WHERE id=?", (student_id,))
        self.conn.commit()
        self.update_treeview()

    def clear_entries(self):
        self.name_var.set("")
        self.roll_number_var.set("")
        self.course_var.set("")
        self.age_var.set("")
        self.gender_var.set("Male")
        self.contact_var.set("")

    def update_treeview(self):
        self.student_tree.delete(*self.student_tree.get_children())
        self.cur.execute("SELECT * FROM students")
        students = self.cur.fetchall()
        for student in students:
            self.student_tree.insert("", "end", values=student)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
