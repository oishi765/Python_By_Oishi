print("Event Guest List")
guest=["Rima","Raka","Oishi","Totini","Raifa"]

unique_guest=[]

for g in guest:
    if g not in unique_guest:
        unique_guest.append(g)

rsvp_list=["Oishi","Raka","Raifa"]

for guests in guest:
    if guests in rsvp_list:
        print(f"{guests}:Comming")
    else:
        print(f"{guests}:Not Coming")
