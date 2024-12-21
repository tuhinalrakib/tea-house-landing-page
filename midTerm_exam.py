# Library Class

class Library:
    book_list = []

    @classmethod
    def entry_book(self,book):
        return self.book_list.append(book)
    
    @classmethod
    def view_all_book(self):
        if not self.book_list:
            print("No books in the Library")
        else:
            for book in self.book_list:
                book.view_book_info()
    
    @classmethod
    def find_book_by_id(self, book_id):
        for book in self.book_list:
            if book.get_book_id() == int(book_id):
                return book
        return None

# Class Book 

class Book:
    def __init__(self,book_id,title,author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        Library.entry_book(self)

    def get_book_id(self):
        return self.__book_id
    
    def view_book_info(self):
        if self.__availability:
            availability_status = 'Available'
        else:
            availability_status = "Not available"

        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Availability: {availability_status}")

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"The book '{self.__title}' has been borrowed.")
        else:
            print(f"The book '{self.__title}' is already borrowed.")
    
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"The book {self.__title} has been returned")
        else:
            print(f"The book '{self.__title}' was not borrowed.")

# Add books to the library
Book(101, "Python Programming", "John Doe")
Book(102, "Data Science Essentials", "Jane Smith")
Book(103, "Machine Learning", "Alan Turing")
Book(104, "Artificial Intelligence", "Marvin Minsky")
Book(105, "Deep Learning", "Yann LeCun")
Book(106, "Natural Language Processing", "Christopher Manning")

def menu():
    while True:
        print("\n-----Library Menu-----")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if not Library.book_list:
                print("No books in the library.")
            else:
                print("\n--- List of Books ---")
                for book in Library.book_list:
                    book.view_book_info()
        elif choice == "2":
            book_id = input("Enter the book ID to borrow: ")
            book = Library.find_book_by_id(book_id)
            
            if book:
                book.borrow_book()
            else:
                print('Invalid book Id')
        elif choice == "3":
            book_id = input("Enter the book ID to return: ")
            book = Library.find_book_by_id(book_id)

            if book:
                book.return_book()
            else:
                print("Invalid Book Id")
        elif choice == "4":
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid Choice, Please take correct choice")

menu()