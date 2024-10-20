# TODO Найдите количество книг, которое можно разместить на дискете

memory = 1.44
pages = 100
lines = 50
symbols = 25
initial_bytes = 4

volume_bytes = initial_bytes * symbols * lines * pages
volume_mbytes = volume_bytes / 1024 / 1024

books = memory // volume_mbytes

print("Количество книг, помещающихся на дискету:", int(books))
