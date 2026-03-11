
# user = ''
# while not user:
#     user = input('enter your username: ').strip()

# user = user.lower()

# users=['Ujjwal','wazir','prince','guddu','golu','admin']

# users = [u.lower() for u in users]
# print(user)

# if user in users:
#     if user == 'admin':
#         print("Good morning Boss, do you want to see today's report")
#     else:
#         print(f"good morning, {user}, thank you for logging in.")
# else:
#     print('not a valid username')                 

existing_users=['Ujjwal','wazir','prince','guddu','golu','admin']
existing_user_lower=[us.lower() for us in existing_users]
print(existing_user_lower)
new_user=['ram', 'hari','ujjwal','wazir','gagan']
for u in new_user:
    if (u in existing_users) or u.lower() in existing_user_lower :
        print(f'{u}, needs to input a new username')
    else:
        print (f"{u}, is available")    