class library:
    def __init__(self):
        self.nobooks = 0
        self.books = []
        
    def addbook(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)
        
    def showinfo(self):
        print(f"The library has {self.nobooks} books. The books are:- ")
        for book in self.books:
            print(book)
        
l = library()
l.addbook("1) The Power of Your Subconscious Mind")
l.addbook("2) The Alchemist")
l.addbook("3) Rich Dad Poor Dad")
l.addbook("4) Atomic Habits")
l.showinfo()