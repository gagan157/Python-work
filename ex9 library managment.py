#class library
#lend(rent) book -(whos own the book if not present)
#add book
#return book
#handle dictonary (book-nameperson)

class library:
    
    def __init__(self,*list_of_books):
        self.list_of_books=list(list_of_books)

    #Display book of list
    def Displaybook(self):
        print("Libarary Book List")
        for book in self.list_of_books:            
            print(f"{book}",end=" || ")
        print("\n")
            

#inherit to baseclass  
class Donate(library):
    donate_detail={}
    def __init__(self,*list_of_books,**donate_details):
        self.donate_detail=donate_details       
        super().__init__(*list_of_books)

    #Add book in list
    def Addbook(self):
        print("\nDonate Book")
        print("Welcome to library for Donating book")
        donater_name=input("Enter your Name : ")
        donater_name=donater_name.capitalize()
        donate_book=input("Enter the Book name : ")
        donate_book=donate_book.capitalize()
        self.donate_detail[donate_book]=donater_name      
        self.list_of_books.append(donate_book) 
        print("Thanks,Book Donate Sucussfully\n")   

    #Add book details
    def donatebookdtail(self):
        print("Detail who's Donate Book\n")
        if not self.donate_detail:
            print("Not Details\n")
        else:    
            for Keyss,valuess in self.donate_detail.items():
                print(f"This Book: {Keyss} Donate {valuess}\n")

#Inherit to upperclass
class Rent(Donate):
    Rent_book={}
    def __init__(self, *list_of_books, **Rent_books):
        self.Rent_book=Rent_books
        super().__init__(*list_of_books, **Rent_books)

    #Rent Book remove in list and add in dict
    def Lendbook(self):
        print("\nRent Any Books ")
        user_name=input("Enter Your Name: ")
        user_name=user_name.capitalize()
        user_lend=input("Which book you want to Rent: ")
        user_lend=user_lend.capitalize()
        if user_lend in self.list_of_books:
            self.list_of_books.remove(user_lend)
            self.Rent_book[user_lend]=user_name   
            print("Thanks! You Rent this book\n")
        elif user_lend not in self.list_of_books and user_lend in self.Rent_book.keys():
            print("Already Rent choose Another Book\n")
        else:
            print("This book not avable in our library\n")  

    #Return book add in list and remove in dict
    def Returnbook(self):
        print("\nReturn Book")
        user_return=input("Enter Return Book Name: ")
        user_return=user_return.capitalize()
        if user_return in self.Rent_book.keys():  
            self.list_of_books.append(user_return)
            self.Rent_book.pop(user_return)
            print("Return Book Sucessfuuly!\n") 
        else:
            print("Sorry, no such book is issued yet\n")

    #Display Rent book detail
    def Lendbookdeatail(self):
        print("Detail Who's Rented the Book\n")
        if not self.Rent_book:
            print("Not Details\n")
        else:    
            for Keyss,valuss in self.Rent_book.items():
                print(f"This Book: {Keyss} rent to {valuss}\n")  

                    

bookslist=Rent("Python","C++","C","Java","Javascript","Html")
    

def main():
    dis=["Displaybook","Donatebook","Donatedetail","Rentbook","Rentdetail","Returnbook","Exit"]
    while True:
    
        for i in dis:
            print(i,end=" || ")
    
        user_main=input("\nEnter select option: ")        
        user_main=user_main.capitalize()
        if user_main=="Donatebook":
            bookslist.Addbook()
        elif user_main=="Donatedetail":
            bookslist.donatebookdtail()
        elif user_main=="Displaybook":
            bookslist.Displaybook()
        elif user_main=="Rentbook":
            bookslist.Lendbook()    
        elif user_main=="Rentdetail":
            bookslist.Lendbookdeatail()
        elif user_main=="Returnbook":
            bookslist.Returnbook() 
        elif user_main=="Exit":
            break

if __name__=="__main__":        
    main() 
                