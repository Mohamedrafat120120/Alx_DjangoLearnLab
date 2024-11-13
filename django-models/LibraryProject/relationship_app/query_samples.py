from .models import Author,Book,Librarian,Library

all_books=Library.objects.get(name="library_name")
all_books_specific_author=Book.objects.get(author="michel")
librarian=Library.objects.get(name=Librarian.name)