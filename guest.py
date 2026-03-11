guest_list=['elon','nikola','leonardo']
print("hey, "+guest_list[0],'you are invited to the party')
print("hey, "+guest_list[1],'you are welomed to the party')
print("hey, "+guest_list[2],'you are the party')

print("\nUnfortunately, "+guest_list[0]+" couldn't make to the party")
guest_list[0] = "Isasc"
print("\n")
print("hey, "+guest_list[0],'you are invited to the party')
print("hey, "+guest_list[1],'you are welomed to the party')
print("hey, "+guest_list[2],'you are the party')

print("\ncongratulations guys, we found a bigger table")
guest_list.insert(0,input("enter a guest you wanna invite: "))
guest_list.append(input("enter a guest you wanna invite: "))
guest_list.insert(int(len(guest_list)/2),input("enter a guest you wanna invite: "))

for i in range(len(guest_list)):
    print ("\nhey, "+guest_list[i],'you are invited to the party')


print("\n\toops, table won't be available at the time of the party")
for i in range(len(guest_list)-2):
    print("\n I am verry sorry Mr."+guest_list.pop()+", unfortunately you are not invited")

print("\nMr."+guest_list[0],"you are still invited to the party")    
print("Mr."+guest_list[1],"you are still invited to the party")  

del guest_list [0:2]
print(guest_list)