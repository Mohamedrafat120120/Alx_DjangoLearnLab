from .models import Author,Book,Librarian,Library

all_books_specific_author=Book.objects.get(author="michel")
all_books=Library.objects.get(name="kdfk")
librarian=Library.objects.get(name=Librarian.name)