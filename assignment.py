# Show Welcome message
print("WELCOME TO MEST ATM")
print("Please insert your atm card")
# Ask user to insert the card
user_card_name = input("Enter your name>> ") 
user_card_number = int(input("Enter your serial number>> "))
# Ask user to enter their pin
user_pin = 4190
current_balance = 10000.00
initial_deposit = 5000
date = 20_08_2025

def pin_authentication():
    while True:
        pin = int(input("Enter your pin>> "))
        try:
            if pin == user_pin:
                print("Login Successful")
                break
            else:
                print("Authentication Failed")
                
        except ValueError:

            print("Invalid pin - Try again!")
    return pin        
    
pin_authentication()

def withdrawal():
    global current_balance
    amount = float(input("Enter the amount>> ")) 
    if amount <= 0:
        print("invalid input")
        
    if amount <= current_balance:
        current_balance -= amount
        print("withdrawal successful, please take your cash.")
    else:
        print("Insufficient balance")    

def deposit():
    global current_balance
    amount2 = float(input("Enter the amount"))
    if amount2 <= 0:
        print("deposit failed")
    if amount2 <= current_balance:
        current_balance += amount2
        print("deposit successful")
    else:
        print("transaction failed")

# List to store past transactions
transaction_history_list = []

# Function to show transaction history
def show_transaction_history():
    if len(transaction_history_list) > 0:
        print("\n=== Transaction History ===")
        for transaction in transaction_history_list:
            print(transaction)
    else:
        print("No transactions yet.")



# Display options
def choices():
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Transaction History")
    print("5. Exit")
        
    options = input("Choose an option>> ")
    if options == "1":
        print(f"Your balance is Ghs {current_balance}")
    elif options == "2":
       deposit() 
    elif options == "3":
        withdrawal()
    elif options == "4":
        show_transaction_history()
    elif options == "5":
        print("Exit")
    else:
        print("Choose from the options")

#issued receipt for atm transaction
print(f"""{choices}
Amount: {initial_deposit}
Balance: {current_balance}
Date: {date}""")


choices()





