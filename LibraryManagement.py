class CentralLibrary:
    def __init__(self, listbook):
        self.books = listbook

    def displayBooksInfo(self):
        print("The available Books in Library are")
        for book in self.books:
            print("* " + book)

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(
                f"Your book {bookname} is available and has been issued \n Keel the book Safe and do return within 30 Days")
            self.books.remove(bookname)

        else:
            print(
                "Your Book is not available in the library \n Kindly Check Few days later")

    def returnBook(self, bookname):
        print("Thank You for using the book")
        self.books.append(bookname)


class Student:
    def issueBook(self):
        self.bookname = input("Enter the name of Book you want : ")
        return self.bookname

    def returnback(self):
        self.bookname = input("Enter the name of Book you want to return : ")
        return self.bookname


if __name__ == "__main__":
    central = CentralLibrary(
        ["algo", "datas", "python", "java", "datascience"])
    # central.displayBooksInfo()
    stud = Student()
    while(True):
        welcomemsg = '''=-=-=-=-=-=-=-=-WELCOME TO CENTRAL LIBRARY-=-=-=-=-=-=-=-

        Please Choose one of the Options :--
        Enter 1 to Display the List of books available
        Enter 2 to Borrow a book amoung available books
        Enter 3 to Return back a issued books to library
        Enter 4 to EXIT the the CENTRAL LIBRARY of books
        '''
        print(welcomemsg)
        

        a = int(input("Enter Your Choice : "))
        if a == 1:
            central.displayBooksInfo()
        elif a == 2:
            central.borrowBook(stud.issueBook())
        elif a == 3:
            central.returnBook(stud.returnback())
        elif a == 4:
            print("Thanks for using library! \n Have a nice day ")
            exit()
        else:
            print("Enter a valid option to Continue")

        
