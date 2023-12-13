import json
from new_loans import add_new_loan




class loan:
    def __init__(self, CustID, BookID, Loandate, Returndate):
        self.CustID = CustID
        self.BookID = BookID
        self.Loandate = Loandate 
        self.Returndate = Returndate    



def check_customer_name(customer_name,customers):
 for customer in customers:
  if customer_name == customer['Name']:
   return True 
 return False
 
def check_book(book_title,books):
  for book in books:
   if book_title == book['Title']:
    return True 
  return False
 




def loan_book():
 customers_file = open("customers.json" , "r")
 customers = json.load(customers_file)
 customers_file.close()

 customer_name = input("please enter your name:")
 if not check_customer_name(customer_name,customers):
  print("name of customer does not exict, try again")
 else:
  books_file = open("books.json" , "r")
  books = json.load(books_file)
  books_file.close()
  book_title = input("Please enter book title:")
  if not check_book(book_title,books):
   print("This book is not in our library")
  else:
   loan_date = input("Please enter loan date:")
   #return_date = input("Please enter return date:")  
   for book in books:
    if book_title == book['Title']:
     for customer in customers:
      if customer_name == customer['Name']:
       if book_title in customer['Loaned_books']:
        print("The book is already loaned")
       else: 
        customer['Loaned_books'].append(book_title)
        print("You have loaned the book successfuly")
        if book['Type'] == '1':
         print("You have 10 days to return this book to library.\n")
        elif book ['Type'] == '2':
         print("You have 5 days to return this book to library.\n")
        elif book ['Type'] == '3':
         print("You have 2 days to return this book to library.\n")
        add_new_loan(book_title, customer['CusID'] , book['BookID'], loan_date)   
  customers_file = open("customers.json" , "w")
  json.dump(customers, customers_file) 
  customers_file.close()


def return_book():
   
 customers_file = open("customers.json" , "r")
 customers = json.load(customers_file)
 customers_file.close()

 customer_name = input("Please enter your name:")
 if not check_customer_name(customer_name,customers):
  print("Name of customer does not exict, try again")
 else:
  loans_file = open("loans.json" , "r")
  loans = json.load(loans_file)
  loans_file.close() 

  book_title = input("Please enter book title:")
  return_date = input("\nPlease enter return date:")

  for customer in customers:
   if customer_name == customer['Name']:
    customer['Loaned_books'].remove(book_title)
    print("The book has been returned to library\n")
    for loan in loans:
     if loan['Title'] == book_title and loan['CusID'] == customer['CusID']:
      loan['Return date'] = return_date
  #print(customers) 
  loans_file = open("loans.json" , "w")
  loans = json.dump(loans, loans_file)
  loans_file.close()    
  customers_file = open("customers.json" , "w")
  json.dump(customers, customers_file) 
  customers_file.close()




      
   

  


 

    





    
   



     
 

