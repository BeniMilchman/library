
class Customer:
    def __init__(self, name, CusID, age, city, loaned_books = [],):
        self.name = name
        self.CusID = CusID
        self.city = city
        self.age = age
        self.loaned_books = loaned_books
