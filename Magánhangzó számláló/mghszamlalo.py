mondat=input("Adj meg egy mondatot: ")
mgh=0
for betu in mondat:
    if betu in "aeiouAEIOUáéíóöőúüűÁÉÍÓÖŐÚÜŰ":
        mgh+=1

print("Mondatod: ")
print(mondat)
print("Magánhangzók száma: ")
print(mgh)