print("Weekly Temperature Analysis")
temp=[20,10,36,27,34,12,46]
days=["Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"]

avg_temp=sum(temp)/len(temp)
highest_temp=max(temp)
min_temp=min(temp)

index_highest=temp.index(highest_temp)
index_lowest=temp.index(min_temp)

print("Average temp:",avg_temp)
print("Highest temp:",highest_temp)
print("Lowest temp:",min_temp)
print("Highest temp of the days:",days[index_highest])
print("Lowest temp of the days:",days[index_lowest])