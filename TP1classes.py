class Devise: #currency
    def __init__(self, nnom, symb, ccode, ppays, ttaux):
        self.nom = nnom
        self.symbole = symb
        self.code = ccode
        self.pays = ppays
        self.taux =  ttaux
        
    def afficher(self): # affiche les chiffres de l'objet
        print(f"Devise:\n* Nom: {self.nom}\n* Symbole: {self.symbole}\n* Code: {self.code}\n* Pays: {self.pays}\n* Taux: {self.taux}\n")
        
    def afficherNom(self): # affiche les chiffres de l'objet
        print(f"*{self.nom}")
        
class Prix(): #convert 
    def __init__(self, val, origine):    
        self.convert = val*(1/origine.taux)
        print("Conversion de {}{:.2f} en Euro: {:.2f} €".format(origine.symbole, val, self.convert))