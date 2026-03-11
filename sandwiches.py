sandwiches = ['veg','pastrami','tuna','pastrami','chicken','pastrami','cheese']
finished_sandwiches=[]
print('Deli has run out of Pastrami')
while sandwiches:
    making = sandwiches.pop()
    if making != 'pastrami':
        print('I am making you a ',making,'sandwich.')
        finished_sandwiches.append(making)
print('following Sandwiches are made: ',finished_sandwiches)