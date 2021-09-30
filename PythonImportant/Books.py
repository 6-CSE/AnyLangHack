#This is a comment
class Book():
    def __init__(self, name, author):
        self.copies = 0
        self.name = name
        self.author = author


class Library():
    def __init__(self):
        self.count = 0
        self.books = []

    def insertbook(self, bookname, bookauthor):
        book = Book(bookname, bookauthor)
        if book in self.books:
            for i in range(len(self.books)):
                if self.books[i].name == bookname:
                    self.books[i].copies += 1
        else:
            book = Book(bookname, bookauthor)
            book.copies = 1
            self.books.append(book)

    def removebook(self, bookname):
        for i in self.books:
            if i.name == bookname:
                self.books.remove(i)
                print("removedthebook\n")
                return
        print("book not found\n")

    def searchbook(self, bookname):
        for i in self.books:
            if i.name == bookname:
                return i
        return False


def insert_book(lib):
    bookname = input("type your bookname\n").upper()
    bookauthor = input("type your book author name\n").upper()
    lib.insertbook(bookname, bookauthor)
    print("inserted\n")


def delete_book(lib):
    bookname = input("type your bookname\n").upper()
    lib.removebook(bookname)


def search_book(lib):
    bookname = input("type your bookname\n").upper()
    book = lib.searchbook(bookname)
    if(book):
        print(f'{book.name} author {book.author} has {book.copies} copies\n')
    else:
        print("No book found\n")


def copies_book(lib):
    bookname = input("type your bookname\n").upper()
    for i in lib.books:
        if i.name == bookname:
            print(i.copies)
            print("\n")
            return
    print("Book not found\n")


lib = Library()
while(True):
    i = input("1 to add book \n2 to delete a book \n3 to search book\n4 to get count of total copies of specific book\nq to exit\n")
    if i == '1':
        insert_book(lib)
    if i == '2':
        delete_book(lib)
    if i == '3':
        search_book(lib)
    if i == '4':
        copies_book(lib)
    if i == 'q':
        exit()
#This is appeneded comment