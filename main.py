from book_options import loan_book, return_book
from New_customer import add_customer
from New_Book import add_book
from remove_book import remove_book_from_library
from remove_customer import remove_customer_from_library
from books_list import display_books
from customers_list import display_customers
from loans_list import display_loans
from FindCustomer import find_customer_by_name
from FindBook import find_book_by_name




class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Book:
    def __init__(self, title, BookID, author, year, type):
        self.title = title
        self.BookID = BookID
        self.author = author
        self.year = year
        self.Type = type



class Customer:
    def __init__(self, name, CusID, age, city, loaned_books = [],):
        self.name = name
        self.CusID = CusID
        self.city = city
        self.age = age
        self.loaned_books = loaned_books



class loan:
    def __init__(self, CustID, BookID, Loandate, Returndate):
        self.CustID = CustID
        self.BookID = BookID
        self.Loandate = Loandate 
        self.Returndate = Returndate    




Sifriya = Library("Library of the dreams!", "mishol haeshkolot 7b")


def main():
   while True:
    print("Welcome to", Sifriya.name ,"Please tell us what you want to do:\n"  
          "1 - New customer? join us!\n"
          "2 - Add a book to the library\n"
          "3 - Loan a book\n"
          "4 - Return a book\n"
          "5 - Display all of the books in our library\n"
          "6 - Display all of our customers\n"
          "7 - Display all of the loans in our library\n"
          "8 - Display all of the late loans in our library\n"
          "9 - Find book by name\n"
          "10 - Find customer by name\n"
          "11 - Remove a book from the library\n"
          "12 - Remove a customer from library\n")
    option = input("")
    if option == "1":
        add_customer()
    elif option == "2":
        add_book() 
    elif option == "3": 
        loan_book()  
    elif option == "4": 
        return_book()
    elif option == "5": 
        display_books()    
    elif option == "6": 
        display_customers()
    elif option == "7": 
        display_loans()
    #elif option == "8": 
       # remove_book_from_library()
    elif option == "9": 
        find_book_by_name()
    elif option == "10": 
        find_customer_by_name()
    elif option == "11":
        remove_book_from_library()
    elif option == "12":
        remove_customer_from_library()


main()
#loan_book()
#return_book()
#add_customer()
#display_books()
#display_customers()
#find_customer_by_name()
#find_book_by_name()
#remove_book_from_library()
#remove_customer_from_library()



    


