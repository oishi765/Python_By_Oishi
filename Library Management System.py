
print("Welcome to the Library Management System")

books = {}

def add_book():
    name = input("Book name: ")
    books[name] = "Available"

def borrow_book():
    name = input("Book name: ")
    if books.get(name) == "Available":
        books[name] = "Borrowed"
        print("Borrowed")
    else:
        print("Not available")

add_book()
borrow_book()
print(books)
