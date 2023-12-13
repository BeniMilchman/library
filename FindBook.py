import json
from book_options import check_book

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
  
    