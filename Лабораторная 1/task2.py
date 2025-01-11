mega_bytes = 1.44
pages = 100
lines = 50
chars = 25
bytes = 4

books = (mega_bytes * 1024 * 1024) // (pages * lines * chars * bytes)

print("Количество книг, помещающихся на дискету:", int(books))
