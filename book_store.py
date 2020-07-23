class Author:

    def __init__(self,author_name,author_age,nationality):
        self.author_name=author_name
        self.author_age=author_age
        self.nationality=nationality

class Book:

    def __init__(self,book_name,book_price,author):
        self.book_name=book_name
        self.book_price=book_price
        self.author=author

    def get_book_name(self):
        return self.book_name

    def get_author_name(self):
        return self.author.author_name

class BookWorld:
    
    def __init__(self,book_obj):
        self.book_obj=book_obj

    def affortable_price(self):
        print("\nBook name and Author name of all affortable price:\n")
        self.aff_books=dict()
        for book in book_obj:
            if book.book_price<1000:
                self.aff_books[book.get_book_name()]=book.get_author_name()
        return self.aff_books

    def calc_print_book_price(self):
        print("Price of all the books in the store:\n")
        for book in book_obj:
            print(book.get_book_name()+"-\t","Rs."+str(book.book_price))

def print_num_of_books_of_author():
    author_name_list=[]
    for book in book_obj:
        author_name_list.append(book.get_author_name().lower().strip())
    print("The total number of books written by "+aut_name+":",author_name_list.count(aut_name))
        
    
guido=Author("Guido van rossum",64,"Dutch")
martin=Author("Martin Odersky",61,"German")
james=Author("James Gosling",65,"Canadian")
dennis=Author("Dennis ritchie",79,"American")
bjarne=Author("Bjarne Stroustrup",69,"Danish")

python=Book("Python",999,guido)
scala=Book("Scala",1500,martin)
java=Book("Java",800,james)
c=Book("C",1999,dennis)
c_plus=Book("C++",1499,bjarne)
generic_java=Book("GenericJava",599,martin)

book_obj=[python,scala,java,c,c_plus,generic_java]
book_shop=BookWorld(book_obj)
book_shop.calc_print_book_price()

for key,value in book_shop.affortable_price().items():
    print(key,":",value)
aut_name=input("\nEnter the author name: ").lower().strip()
print_num_of_books_of_author()

'''
output:-

Price of all the books in the store:

Python-	 Rs.999
Scala-	 Rs.1500
Java-	 Rs.800
C-	 Rs.1999
C++-	 Rs.1499
GenericJava-	 Rs.599

Book name and Author name of all affortable price:

Python : Guido van rossum
Java   : James Gosling
GenericJava : Martin Odersky

Enter the author name: martin odersky
The total number of books written by martin odersky: 2
'''
