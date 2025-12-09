import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from storage import add_student

class AddStudentFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_form()

    def create_form(self):
        self.fields = ["First Name","Middle Name","Last Name","DOB",
                       "Gender","Email","Phone","City","State","Country",
                       "Physics","Chemistry","Maths"]
        self.entries = {}

        row = 0
        for f in self.fields:
            tk.Label(self, text=f).grid(row=row, column=0, sticky="w", padx=5, pady=5)
            entry = tk.Entry(self, width=30)
            entry.grid(row=row, column=1, padx=5, pady=5)
            self.entries[f] = entry
            row += 1

        tk.Label(self, text="Hobbies").grid(row=row, column=0, sticky="nw", padx=5, pady=5)
        self.hobbies_text = scrolledtext.ScrolledText(self, width=30, height=4)
        self.hobbies_text.grid(row=row, column=1, padx=5, pady=5)
        row += 1

        self.pcm_var = tk.StringVar()
        tk.Label(self, text="PCM %:").grid(row=row, column=0, sticky="w")
        tk.Label(self, textvariable=self.pcm_var).grid(row=row, column=1, sticky="w")
        row += 1

        tk.Button(self, text="Save", command=self.save_student).grid(row=row, column=0, pady=10)
        tk.Button(self, text="Calculate PCM", command=self.calculate_pcm).grid(row=row, column=1, pady=10)

    def calculate_pcm(self):
        try:
            p = float(self.entries["Physics"].get())
            c = float(self.entries["Chemistry"].get())
            m = float(self.entries["Maths"].get())
            pcm = round((p + c + m)/3,2)
            self.pcm_var.set(str(pcm))
        except:
            messagebox.showerror("Error","Enter valid marks")

    def save_student(self):
        self.calculate_pcm()
        data = [self.entries[f].get() for f in self.fields]
        data.append(self.pcm_var.get())
        data.append(self.hobbies_text.get("1.0","end-1c"))

        if any(x=="" for x in data):
            messagebox.showwarning("Warning","All fields required")
            return

        add_student(data)
        messagebox.showinfo("Success","Student added successfully")
        for e in self.entries.values():
            e.delete(0,tk.END)
        self.hobbies_text.delete("1.0","end")
        self.pcm_var.set("")
