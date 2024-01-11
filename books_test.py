from book_options import check_book
import json

def check_book_test():
 books_file = open("books.json" , "r")
 books = json.load(books_file)
 books_file.close()
 assert check_book("the hunger games", books) == True
 
 assert check_book("alice in wonderland", books) == False
  