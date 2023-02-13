import sys

n = len(sys.argv)

print('Petit lundi, grosse semaine')
print('Arguments:', sys.argv)
print('Nb arguments:', n)

if n > 1:
    name = sys.argv[1]
    print('Arg 1:', name)
# elif n < 0:
#     pass
else:
    name = None
print('Dernier argument:', sys.argv[-1])

print('Liste des arguments:')
for arg in sys.argv:
    print('-', arg)

# slices with lists
drinks = sys.argv[2:]
for drink in drinks:
    print('I drink', drink)

# slices with strings
ville = 'Toulouse'
print('3 1ères lettres:', ville[:3])
print('3 dernières lettres:', ville[-3:])

# while example
cpt = 10
while cpt >= 0:
    print(cpt, end=' ')
    cpt -= 1 
print('Boom')

drinkWanted = 'soda'
found = False
for drink in drinks:
    if drink == drinkWanted:
        found = True
        break
if found:
    print('You can drink', drinkWanted, drink)
else:
    print('Sorry, no more', drinkWanted)

for drink in drinks:
    print(drink, end=': ')
    match drink:
        case "coffee" | "tea":
            print('va me reveiller')
        case "water":
            print('bon pour la santé')
        case "soda":
            print('bon et pas bon à la fois')
        case _:
            print('joker')
print()
