
import json
from book_options import check_customer_name



def find_customer_by_name():
 customers_file = open("customers.json" , "r")
 customers = json.load(customers_file)
 customers_file.close()
 customer_name = input("please enter customer name:")
 if not check_customer_name(customer_name,customers):
  print("name of customer does not exict, try again")
 else:
  for customer in customers:
   if customer_name == customer['name']:
    print(customer)




