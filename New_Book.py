from book_options import check_book
import random
import json


class Book:
    def __init__(self, title, BookID, author, year, type):
        self.title = title
        self.BookID = BookID
        self.author = author
        self.year = year
        self.type = type

def add_book():

 checkID = 0
 title = input("Please enter book Title:")
 author = input("Please enter book Author:")
 year = input("Please enter Publication Year:")
 type = input("Please select book type(1/2/3): ")
 if type != 1 and type != 2 and type != 3:
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
        "type": new_book.type
       }
   books.append(B)
   books_file = open ("Books.json","w")
   json.dump(books, books_file) 
   books_file.close()

        
