import json





def display_books():
  books_file = open("books.json" , "r")
  books = json.load(books_file)
  books_file.close()
  print("Books: \n")
  for book in books:
   print(book,"\n")
   

    