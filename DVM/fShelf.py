class Shelf():
    def __init__(self, genre):
        self.genre = genre
        self.books = []
        self.book_count = 0

    def show_catalog(self):
        print("Books on the shelf:")
        for i in self.books:
            print("- " + i.name)

    def add_book(self, book):
        self.books.append(book)
        self.book_count += 1

    def remove_book(self, book):
        self.books.remove(book)
        self.book_count -= 1

    def get_books_count(self):
        return self.book_count

    def populate_book(self):
        from popscript import populate
        populate(input("Enter Filename"))
