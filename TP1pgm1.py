from TP1classes import *

def getCurrency(currency):
    try:
        for i in currencies:
            if i.nom == currency:
                break
                return i
            else:
                print("Currency not found.")
    except:
        print("Error!")

currencies = []
currencies.append( Devise("Euro", "€", "EUR", "Union Européenne", 1) )
currencies.append( Devise("Real", "R$", "BRL", "Brésil", 5.4899) )
currencies.append( Devise("Dolar", "$", "USS", "USA", 1.0897) )
currencies.append( Devise("Franc", "F", "CHF", "Swiss", 1.0080) )

print("currencies", currencies)
while True:
    print("Choose a currency in the list below: ")
    for i in currencies: i.afficherNom()
    choisi = str(input("-> "))
    deviseObj = getCurrency(choisi)



# real = Devise("Real", "R$", "BRL", "Brésil", 5.4899)
# dolar = Devise("Dolar", "$", "USS", "USA", 1.0897)
#franc = Devise("franc", "F", "CHF", "Swiss", 1.0080)

#real.afficher()
#dolar.afficher()
#franc.afficher()

