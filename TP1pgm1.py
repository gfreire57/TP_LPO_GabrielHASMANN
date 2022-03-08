from TP1classes import *

def getCurrency(currency):
    try:
        for i in currencies:
            if i.nom == currency:
                print("Achado")
                break
            # verificar forma de alertar caso nao haja aquele nome na lista
        return i
    except:
        print("Error!")

currencies = []
currencies.append( Devise("Euro", "€", "EUR", "Union Européenne", 1) )
currencies.append( Devise("Real", "R$", "BRL", "Brésil", 5.4899) )
currencies.append( Devise("Dolar", "$", "USS", "USA", 1.0897) )
currencies.append( Devise("Franc", "F", "CHF", "Swiss", 1.0080) )

while True:
    print("Choose a currency in the list below: ")
    for i in currencies: i.afficherNom()
    choisi = str(input("-> "))
    deviseObj = getCurrency(choisi) # função devolve objeto de nome armazenado em choisi
    valueFrom = float(input("Value to convert: " )) # valor de origem para converter
    valueEuro = Prix(valueFrom, deviseObj) # devolve valor de saída
    if (input("Another consult? (Y/n): ") in ('Y', 'y') ):
        print('\n')
    else: break




# real = Devise("Real", "R$", "BRL", "Brésil", 5.4899)
# dolar = Devise("Dolar", "$", "USS", "USA", 1.0897)
#franc = Devise("franc", "F", "CHF", "Swiss", 1.0080)

#real.afficher()
#dolar.afficher()
#franc.afficher()

