print("Advanced Expense Manager")

expenses = {}

def add_expense():
    cat = input("Category: ")
    amt = int(input("Amount: "))
    expenses[cat] = expenses.get(cat, 0) + amt

def show_expense():
    total = 0
    for c, a in expenses.items():
        print(c, ":", a)
        total += a
    print("Total:", total)

while True:
    print("1.Add Expense 2.Show 3.Exit")
    op = input()
    if op == "1":
        add_expense()
    elif op == "2":
        show_expense()
    else:
        break
