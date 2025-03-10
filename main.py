class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def addBook(self, bookname):
        self.books.append(bookname)
        print(f'"{bookname}" added to the library')

    def showBooks(self):
        if self.books:
            print(f"\n📚 Books Available In {self.name}:")
            for book in self.books: 
                print(f"- {book}")
        else:
            print("😞 No Books In The Library")

    def borrowBooks(self, bookname):
        if bookname in self.books:
            self.books.remove(bookname)
            print(f'✅ You Borrowed "{bookname}", enjoy reading!')
        else:
            print(f'😔 Sorry, "{bookname}" is not available!')

myLibrary = Library("Kid's Library")

myLibrary.addBook("Alice in Wonderland")
myLibrary.addBook("Harry Potter")
myLibrary.addBook("Charlie and The Chocolate Factory")
myLibrary.addBook("Rich Dad and Poor Dad")
myLibrary.addBook("You are born to Blossom")

myLibrary.showBooks()

myLibrary.borrowBooks("Harry Potter")
myLibrary.borrowBooks("Rich Dad and Poor Dad")


myLibrary.showBooks()
