import admin
import client
import pprint


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



print("\nWelcome to your favourite bookstore! We are pleased to see you here!\n")

total_price = 0
shipping_price = 0
shipping = 0
 #if list empty, say that there are no books
#add books list, print added books, print removed books, maybe create fucntions?
#book name, author, year, price, quantity, for admin, print list of books, see quantity, etc

#---------------- Main Menu ----------------------#


client_or_admin = input("Are you a client or an admin? ").lower()




#---------- Admin Menu -----------#


if client_or_admin == "admin":  
    
    exit_admin = False 
    
    while not exit_admin: #while loop used to continue or exit 
     
        print("\t\t\t******     1. Add Books               ******")
        print("\t\t\t******     2. Remove Books            ******")
        print("\t\t\t******     3. List Books              ******")
        print("\t\t\t******     4. See Bookstore Profits   ******")

        option1_admin = input()
        should_continue = ""
    
        admin.admin_menu(option1_admin)
        
        should_continue = input("Want to continue or exit? ").lower()
            
    if should_continue == "continue":
        admin.admin_menu(option1_admin)
            
    else:
        exit_admin = True
        print("Thank you!")
        

#----------- Client Menu ---------#


elif client_or_admin == "client":
    print("\t\t\t******     1. Browse Books        ******")
    print("\t\t\t******     2. Buy Books           ******")
    print("\t\t\t******     3. See Total           ******")
    
    option1_client = input()
    
    if option1_client == "1":
        
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
  