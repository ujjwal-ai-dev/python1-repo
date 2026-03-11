person1 = {'name':'Prince', 'last_name':'Yadav', 'age':'24','city':'Noida'}
person2 = {'name':'Ujjwal', 'last_name':'Gupta', 'age':'25','city':'Birgunj'}
person3 = {'name':'Rajan', 'last_name':'Yadav', 'age':'25','city':'Dhulikhel'}

people = [person1,person2,person3]
for index,p in enumerate(people, start =1):
        print(f"person{index}")
        fn = p['name'] + ' ' + p['last_name']
        print(f"full name: {fn} age: {p['age']} city: {p['city']} \n")

