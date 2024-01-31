
print('''
      
                ,   ,        ,   ,
               /////|       /////|
              ///// |      ///// |
             |~~~|  |     |~~~|  |
             |===|  |     |===|  |
             |j  |  |     |j  |  |
             | g |  |     | g |  |
             |  s| /      |  s| /
             |===|/       |===|/
             '---'        '---'
       
''')



print("\tWelcome to your favourite bookstore! We are pleased to see you here!")

total_price = 0
shipping_price = 0
books_to_add = 0
books_to_remove = 0
shipping = 0
address = ""
book_list_name = [" "] #if list empty, say that there are no books
#add books list, print added books, print removed books, maybe create fucntions?
#book name, author, year, price, quantity, for admin, print list of books, see quantity, etc

#---------------- Main Menu ----------------------#


client_or_admin = input("Are you a client or an admin?")

client_or_admin.lower()


#---------- Admin Menu -----------#



if client_or_admin == "admin":    
    print("\t\t\t******     1. Add Books               ******")
    print("\t\t\t******     2. Remove Books            ******")
    print("\t\t\t******     3. List Books              ******")
    print("\t\t\t******     4. See Bookstore Profits   ******")

    option1_admin = input()

    if option1_admin == "1":
        #add books to list, print how many were adde and how many are left in inventory\
        books_to_add = int(input("How many books would you like to add?"))
        
        if books_to_add == 0:
            print("No books to add!")
        
        elif books_to_add > 0:
            print(f"You would like to add {books_to_add}")
            
            
            for books in range(0, books_to_add):
                print()
                 
        else:
            print("Invalid choice!")
        
        

#----------- Client Menu ---------#


elif client_or_admin == "client":
    print("\t\t\t******     1. Browse Books        ******")
    print("\t\t\t******     2. Buy Books           ******")
    print("\t\t\t******     3. Return a Book       ******")
    
    option1_client = input()
    
    if option1_client == "1":
        #list books
        print()
    
    elif option1_client == "2":
        #list books and choose which number to buy, list the details and if buy, remove brom list and print receipt, there is none in inventory, print message
        print()
        
    elif option1_client == "3":
        #return a book to list, print receipt, remove profits
        print()
    
    else:
        print("Invalid option")
        
        
    
# --------------  else  -----------------# 


else:
    print("Invalid option!")