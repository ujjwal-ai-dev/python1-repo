next_entry=''
name=[]
poll=[]
counter = 0
int(counter)
while next_entry != 'no':
    current_name=input('what is your name: ')
    destination = input('where do you wanna go for vacation: ')
    poll.append(destination)
    name.append(current_name)
    next_entry=input('is there another entry? ')
    
for i in name:
    print(f'{i} wants to go to {poll[counter]}.')
    counter += 1
