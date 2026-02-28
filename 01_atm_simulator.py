"""
ATM Simulator - Version 2
Level: Mini Project
Concepts: Conditions, Validation, State Handling, Loops
"""




balance = float(input("Enter the initial balance: "))


while True:
    
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter the number for the query: "))



    if choice == 1:
        print("Balance Amount: ",balance)
    
    
    elif choice == 2:
        deposit_amount = float(input("Enter the Amount to Deposit: "))
        if deposit_amount>0:
            print("Amount Deposited Successfully")
            balance += deposit_amount
            print("Total Balance Amount is: ",balance)
        else:
            print("Invalid Deposit Amount")
        
        
    elif choice == 3:
        withdraw_amount = float(input("Enter the amount to be withdrawn: "))
        if withdraw_amount>0 and withdraw_amount<=balance:
            print("Money withdrawn successfully")
            balance = balance-withdraw_amount
            print("Remaining balance amount in your account is: ",balance)
        else:
            print("Insufficient balance")
        
        
        
    elif choice == 4:
        print("Exit successfull")
        break
    
    
    else:
        print("Invalid choice")
        
