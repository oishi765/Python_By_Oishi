print("Shop Discount & Billing System")
name=input("Enter your name:")
total_amount=int(input("Enter your total amount:"))

def discount_rules(amount):
    if amount >= 5000:
        return "20%"
    elif amount >= 3000 and amount<5000:
        return "10%"
    elif amount >= 1000 and amount<3000:
        return "5%"
    elif amount < 1000:
        return "No discount"

print("Discount:",discount_rules(total_amount))


discount_percent = int(discount_rules(total_amount).replace("%", ""))

discount=(total_amount * discount_percent)/100
print("discount cost:",discount)

payable_bill=total_amount-discount
print("Payable bill:",payable_bill)

print("Thanks for your khanas treat tomtom .")