import random

ro = random.randint(1,2)
tipp = input("Tippelj (Fej, Írás nagybetű + ékezet kötelező): ")

if ro == 1:
    eredmeny="Fej"
elif ro == 2:
    eredmeny="Írás"

if tipp==eredmeny:
    print("Nyertél!", "Eredmény:", eredmeny)
else:
    print("Vesztettél!", "Eredmény:", eredmeny, "Tipped:", tipp)