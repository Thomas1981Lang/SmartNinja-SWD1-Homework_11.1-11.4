with open('dna.txt', 'r') as dna_file:
    dna_string = dna_file.read()
    print(dna_string)

suspects = {
    'Eva': {
        'gender': 'female',
        'race': 'white',
        'hair_color': 'blonde',
        'eye_color': 'blue',
        'face_shape': 'oval'
    },
    'Larisa': {
        'gender': 'female',
        'race': 'white',
        'hair_color': 'brown',
        'eye_color': 'brown',
        'face_shape': 'oval'
    },
    'Matej': {
        'gender': 'male',
        'race': 'white',
        'hair_color': 'black',
        'eye_color': 'blue',
        'face_shape': 'oval'
    },
    'Miha': {
        'gender': 'male',
        'race': 'white',
        'hair_color': 'brown',
        'eye_color': 'green',
        'face_shape': 'square'
    }
}


dna_profils = {
    'hair_color': {
        "black": "CCAGCAATCGC",
        "brown": "GCCAGTGCCG",
        "blonde": "TTAGCTATCGC"
    },
    'face_shape': {
        "square": "GCCACGG",
        "round": "ACCACAA",
        "oval": "AGGCCTCA"
    },
    'eye_color': {
        "blue": "TTGTGGTGGC",
        "green": "GGGAGGTGGC",
        "brown": "AAGTAGTGAC"
    },
    'gender': {
        "female": "TGAAGGACCTTC",
        "male": "TGCAGGAACTTC"
    },
    'race': {
        "white": "AAAACCTCA",
        "black": "CGACTACAG",
        "asian": "CGCGGGCCG"
    }
}

criminal_profil = {}

for key, value in dna_profils.items():
    # print(key)
    # print(value)
    for attributes, sequence in value.items():
        if dna_string.find(sequence) != 1:
            criminal_profil[key] = attributes
            break

print(criminal_profil)

perpetrator = ''

for name, attribute in suspects.items():
    current_name = ''

    for key, value in attribute.items():
        if criminal_profil[key] == value:
            # print(name)
            current_name = name
        else:
            current_name = ''
            break
    if current_name:
        name = current_name
        break

print("{} eats the ice creame".format(name))