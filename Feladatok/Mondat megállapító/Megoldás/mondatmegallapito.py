folyt=True
vizsgal=None
while folyt:
    while vizsgal!="":
        vizsgal=input("Írj egy mondatot: ")
        for jel in vizsgal:
            if jel=="?":
                print("Ez egy kérdő mondat")
            if jel==".":
                print("Ez egy kijelentő mondat")
            if jel=="!":
                print("Ez a mondat lehet felkiáltó / felszólító / óhatjtó")
    while vizsgal!="":
        folyt=False