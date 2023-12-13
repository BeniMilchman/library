import json
from book_options import check_book





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
    json.dump(books, books_file) 
    books_file.close()     