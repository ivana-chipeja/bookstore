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


 #if list empty, say that there are no books
#add books list, print added books, print removed books, maybe create fucntions?
#book name, author, year, price, quantity, for admin, print list of books, see quantity, etc

#---------------- Main Menu ----------------------#


client_or_admin = input("Are you a client or an admin? ").lower()
should_continue = ""



#---------- Admin Menu -----------#


if client_or_admin == "admin":  
    
    exit_admin = False 
    
    while not exit_admin: #while loop used to continue or exit 
     
        print("\t\t\t******     1. Add Books               ******")
        print("\t\t\t******     2. Remove Books            ******")
        print("\t\t\t******     3. List Books              ******")
        print("\t\t\t******     4. See Bookstore Profits   ******")

        option1_admin = input()
    
        admin.admin_menu(option1_admin)
        
        should_continue = input("Want to continue or exit? ").lower()
            
    if should_continue == "continue":
        admin.admin_menu(option1_admin)
            
    else:
        exit_admin = True
        print("Thank you!")
        

#----------- Client Menu ---------#


elif client_or_admin == "client":
    
    exit_client = False
    
    while not exit_client:
        
        print("\t\t\t******     Free shipping on orders above £60       ******\n")
        print("\t\t\t******     1. Browse Books        ******")
        print("\t\t\t******     2. Buy Books           ******")
        print("\t\t\t******     3. See cart            ******")
        
        option1_client = input()
    
        client.client_menu(option1_client)
        
        should_continue = input("Want to continue or exit? ").lower()
            
    if should_continue == "continue":
        client.client_menu(option1_client)
            
    else:
        exit_client = True
        print("We hope to see you again!")
        
            
        
    
# --------------  else  -----------------# 


else:
  print("Invalid option!")
  