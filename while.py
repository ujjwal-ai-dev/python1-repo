# all_toppings=''
# toppings=''
# while toppings != 'quit':
#     toppings = input('enter the topping you want to add on your pizza: ')
#     if toppings.lower() != 'quit':
#         all_toppings = all_toppings + ' ' + toppings
# print('following toppings are added to your pizza: ',all_toppings)


# watch = ''
# while watch != 'no':
#     watch = input('do you want to watch a movie? (yes/no): ')
#     if watch.lower()!='no':
#         age = int(input('enter you age: '))
#         if age < 3:
#             print('your ticket is free')
#         elif age < 12:
#             print('your ticket costs $10')
#         else:
#             print('your ticket cots $15')    



# watch = True
# while watch == True:
#     watch1 = input('do you want to watch a movie? (yes/no): ')
#     if watch1.lower()=='no':
#         watch = False
#     else:    
#         age = int(input('enter you age: '))
#         if age < 3:
#             print('your ticket is free')
#         elif age < 12:
#             print('your ticket costs $10')
#         else:
#             print('your ticket cots $15')  



watch = True
while watch == True:
    watch1 = input('do you want to watch a movie? (yes/no): ')
    if watch1.lower()=='no':
        break
    else:    
        age = int(input('enter you age: '))
        if age <= 3:
            print('your ticket is free')
        elif age <= 12:
            print('your ticket costs $10')
        else:
            print('your ticket cots $15')    