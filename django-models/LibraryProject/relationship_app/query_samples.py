from .models import Author,Book,Librarian,Library

all_books_specific_author=Book.objects.get(author="michel")
all_books=Book.objects.all()
librarian=Library.objects.get(name=Librarian.name)