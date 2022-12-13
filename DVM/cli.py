from fBook import Book
from fShelf import Shelf
from fUser import User
import logging
def __init__(self):
    self.role=input("Enter your role")
    b1=Book(input("Enter Book Name","Enter Book Author","Enter ISBN Code"))
    s1=Shelf(input("Enter Book Genre",b1))
    