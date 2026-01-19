print("Daily Expense Tracker")

costing_list=["Reading","Tuition fee","Hostel Billing"]
costs=[]

for item in costing_list:
 amount=float(input(f"Enter your cost of {item}:"))
 costs.append(amount)

total=sum(costs)
avg=total/len(costs)
maximum=max(costs)
minimum=min(costs)
index_max=costs.index(maximum)
index_min=costs.index(minimum)

print("Total:",total,"BDT")
print("Average:",avg,"BDT")
print("Maximum:",maximum,"BDT")
print("Highest costing item:",costing_list[index_max])
print("Lowest costing item:",costing_list[index_min])