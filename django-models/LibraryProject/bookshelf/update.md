Book_update=Book.objects.get(title="1984")
Book_update.title="Nineteen Eighty-Four"
Book_update.save()
#output