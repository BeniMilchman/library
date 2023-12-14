import json
from book_options import check_customer_name


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

