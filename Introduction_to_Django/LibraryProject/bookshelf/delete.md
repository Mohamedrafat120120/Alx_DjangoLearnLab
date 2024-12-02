book=Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
(1, {'bookshelf.Book': 1})
all_Books=Book.objects.all()
#output