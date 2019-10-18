# erstelle eine liste mit folgenden elementen: "protons", "neutronen", "elektronen"

# oeffne die datei particles.txt und speichere die element ab mit einem komma als trennzeichen


elements = ["protons", "neutronen", "elektronen"]

with open("particles.txt", "w") as element_file:
    save = ''
    c = 0
    for element in elements:
        c += 1
        save += element
        if c < 3:
            save += ', '
    element_file.write(save)