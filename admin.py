import pprint

books_list = []
new_book = {}

def admin_menu(option):
    
    if option == "1":
        add_books()  
        books_list.append(new_book)
        
        print("The book was successfuly added!")
        pprint.pprint(books_list)
            
    elif option == "2":
        print()
            
    elif option == "3":
        list_books()
            
    elif option == "4":
        print()


def add_books():
    
    title = input("Title: ")
    author = input("Author: ")
    publication_year = int(input("Publication year: "))
    price = float(input("Price: £"))
    quantity = int(input("Copies being added: "))
    
    
    new_book["Title"] = title
    new_book["Author"] = author
    new_book["Year: "] = publication_year
    new_book["Price"] = price
    new_book["In stock"] = quantity
    


def list_books():
    pprint.pprint(books_list)
    

def remove_copies():
    #remove one copy of the book when a client buys
    print()
    
def remove_books():
    #remove entire book
    
    print(f"The book {books} was successfuly removed")
    
     
def profits():
    print()
    

def updates():
    print()
    


    
    
