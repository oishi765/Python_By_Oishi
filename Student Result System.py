
#prrint student name from user input
print("Student Result System")
#rint("Enter Student name:")
name=input("Enter student name:")
print("Name:"+name)

#taking 3 subject from user input
#In python input means string so when we declare the int or float or any other variables then we use data_type(input(""))
chemistry=int(input("Enter chemistry:"))
Physics=int(input("Enter Physics:"))
Biochemistry=int(input("Enter Biochemistry:"))

#calculate total and avg
average=int(input("Enter average:"))
total=chemistry+Physics+Biochemistry
print("Total:",total)
average=total/3
print("Avg marks:",average)

if chemistry>=33 and Physics>=33 and Biochemistry>=33:
    print("Pass")
else:
    print("Fail")
#calculate grade using function
def get_grade(marks):
   if marks>=80 :
      return "A+"
   elif marks>=75 and marks<=79:
      return "A"
   elif marks>=70 and marks<=74:
      return "A-"
   elif marks>=65 and marks<=69:
      return "B+"
   elif marks>=60 and marks<=64:
      return "B"
   elif marks>=50 and marks<=59:
      return "B-"
   elif marks>=45 and marks<=49:
      return "C"
   elif marks>=40 and marks<=44:
     return "D"
   else:
     return "Fail"

print("Chemistry grade:",get_grade(chemistry))
print("Physics grade:",get_grade(Physics))
print("Biochemistry grade:",get_grade(Biochemistry))
print("Avg grade:",get_grade(average))

def pass_fail(chemistry,Physics,Biochemistry):
  if chemistry < 33:
      print("Failed in Chemistry")
  elif Physics < 33:
      print("Failed in Physics")
  elif Biochemistry < 33:
      print("Failed in Biochemistry")

pass_fail(chemistry,Physics,Biochemistry)

#remarks using functiom
avg_grade = get_grade(average)
def remarks_grade(grade):
    if grade == "A+" or grade == "A":
        return "Remarks: Very good"
    elif grade == "A-" or grade == "B+":
        return "Remarks: Not so good"
    else:
        return "Remarks: Keep trying"


result_remarks = remarks_grade(avg_grade)
print(result_remarks)