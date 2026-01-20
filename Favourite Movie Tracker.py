print("Favourite Movie Tracker")

oishi_fav_movie=["Avater","Inspection","Cradle to Grave"]
Niha_fav_movie=["Avater","Inspection","Super Hero"]
Raima_fav_movie=["Avater","Super Hero"]

a=set(oishi_fav_movie)
b=set(Niha_fav_movie)
c=set(Raima_fav_movie)

#most common favourite movie

lib= list(a & b & c)

print("Most favourite movie:",lib)
