import admin

cart = [] #record book added to cart
total_price = 0
total_no_shipping = 0
shipping = 0

def client_menu(option):
    
        if option1 == "1":
            browse_books()
        
        elif option == "2":
            #list books and choose which number to buy, list the details and if buy, remove brom list and print receipt, there is none in inventory, print message
            buy()
            
        elif option1 == "3":
            #return a book to list, print receipt, remove profits
            cart()
        

def browse_books():
    admin.list_books()
    
    
def buy():
    print("Books available for purchase: \n")
    admin.list_books()
    
    want_to_buy = int(input("Please choose the reference number of the book you wish to purchase from the list: "))
    #choose the book according to the reference number and add to cart
    
    
def cart():
    print(f"Your cart: \n{cart}")
    
    complete_purchase = input("Would you like to complete your purchase ('Yes' or 'No')? ").lower()
    
    if complete_purchase == "yes":
        
        name = input("Please write your name and surname: \n")
        address = input("Please write your address: \n")
        
        if total_price >= 60:
            print(f"Your total is {total_no_shipping}, with free shipping")
            
        else:
            total_price = total_no_shipping + shipping
            
            print(f"Your total is {total_price}, and shipping is {shipping}")
            
        print("Thank you for shopping with us!")

    else:
        client_menu(option)
        
    
        
    
