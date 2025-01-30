# Author: Sunil Kumar
# Date: 29th Jan, 2025
# Library management live project
# Constructs the library management project
# Core objective: develop the management activity
# Attributes: list of books, borrow books, return books, donate books
# User attributes: request books, return books, donate books

class Library:
    def __init__(self, list_of_books):
        self.books = list_of_books

    def display_books(self):
        print("------ List of available books in the library ------")
        for book in self.books:
            print(book)

    def borrow_book(self, name, book_name):
        if book_name not in self.books:
            print(f"Sorry, {book_name} is not available in the library right now. Please try again later.")
        else:
            tracke.append({name: book_name})
            print(f"{book_name} has been issued to {name}. Please keep it safe and return it within 30 days.")
            self.books.remove(book_name)

    def return_book(self, book_name):
        for record in tracke:
            if book_name in record.values():
                self.books.append(book_name)
                print(f"{book_name} has been returned. Thank you for returning the book on time.")
                tracke.remove(record)
                return
        print(f"Sorry, {book_name} was not issued from this library. Please check the book name and try again.")

    def donate_book(self, book_name):
        print(f"Thank you for donating {book_name}. The book has been added to the library.")
        self.books.append(book_name)


class Student:
    def request_book(self):
        print("Welcome to the Borrow Portal! Please tell us your name and the book you want to borrow.")
        self.book = input("Enter the name of the book you want: ")
        return self.book

    def return_book_student(self):
        print("Welcome to the Return Portal!")
        name = input("Enter your name: ")
        self.book = input("Enter the book you want to return: ")
        for record in tracke:
            if record.get(name) == self.book:
                tracke.remove(record)
                return self.book
        print(f"Sorry, {self.book} was not issued to {name}.")
        return None

    def donate_book(self):
        print("Welcome to the Donation Portal!")
        self.book = input("Enter the name of the book you want to donate: ")
        return self.book
              
    def list_donated_books(self):
        name = input("Enter your name:")
        print(f"Dear, {name}, Welcome to your Donated Book Portal !!!")
        donated_books = [record[name] for record in tracke if name in record] 
        if donated_books:
            print("Here is the list of books you have donated in Safal Library")
            for book in donated_books:
                print(book)
            else:
             print("You have not donated any book yet.")      
                        

        
if __name__ == "__main__":
    Safal_library = Library(['Stats Vol1', 'Programming with Java', 'Python', 'Advanced SQL', 'Power BI', 'JavaScript', 'Database Management', 'NoSQL', 'React JS'])
    student = Student()
    tracke = []  # Holds the current changes

    print("\n\n----- Welcome to the Safal Library ------")
    print("Select from the options below what you want to do: \
        \n 1. List of all books \
        \n 2. Request a book to borrow \
        \n 3. Return a book \
        \n 4. Donate a book \
        \n 5. Track your issued books \
        \n 6. Your Donated books \
        \n 7. Exit")

    while True:
        usr_response = int(input('Please Enter your choice of action between 1 to 7 :- '))

        if usr_response == 1:
            Safal_library.display_books()
        elif usr_response == 2:
            Safal_library.borrow_book(input('Enter your name: '), student.request_book())
        elif usr_response == 3:
            returned_book = student.return_book_student()
            if returned_book:
                Safal_library.return_book(returned_book)
        elif usr_response == 4:
            Safal_library.donate_book(student.donate_book())
        elif usr_response == 5:
            print("Welcome to the Tracker Portal!")
            username = input('Enter your name: ')
            flag = 0
            for issue in tracke:
                if username in issue:
                    print(f'{username}: BORROWED {issue[username]}')
                    flag = 1
                    break
            if flag == 0:
                print(f'{username} has no books issued under your name.')
        elif usr_response == 6:
            student.list_donated_books        
        elif usr_response == 7:
            print("Thank you for visiting the Safal Library portal! See you soon!")
            exit()
        else:
            print("INVALID RESPONSE! Please enter a choice between 1 to 6.")
