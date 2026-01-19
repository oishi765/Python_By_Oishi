print("Mobile Balance Check System")

phone_no=input("Enter your phone no :")

current_balance=int(input("Enter your current balance :"))


def des_balance(balance):
    if balance>100:
        return "You can make a call"
    elif balance>=20 and balance<100:
        return "Low balance"
    else:
        return "Recharge needed"

print("Status:",des_balance(current_balance))

def check_balance(balance1):
    if balance1==0:
        return "No balance left"
    elif balance1>0:
        return "Invalid balance input"

print(check_balance(current_balance))
print("Thank you for using our service ")