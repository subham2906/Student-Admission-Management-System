import tkinter as tk
from add_student import open_add_student_window
from view_students import open_view_window

root = tk.Tk()
root.title("Student Admission Management System")
root.geometry("450x350")

tk.Label(root, text="Student Admission System", font=("Arial", 18, "bold")).pack(pady=30)

tk.Button(root, text="Add Student", width=20, font=("Arial", 12),
          command=open_add_student_window, bg="#007bff", fg="white").pack(pady=15)

tk.Button(root, text="View All Students", width=20, font=("Arial", 12),
          command=open_view_window, bg="#28a745", fg="white").pack(pady=15)

tk.Button(root, text="Exit", width=20, font=("Arial", 12),
          command=root.destroy, bg="red", fg="white").pack(pady=15)

root.mainloop()
