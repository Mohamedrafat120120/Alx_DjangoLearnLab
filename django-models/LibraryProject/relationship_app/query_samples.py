from .models import Author,Book,Librarian,Library

def get_library_by_name(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library
    except Library.DoesNotExist:
        return None
all_books_specific_author=Book.objects.get(author="michel")
librarian=Library.objects.get(name=Librarian.name)