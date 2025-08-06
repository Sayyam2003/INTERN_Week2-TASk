students = {}

# CREATE
def add_student(roll_no, name, age):
    students[roll_no] = {"name": name, "age": age}
    print(f"Student {name} added.")

# READ
def view_student(roll_no):
    student = students.get(roll_no)
    if student:
        print(f"Roll No: {roll_no}, Name: {student['name']}, Age: {student['age']}")
    else:
        print("Student not found.")

# UPDATE
def update_student(roll_no, name=None, age=None):
    if roll_no in students:
        if name:
            students[roll_no]["name"] = name
        if age:
            students[roll_no]["age"] = age
        print(f"Student {roll_no} updated.")
    else:
        print("Student not found.")

# DELETE
def delete_student(roll_no):
    if roll_no in students:
        del students[roll_no]
        print(f"Student {roll_no} deleted.")
    else:
        print("Student not found.")

# Example usage:
add_student(1, "Alice", 20)
add_student(2, "Bob", 21)
view_student(1)
update_student(2, age=22)
delete_student(1)
view_student(1)

#Count word frequency
from collections import Counter

sentence = "this is a test this is only a test"
words = sentence.split()

word_freq = Counter(words)

for word, count in word_freq.items():
    print(f"{word}: {count}")
