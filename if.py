car = ['toyota','scorpio','audi','penault']
if "toyota" in car:
    print("we have toyota as well")

if "thar" not in car: 
    print("we don't have car")

a = 'boss'
if a == 'boss':
    print('true')

if a != 'Boss':
    print("false")
 

if a.upper() == 'BOSS':
    print (' u the boss')

b = 45

if 50 > b and b > 10:
    print (' right input')

if 50 > b or b > 10:
    print (' among input')


age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + price + ".")