import tkinter as tk
from tkinter import ttk
from student_form import AddStudentFrame
from storage import get_all_students

class StudentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Admission Management System")
        self.geometry("800x600")
        self.create_tabs()

    def create_tabs(self):
        tabControl = ttk.Notebook(self)
        self.tab1 = AddStudentFrame(tabControl)
        self.tab2 = ttk.Frame(tabControl)

        tabControl.add(self.tab1, text='Add Student')
        tabControl.add(self.tab2, text='View Students')
        tabControl.pack(expand=1, fill="both")

        self.create_view_tab()

    def create_view_tab(self):
        columns = ["First","Middle","Last","DOB","Gender","Email","Phone","City","State","Country","Physics","Chemistry","Maths","PCM%","Hobbies"]
        self.tree = ttk.Treeview(self.tab2, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col,width=80)
        self.tree.pack(expand=True, fill="both")
        self.refresh_button = tk.Button(self.tab2, text="Refresh", command=self.refresh_table)
        self.refresh_button.pack(pady=5)

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for student in get_all_students():
            self.tree.insert("",tk.END,[student[col] for col in student.keys()])

if __name__ == "__main__":
    app = StudentApp()
    app.mainloop()
