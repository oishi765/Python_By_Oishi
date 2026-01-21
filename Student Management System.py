
print("Student Management System")
students = {}

def add_student():
    sid = input("Enter ID: ")
    if sid in students:
        print("Student already exists")
        return
    name = input("Enter name: ")
    marks = list(map(int, input("Enter 3 marks: ").split()))
    students[sid] = {"name": name, "marks": marks, "attendance": 0}
    print("Student added")

def show_report():
    for sid, info in students.items():
        avg = sum(info["marks"]) / len(info["marks"])
        print(sid, info["name"], "Avg:", avg)

while True:
    print("1.Add 2.Report 3.Exit")
    ch = input("Choice: ")
    if ch == "1":
        add_student()
    elif ch == "2":
        show_report()
    else:
        break
