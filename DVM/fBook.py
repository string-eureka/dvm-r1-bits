class Book():
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.borrowed = False
        self.reserved = False

    def borrow_book(self):
        if not self.borrowed and not self.reserved:
            self.borrowed = True
            return True
        return False

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return True
        return False

    def reserve_book(self):
        if not self.borrowed and not self.reserved:
            self.reserved = True
            return True
        return False