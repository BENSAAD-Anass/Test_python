import random

Nom=input("Veuillez saisir votre nom : ")
print("Bienvenu "+Nom+" dans le jeux Pierre Papier Ciseau")


def convertion(val_input) :
    if val_input == "1" : return "Papier"
    if val_input == "2" : return "Ciseau"
    if val_input == "3" : return "Pierre"
    else : print("Erreur : Veuillez entrer un des chiffres en haut")

def convertion_rand(val_input) :
    if val_input <= (1/3): return "Papier"
    elif val_input <= (2/3) : return "Ciseau"
    elif val_input <= 1 : return "Pierre"

def PPC(val_usr,val_PC) :
    if val_usr == val_PC : return "Egalité !"
    elif val_usr=="Papier" and val_PC=="Ciseau" : return "Le PC a gagné !"
    elif val_usr=="Papier" and val_PC=="Pierre" : return str(Nom+" a gagné !")
    elif val_usr=="Ciseau" and val_PC=="Pierre" : return "Le PC a gagné !"
    elif val_usr=="Ciseau" and val_PC=="Papier" : return str(Nom+" a gagné !")
    elif val_usr=="Pierre" and val_PC=="Papier" : return "Le PC a gagné !"
    elif val_usr=="Pierre" and val_PC=="Ciseau" : return str(Nom+" a gagné !")

while 1==1 :
    print("Tapez un des chiffres suivants : ")
    print("  - 1 pour 'Papier': ")
    print("  - 2 pour 'Ciseau': ")
    print("  - 3 pour 'Pierre': ")
    print("  - 0 pour quitter le jeux")

    Val_usr=input()

    if Val_usr=="0" : break

    while Val_usr not in ("1","2","3","0") :
        print("Erreur : Veuillez entrer un des chiffres en haut")
        Val_usr=input()

    Choix_usr=convertion(Val_usr)
    Val_PC=random.uniform(0, 1)
    Choix_PC=convertion_rand(Val_PC)
    print ("")
    print(Nom + " a choisi " + Choix_usr)
    print ("")
    print("Le PC a choisi " + Choix_PC)
    print ("")
    print(PPC(Choix_usr,Choix_PC))
    print ("")

print ("Merci pour avoir jouer à Pierre Papier Ciseau")
print ("Nous vous donnons rendez-vous la prochaine fois")
print("A+")
