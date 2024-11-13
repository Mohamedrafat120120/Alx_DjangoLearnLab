from .models import Author,Book,Librarian,Library

def get_library_by_name(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library
    except Library.DoesNotExist:
        return None

def get_all_books_in_library(library_name):
    library = get_library_by_name(library_name)
    if library:
        return library.books.all()  
    return []
def get_author(author):
  try:  
    author=Author.objects.get(name=author)
    return author
  except Author.DoesNotExist:
      return None
def get_book(author):
    author=get_author("michel")
    try:
        book=Book.objects.filter(author=author)
    except Book.DoesNotExist:
        return None
librarian=Library.objects.get(name=Librarian.name)