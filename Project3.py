from termcolor import colored

class Library:
    def __init__(self,listofBooks):
        self.books = listofBooks

    def DisplayAvailableBooks(self):
        print(colored(("Books are present in this library: "),'red'))
        for Book in self.books:
            print(" * " + Book.title())

    def BorrowBooks(self,BookName):
        if BookName in self.books:
            print(colored((f"You have been issued {BookName}. Please keep it safe and return within 30 days."),'red'))
            self.books.remove(BookName)
            return True
        else:
            print(colored(("Sorry, This Book is not avilable or either already issued by someone else. Please try after some days."),'red'))
            return False
    
    def returnBooks(self,BookName):
        self.books.append(BookName)
        print(colored(("Thanks for returning or this books. Hope you enjoyed reading this books!"),'red'))

class Students:
    def __init__(self):
        self.Booklist = []
    def requestBooks(self):
        self.book = input("Enter the name of the book you want to borrow it!: ") 
        return self.book
        print(f"You Have Borrowed {self.book}")
    def returnBooks(self):
        self.book = input("Enter the Book name! You want to Return Or Donate : ")
        return self.book
        

if __name__ == "__main__":
    CentralLibrary = Library(['python crash course','python for hackers','C++'])
    student = Students()
    while True:
        welcomemsg =print(colored(('''\n=======Hello, Welcome To The Central Library=======
            Please Select An Option:
            1.List the books.
            2.Borrow a Book.
            3.Add/Return a Book.
            4.Quit The Program.'''),'red'))
        try:
            a = int(input("Choose Any Option: "))
            if a == 1:
                CentralLibrary.DisplayAvailableBooks()   
            elif a == 2:
                CentralLibrary.BorrowBooks(student.requestBooks())
            elif a == 3:
                CentralLibrary.returnBooks(student.returnBooks())
            elif a == 4:
                print(colored(("Thanks For Choosing Central Library. Have a great day ahead!"),'red'))
                exit()
            else:
                print(colored(("This is invaild output. please choose vaild output."),'red'))
        except Exception as e:
            print("Your Choice is must be in a numbers!")
            print(f"{e}")
        except KeyboardInterrupt as e:
            print("KeyBoard Interrupted!")
            print(f" {e}")
