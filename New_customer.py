from class_customer import Customer
import random
import json




def check_customer_name(customer_name,customers):
 for customer in customers:
  if customer_name == customer['Name']:
   return True 
 return False
 




def add_customer():
 checkID = 0
 name = input("What is your full name?")
 age = input("please tell us your age:")
 city = input("where are you from?")
 customers_file = open ("customers.json","r") 
 customers = json.load(customers_file)
 customers_file.close()
 while True:
    CusID = random.randint(2, 10000)
    for customer in customers:
       if CusID == customer['CusID']:
          checkID = 1
          break
    if checkID != 1:
       break
 new_customer = Customer(name, CusID, age, city,  []) 
 C = { "Name": new_customer.name,
       "CusID": new_customer.CusID,
       "Age": new_customer.age,
       "City": new_customer.city,
       "Loaned_books": new_customer.loaned_books, 
       }
 customers.append(C)
 print("\nYou have signed in successfuly!\n")
 customers_file = open ("customers.json","w")
 json.dump(customers, customers_file, indent = 1) 
 customers_file.close()


 


def find_customer_by_name():
 customers_file = open("customers.json" , "r")
 customers = json.load(customers_file)
 customers_file.close()
 customer_name = input("please enter customer name:")
 if not check_customer_name(customer_name,customers):
  print("name of customer does not exict, try again")
 else:
  for customer in customers:
   if customer_name == customer['Name']:
    print(customer)





def display_customers():
 customers_file = open("customers.json" , "r")
 customers = json.load(customers_file)
 customers_file.close()
 print("Customers: \n")
 for customer in customers:
   print(customer,"\n")






def remove_customer_from_library():
 
 customers_file = open("customers.json" , "r")
 customers = json.load(customers_file)
 customers_file.close()

 customer_name = input("Please enter customer's name:")
 if not check_customer_name(customer_name,customers):
  print("Name of customer does not exict, try again")

 else:
   for customer in customers:
      if customer_name == customer['Name']:
        customers.remove(customer)
   print("Customer has been removed\n")  
   customers_file = open("customers.json" , "w")
   json.dump(customers, customers_file, indent = 1)
   customers_file.close   

