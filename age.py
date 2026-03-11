age= int(input("enter your age: "))
if age < 2:
    print("you are a baby")
elif age < 4:
    print ('you are a toddler')
elif age < 13:
    print ('you are a kid')
elif age < 20:
    print ('you are a teenager')
elif age < 65:
    print ('you are an adult')
else:
    print('your are an elder')

favourite_fruits = ['apple', 'banana','mango','guava','litchi']

for fruit in favourite_fruits:
    if fruit == 'peach':
        print('you really like peach')
    if fruit == 'orange':
        print('you really like orange')
    if fruit == 'apple':
        print('you really like apple')
    if fruit == 'mango':
        print('you really like mango')
    if fruit == 'litchi':
        print('you really like litchi')