print("Electricity Bill Calculator")
unit=int(input("Enter  total unit:"))

def calc_bill(unit1):
    if unit1>=1 and unit1<=100:
        return 5
    elif unit1>=101 and unit1<=200:
        return 7
    elif unit1>=201:
        return 10

print("Rate per unit:",calc_bill(unit),"taka")

total_bill=unit*calc_bill(unit)
print("Total Bill:",total_bill,"taka")