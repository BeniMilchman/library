import json




def display_loans():
 loans_file = open("loans.json" , "r")
 loans = json.load(loans_file)
 loans_file.close()
 print("Loans: \n")
 for loan in loans:
    print(loan, "\n")
