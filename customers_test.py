from customer_options import check_customer_name
import json

 

def test_check_customer_name():

 customers_file = open ("customers.json","r") 
 customers = json.load(customers_file)
 customers_file.close()

 assert check_customer_name ("beni milchman", customers) == True

 assert check_customer_name ("yoval maman", customers) == False




