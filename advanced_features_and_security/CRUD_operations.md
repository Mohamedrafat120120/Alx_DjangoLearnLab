Book_instance=Book.objects.create(title="1984",author="George Orwell",publication_year=1949)
#output
# <Book: 1984>


Book_retrive=Book.objects.all()
#output
# <QuerySet [<Book: 1984>]>

Book_update=Book.objects.get(title="1984")
Book_update.title="Nineteen Eighty-Four"
Book_update.save()
#output
# <Book: Nineteen Eighty-Four>



Book_deleted=Book.objects.get(title="Nineteen Eighty-Four")
Book_deleted.delete()
(1, {'bookshelf.Book': 1})
all_Books=Book.objects.all()
#output
# <QuerySet []><|eom_id|><|start_header_id|>assistant