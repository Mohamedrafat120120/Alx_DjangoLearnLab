Book_deleted=Book.objects.get(title="Nineteen Eighty-Four")
Book_deleted.delete()
(1, {'bookshelf.Book': 1})
all_Books=Book.objects.all()
#output
