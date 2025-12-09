import tkinter as tk
from tkinter import ttk
import csv
import matplotlib.pyplot as plt

def open_view_window():
    win = tk.Toplevel()
    win.title("View Students")
    win.geometry("700x500")

    tree = ttk.Treeview(win, columns=("fname","lname","p","c","m","email","phone","pcm"), show="headings", height=15)
    headings = ["First","Last","Phy","Chem","Math","Email","Phone","PCM %"]
    
    for i, col in enumerate(headings):
        tree.heading(i, text=col)
        tree.column(i, width=90)
    tree.pack(pady=20)

    try:
        with open("database.csv", "r") as f:
            for row in csv.reader(f):
                tree.insert("", tk.END, values=row)
    except:
        pass

    def show_graph():
        pcm_list = []
        names = []
        with open("database.csv", "r") as f:
            for row in csv.reader(f):
                names.append(row[0])
                pcm_list.append(float(row[7]))

        plt.bar(names, pcm_list)
        plt.xlabel("Students")
        plt.ylabel("PCM %")
        plt.title("PCM Performance Graph")
        plt.show()

    tk.Button(win, text="Show PCM Graph", bg="#007bff", fg="white",
              command=show_graph).pack()

