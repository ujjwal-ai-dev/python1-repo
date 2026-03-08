import numpy as np
alien = ['red','yellow','green']
dead_alien = np.random.choice(alien)
print (dead_alien)

if dead_alien == 'green':
    print('you scored 5 points')
elif dead_alien == 'yellow':
    print('you scored 10 points')
else:
    print('you scored 20 points')
        
