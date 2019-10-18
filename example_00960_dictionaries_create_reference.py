# erstelle dictionary 'christian': 50, 'bettina': 100, 'doris': 75, 'alfred': 10
punkte = {
    'christian': 50,
    'bettina': 100,
    'doris': 75,
    'alfred': 10
}

# change punkte von alfred auf 30
punkte['alfred'] = 30
print(punkte)

# erstelle eine liste mit 2 nachnamen und fuege ihren alter und
# vornamen als liste in form von value hinzu
users = ["Lang", "Kurz"]

users.insert(1, [38, "Thomas"])
users.insert(3, [20, "Simone"])
print(users)




# Iteration und alle Elemente einzeln aufzeigen
for user in users:
    if isinstance(user, list):
        for dates in user:
            print(dates)
    else:
        print(user)
