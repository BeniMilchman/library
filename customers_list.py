import json


def display_customers():
 customers_file = open("customers.json" , "r")
 customers = json.load(customers_file)
 customers_file.close()
 print("Customers: \n")
 for customer in customers:
   print(customer,"\n")
   
