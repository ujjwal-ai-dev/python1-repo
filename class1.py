class Resturant():
        def __init__(self,resturant_name,cusine_type):
                self.resturant_name = resturant_name
                self.cusine_type = cusine_type
                self.no_costumers = 0
        def describe_resturant(self):
                print("The name of the resturant is " + self.resturant_name) 
                print('This resturant sells '+ self.cusine_type+' cusine.')               
        def open_resturant(self):
                print(self.resturant_name+' is open.')  
        def costumers_served(self):
                print("total numbers of costumers seved are :"+ str(self.no_costumers) )              
        def update_costumers_served(self,costumer_served):
                self.costumer_served = costumer_served
                if self.costumer_served >= self.no_costumers:
                        self.no_costumers = self.costumer_served
                else:
                        print('no. of costumers served cannot be reduced.')
        def increment_no_costumer_served(self,number):
                self.number = number
                self.no_costumers += self.number


resturant = Resturant("Poonam's kitchen","Indian")
resturant.describe_resturant()
resturant.costumers_served()
resturant.no_costumers = 5
resturant.costumers_served()
resturant.update_costumers_served(1)
resturant.costumers_served()
resturant.increment_no_costumer_served(12)
resturant.costumers_served()




# resturant2=Resturant("Sankey's Kitchen","All")
# resturant2.describe_resturant()

# resturant3=Resturant("Laddu's Kitchen","American")
# resturant3.describe_resturant()

# class Costumer():
#         def __init__(self,first_name,last_name,orders):
#                 self.first_name = first_name
#                 self.last_name = last_name
#                 self.orders = orders
#         def place_orders(self):
#                 print(f"Following are the orders of {self.first_name} {self.last_name}:")
#                 print(f"\t {self.orders}\n") 


# costumer1 = Costumer("Ujjwal","Gupta","Paneer Chilli")
# costumer2 = Costumer('prince',"yadav",'burger')
# cosstumer3 = Costumer('Rajan','Yadav','mutton')                      


# costumer1.place_orders()
# costumer2.place_orders()
# cosstumer3.place_orders()
