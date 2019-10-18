# erstelle eine leere dictionary storage
# starte einen endlosschleife 
# mit input gibt es folgende funktionen eingeben, suchen, loeschen, anzeigen, exit
# bei "eingeben" --> 2 neue inputs erzeugt: 1. fuer die id und 2. fuer das produkt --> zur dictionary storage hinzugefuegt
# bei "exit" --> steigt man aus dem programm aus
# bei "anzeigen --> werden ueber alle elemente in storage iteriert und key , value angezeigt
# bei "suchen" --> ein neuer input fuer key als such element, wenn der key in storage vorhanden ist dann print "ja vorhanden", wenn nicht
#		   print "nein nicht vorhanden"
# bei "loeschen" --> ein neuer input fuer key als loesch element, wenn vorhanden ist dann aus der storage dictionary entfernen, wenn nicht
#                --> print "produkt nicht vorhanden zum loeschen"
# ACHTUNG AUF UNGUELTIGE EINGABEN!

products = {
    'id': 'produkt',
    'id2': 'produkt2'
}


def eingeben():
    item_id = input('Waren ID eingeben: ')
    error_id = 0
    error_product = 0
    for id in products:
        if item_id == id:
            error_id += 1
            print('ID schon vergeben')
            return
    item_product = input('Waren Bezeichnung eingeben: ')
    for id, product in products.items():
        if item_product == product:
            error_product += 1
            print('Produkt ist bereit einer anderen ID zugewiesen')
            return

    print('eingabe möglich')
    products[item_id] = item_product
    print('eingabe')


def suchen():
    print('suche')
    search_item = input('Welches Produkt suchen Sie?')
    found = 0
    for id, product in products.items():
        if product == search_item:
            found += 1

    if found > 0:
        print('ja vorhanden')
    else:
        print('nein nicht vorhanden')


def loeschen():
    print('löschen')
    found = ''
    del_item = input('Welches Produkt soll gelöscht werden? ')
    for id, product in products.items():
        if product == del_item:
            found = id
            print(found)
    if found:
        products.pop(found)
    else:
        print('produkt nicht vorhanden zum loeschen')


def anzeigen():
    print('anzeigen')
    for id, product in products.items():
        print('{} -> {}'.format(id, product))


def exit():
    print('exit')
    quit()


while True:
    operation = input("Bitte gib die gewünscht Operation ein: ")

    if operation == 'exit':
        exit()
    elif operation == 'anzeigen':
        anzeigen()
    elif operation == 'loeschen' or operation == 'löschen':
        loeschen()
    elif operation == 'suchen':
        suchen()
    elif operation == 'eingeben':
        eingeben()
    else:
        print('Falsche Eingabe!')