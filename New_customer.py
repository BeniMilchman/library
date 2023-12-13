from class_customer import Customer
import random
import json


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
 json.dump(customers, customers_file) 
 customers_file.close()

