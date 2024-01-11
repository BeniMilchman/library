import json
from new_loans import add_new_loan
from class_book import Book
import random

  

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
        add_new_loan(book_title, book['Type'], customer['CusID'] , book['BookID'], loan_date)   
  customers_file = open("customers.json" , "w")
  json.dump(customers, customers_file, indent = 1) 
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
  loans_file = open("loans.json" , "w")
  loans = json.dump(loans, loans_file, indent = 1)
  loans_file.close()    
  customers_file = open("customers.json" , "w")
  json.dump(customers, customers_file, indent = 1) 
  customers_file.close()



def display_books():
  books_file = open("books.json" , "r")
  books = json.load(books_file)
  books_file.close()
  print("Books: \n")
  for book in books:
   print(book,"\n")
   
      
def find_book_by_name():
  books_file = open("books.json" , "r")
  books = json.load(books_file)
  books_file.close()
  book_title = input("Please enter book title:")
  if not check_book(book_title,books):
   print("this book is not in our library")
  else:
   for book in books:
    if book_title == book['title']:
     print(book) 
  
    
    
def add_book():

 checkID = 0
 title = input("Please enter book Title:")
 author = input("Please enter book Author:")
 year = input("Please enter Publication Year:")
 type = input("Please select book type(1/2/3): ")
 if type != '1' and type != '2' and type != '3':
    print("Please insert a valid Type.\n")
 else:    
  books_file = open ("Books.json","r") 
  books = json.load(books_file)
  books_file.close()
  if check_book(title , books):
     print("This book is already exist in the library.\n")
  else:
     
   while True:
     BookID = random.randint(2, 10000)
     for book in books:
        if BookID == book['BookID']:
           checkID = 1
           break
     if checkID != 1:
        break
   new_book = Book(title, BookID, author, year, type) 
   B = { "Title": new_book.title,
        "BookID": new_book.BookID,
        "Author": new_book.author,
        "Year": new_book.year,
        "Type": new_book.type
       }
   books.append(B)
   print("\nThe book has been added to library\n") 
   
   books_file = open ("Books.json","w")
   json.dump(books, books_file, indent = 1) 
   books_file.close()
   

        

  
def remove_book_from_library():

  books_file = open("books.json" , "r")
  books = json.load(books_file)
  books_file.close()
  book_title = input("Please enter book title:")
  if not check_book(book_title,books):
   print("this book is not in our library")
  else:
    for book in books:
      if book_title == book["Title"]:
        books.remove(book)
        print("\nThe book has been removed from the library\n")
    books_file = open ("Books.json","w")
    json.dump(books, books_file, indent = 1) 
    books_file.close()     

 

    





    
   



     
 

