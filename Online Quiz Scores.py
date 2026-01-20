print("Online Quize Score")

student=["Rima","Raka","Oishi","Totini","Raifa"]
marks=[
    [90,80,87],
    [87,34,67],
    [56,67,28],
    [90,90,89],
    [67,56,88]
]
avg_scores=[]

for score in marks:
    avg=sum(score)/len(score)
    avg_scores.append(avg)

highest_score=max(avg_scores)
lowest_score=min(avg_scores)
index_highest=avg_scores.index(highest_score)
index_lowest=avg_scores.index(lowest_score)

print("Highest score:",highest_score)
print("Lowest score:",lowest_score)
print("Highest score student:",student[index_highest])
print("Lowest score student:",student[index_lowest])