print('Student Attendance Report')
name=input("Enter your name:")
total_class=int(input("Enter total class:"))
attend_class=int(input("Enter attend class:"))
attendance_percentage = (attend_class / total_class) * 100


def check_elligibility(attendance_percentage):

    print(f"attendance:{attendance_percentage}%")

    if attendance_percentage>=80:
        return  "Regular:Allow to sit in exam"
    elif attendance_percentage>=70 and attendance_percentage<80:
        return "Non Collegiate"
    else:
        return "Dis Collegiate"
print(check_elligibility(attendance_percentage))

def attendance_fine(checkAttendance):
    if checkAttendance>=80:
        return "0 BDT"
    elif checkAttendance>=70 and checkAttendance<80:
        return "500 BDT"
    else:
        return "1000 BDT"

print("Attendance fine :",attendance_fine(attendance_percentage))