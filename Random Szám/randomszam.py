import random 
randomszam=random.randint(1,100)
while True: #while ciklus
    tipp=int(input("Gondoltam egy számra, tippelj: "))
    if tipp == randomszam:
        print("Ügyes, sikeresen kitaláltad a számot!")
        break 
    if tipp > randomszam:
        print("Tipp: A gondolt szám kisebb!")
    else:
        print("Tipp: A gondolt szám nagyobb!")
    