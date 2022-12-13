class User():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def borrow_book(self, book):
        if self.role == "basic":
            return book.borrow_book()
        return False

    def return_book(self, book):
        if self.role == "basic":
            return book.return_book()
        return False

    def reserve_book(self, book):
        if self.role == "basic":
            return book.reserve_book()
        return False

    def add_book_to_shelf(self, shelf, book):
        if self.role == "librarian":
            shelf.add_book(book)
            return True
        return False

    def remove_book_from_shelf(self, shelf, book):
        if self.role == "librarian":
            shelf.remove_book(book)
            return True
        return False

    def edit_book_details(self, book, new_name, new_author, new_isbn):
        if self.role == "librarian":
            book.name = new_name
            book.author = new_author
            book.isbn = new_isbn
            return True
        return False