import pytest
from storage import add_student, get_all_students, clear_students

def test_add_and_get_student():
    clear_students()
    data = ["John","M","Doe","01/01/2005","Male","john@example.com","1234567890",
            "City","State","Country","80","90","85","85.0","Reading"]
    add_student(data)
    students = get_all_students()
    assert any(s["First"]=="John" for s in students)
