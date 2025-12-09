import csv
import os

FILE = "students.csv"

def ensure_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["First","Middle","Last","DOB","Gender",
                             "Email","Phone","City","State","Country",
                             "Physics","Chemistry","Maths","PCM%","Hobbies"])

def add_student(data):
    ensure_file()
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def get_all_students():
    ensure_file()
    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

def clear_students():
    ensure_file()
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["First","Middle","Last","DOB","Gender",
                         "Email","Phone","City","State","Country",
                         "Physics","Chemistry","Maths","PCM%","Hobbies"])
