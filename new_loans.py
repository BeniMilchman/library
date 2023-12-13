import json
from class_loan import loan


def add_new_loan(book_title, book_type, CusID, BookID, loandate):
 loans_file = open("loans.json" , "r")
 loans = json.load(loans_file)
 loans_file.close()
 new_loan = loan(book_title,book_type, CusID, BookID, loandate, returndate = '')

 L = {"Title": new_loan.book_title,
      "Type": new_loan.book_type,
      "CusID": new_loan.CusID,
      "BookID": new_loan.BookID,
      "Loan date": new_loan.loandate,
      "Return date": new_loan.returndate

      } 
 loans.append(L)
 loans_file = open ("loans.json","w")
 json.dump(loans, loans_file) 
 loans_file.close()









 
