import tkinter as tk
from tkinter import messagebox
import csv

def open_add_student_window():
    win = tk.Toplevel()
    win.title("Add Student")
    win.geometry("500x600")

    fields = ["First Name", "Last Name", "Physics", "Chemistry", "Maths", "Email", "Phone"]
    entries = {}

    row = 0
    for label in fields:
        tk.Label(win, text=label).grid(row=row, column=0, padx=10, pady=10, sticky="w")
        entry = tk.Entry(win, width=30)
        entry.grid(row=row, column=1, padx=10, pady=10)
        entries[label] = entry
        row += 1

    pcm_label = tk.Label(win, text="PCM %: ")
    pcm_label.grid(row=row, column=0, sticky="w")
    pcm_value = tk.Label(win, text="")
    pcm_value.grid(row=row, column=1, sticky="w")
    row += 1

    def calculate_pcm():
        try:
            p = float(entries["Physics"].get())
            c = float(entries["Chemistry"].get())
            m = float(entries["Maths"].get())
            per = round((p + c + m) / 3, 2)
            pcm_value.config(text=str(per))
            return per
        except:
            messagebox.showerror("Error", "Enter valid marks")
            return None

    def save():
        per = calculate_pcm()
        if per is None:
            return

        data = [entries[f].get() for f in fields]
        data.append(per)

        if any(val == "" for val in data):
            messagebox.showwarning("Warning", "All fields required!")
            return

        with open("database.csv", "a", newline="") as f:
            csv.writer(f).writerow(data)

        messagebox.showinfo("Success", "Student Added!")
        for entry in entries.values():
            entry.delete(0, tk.END)
        pcm_value.config(text="")

    tk.Button(win, text="Calculate PCM", command=calculate_pcm,
              bg="#17a2b8", fg="white").grid(row=row, column=0, pady=20)
    tk.Button(win, text="Save Student", command=save,
              bg="#28a745", fg="white").grid(row=row, column=1)

