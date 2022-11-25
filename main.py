## dit is eeen dictionary van het menu, hierbij staan alle soorten koffie die je kan kiezen hiernaast kan staat er ook de ingredieten en de kosten
menu = {
    "espresso":{
        "ingredient":{
            "water": 40,
            "coffe": 30,
        },
        "kosten":2.0,
    },
    "dubbele espresso":{
        "ingredient":{
            "water": 80,
            "coffe": 60,
        },
        "kosten":3.5,
    },
    "koffie verkeerd":{
        "ingredient":{
            "water": 150,
            "coffe": 30,
            "melk": 80,
        },
        "kosten":3.5,
    },
    "cappucino":{
        "ingredient":{
            "water": 150,
            "coffe": 30,
            "melk": 80,
        },
        "kosten":3.5,
    }
 }

winst = 0

is_aan = True


resource = {"water": 2000,
          "coffe": 1000,
          "melk": 2000,
}


def is_er_genoeg(inputs): # dit is om te checken  of er genoeg ingredietn om de koffie te maken
    for item in inputs:
        if inputs[item] >= resource[item]:
            print(f'er is niet genoeg ingredient {item}')
        return True # om te gaan naar de volgende proces


def proces_coin():
    """ in dit functie worden de totalen ingevoerde coins geretourneerd"""
    print("voer uw munten in")
    total = int(input("hoeveel 50 cent?")) * 0.5
    total += int(input("hoeveel 1 euro?")) * 1.0
    total += int(input("hoeveel 2 euro?")) * 2.0
    return total


def transactie_is_succesvol(ontvangen_geld, kosten_koffie):
    """retourneer true als betaling is geaccepteerd of return False als te weinig geld is ontvangen"""
    if ontvangen_geld >= kosten_koffie:
        change = ontvangen_geld - kosten_koffie  # dit berekent het wisselgeld
        print(f'hier is wissel geld {change}')
        global winst
        winst += kosten_koffie
        """ik wil dat wanneer elke keer een transactie succcesvol 
        is dat alle kosten van de koffie wordt bij elaar opgeteld en opgeslagen bij money"""
        return True
    else:
        print("sorry  is niet genoeg geld")
        return False

def koffie_maken(name, ingredient):
    for item in ingredient:
        resource[item] -= ingredient[item]
        print(f'hier is je {name} ')


while is_aan:
    kiezen = input("wat wil je hebben? espresso/dubbele espresso/ koffie verkeerd/ cappucino: ")
    if kiezen == "uit":
        is_aan = False
    elif kiezen == "overzicht":  # wanner je bij het menu overzicht kies krijg je te zien hoeveel ingredient je heb  op de machine en hoeveel geld is verdient
        print(f'water: {resource["water"]}ml')
        print(f'koffie:  {resource["coffe"]}g')
        print(f'melk:  {resource["melk"]} ml')
        print(f'geld: $ {winst}')
    else:
        drink = menu[kiezen]
        if is_er_genoeg(drink["ingredient"]):
            pay = proces_coin()
            if transactie_is_succesvol(pay, drink["kosten"]):
                koffie_maken(kiezen, drink["ingredient"])
