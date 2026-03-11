# def sandwiches(*items):
#     print('followig items were added to your sandwiches:\n',items)

# sandwiches('a','b','c')
# sandwiches('a')
# sandwiches('a','b')

# def user_profile(first,last,**others):
#     profile={}
#     profile['first_name']=first
#     profile['last_name']=last
#     for key,values in others.items():
#         profile[key]=values
#     return profile    

# profile1 = user_profile('ujjwal','Gupta',age='25',DOB='2001/01/01')
# print (profile1)

import car_information as ci

car1=ci.car_info('bmw','x1','number plate should be 0','deliver next week',colour='black',seat='4',tow_package=True)
print(car1)
