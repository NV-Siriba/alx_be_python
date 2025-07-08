class Book:
    def __init__(self,title,author,is_checked_out=False):
        self.title=title
        self.author=author
        self._checkout=is_checked_out
class Library:
    def __init__(self):
        self._books=[]
    def add_book(self,book):
        self._books.append(Book)
    def check_out_book(self,book):
        self._books.remove(Book)
    
    def return_book(self,book):
        self._books.append (Book)
    def list_available_books(self):
        print(self._books)






     
