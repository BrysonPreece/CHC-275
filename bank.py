#This code was made by James Neff and Bryson Preece
import json
import os
SAVE_FILE = "accounts.json"
def save_accounts(names, balances, path: str = SAVE_FILE) -> None: # Used to save account names and balances to a .json file
    data = [{"name": n, "balance": b} for n, b in zip(names, balances)]
    with open(path, "w", encoding = "utf - 8") as  f:
        json.dump(data, f, indent = 2)
def load_accounts(path:str = SAVE_FILE): #Used to load account names and balances
    if not os.path.exists(path):
        return[], []
    try:
        with open(path, "r", encoding = "utf - 8") as f:
            data = json.load(f)
        names = [item.get("name","") for item in data] # Ensure balances are floats when loading
        balances = []
        for item in data:
            b = item.get("balannce", 0)
            try:
                balances.append(float(b))
            except (ValueError,TypeError):
                balances.append(0.0)
        return names, balances
    except Exception: #If your file is corrupt or it is unreadablle, you can start fresh
        return [], []
print ("welcome to First Financial Credit Union!") 
accountnames, accountbalance = load_accounts() # Used to load the accounts immediately after you start the program.
exit = False
while exit == False: # This while loop is used to keep the entire program running indefinately unless exit is True
    check = False
    print ("1. Add an account")
    print ("2. Delete an account")
    print ("3. Print all accounts ")
    print ("4.  Withdraw money from a chosen account")
    print ("5. Deposit money into an account")
    print ("6. Transfer money between two accounts")
    print ("7. Exit.")
    choice = input ("Please enter your choice: ").strip()
    if choice == '1': #This if-statement is used to take in a name and its balance which is saved into the lists corresponding to each, then it is automatically saved to a .json file. Allows user to add multiple at a time
        while check == False:
            accountnames.append(input("Please enter a name for your brand new account"))
            accountbalance.append(float(input("Please enter a balance for the corresponding name: $")))
            confirmation = input ("Would you like to enter another account? Type Yes for Yes, or type No for No")
            if confirmation == 'Yes':
                    print ("***************************************************************************************************")
            elif confirmation == 'No':
                check = True
            else:
                print("Error. Invalid input, please try again :( ")
                check = True
    elif choice == '2': #Used to remove an account by taking the name of the account that you added and removing it. Simple as Vanilla.
        while check == False:
            name = input("Please enter the name of the account to remove").strip()
            try:
                idx = accountnames.index(name)
            except ValueError:
                print ("No account found with that name")
            else:
                removedname = accountnames.pop(idx)
                removedbalance = accountbalance.pop(idx)
                print(f"Removed account '{removedname}' with balance ${removedbalance}.")
                confirmation = input("Remove another account (Yes or No)").strip().lower
                if confirmation == 'Yes':
                    print ("***************************************************************************************************")
                elif confirmation == 'No':
                    check = True
                else:
                    print ("Invalid input. Womp Womp. Try again")
                    chexk = True
    elif choice == '3': #This is used to print out each account name and the corresponding balance
        for i in range (len(accountbalance)): #Prints all accounts in the .json file
            print(f"Account Name: {accountnames[i]}. Account Balance: ${accountbalance[i]}.")
    elif choice =='4': #Used to remove or withdraw money from the account you choose
        while check == False:
            name = input ("Please enter a name of that account to withdraw from").strip()
            try:
                idx = accountnames.index(name)
            except ValueError:
                print ("No account found with that name. Womp Womp :( ")
            else:
                amount = float(amount)
                if amount > 0:
                    accountbalance[idx] -= amount
                    print (f"Withdrew $ {amount} from account '{name}. New balance: ${accountbalance[idx]}.")
                else:
                    print("Invalid amount entered.")
                confirmation = input("Error. Invalid amount entered :( ")
                if confirmation == 'Yes':
                    print ("***************************************************************************************************")
                elif confirmation == 'No':
                    check = True
                else:
                    print("Invalid input, Womp Womp. :(. Please try again.")
                    check = True
    elif choice == '5': #Used to deposit $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ :)
        while check == False:
            name = input("Please enter the name of the account to deposit into Por Favor").strip
            try:
                idx = accountnames.index(name)
            except ValueError:
                print("No account found with that name")
            else:
                try:
                    amount = float(amount)
                except ValueError:
                    print ("Invalid amount entered. Womp Womp. Too bad so sad.")
                else:
                    amount = float(amount)
                    if amount > 0:
                        accountbalance[idx] += amount
                        print (f"Deposited {amount} into account '{name}'. New balance is ${accountbalance[idx]}")
                    else:
                        print("Invalid input. *Cries intensly*. Please try again.")
                confirmation = input("Deposit into another account (Yes or No)?").strip().lower()
                if confirmation == 'Yes':
                    print ("***************************************************************************************************")
                elif confirmation == 'No':
                    check = True
                else: print("Invalid option. Try again.")
                check = True
    elif choice == '6': #Used to transfer $$$$$$ between two accounts. 
        while check == False:
            from_name = input("Please enter the name that you would like to transfer from: ").strip()
            try:
                from_idx = accountnames.index(from_name)
            except ValueError:
                print ("No account found. Womp Womp. Please try again.")
                check = True
            to_name = input ("Please enter the name of the account to transfer to: ").strip()
            try:
                to_idx = accountnames.index(to_name)
            except ValueError:
                print("Invalid amount entered.")
                check = True
            else:
                amount = float(amount)
                if 0 < amount <= accountbalance[from_idx]:
                    accountbalance[from_idx] -= amount
                    accountbalance[to_idx] += amount
                    print(f"Transfered ${amount} from ' {from_name} ' to ' {to_name} ' ")
                    print(f"New balance of ' {from_name} ' : $ {accountbalance[from_idx]}.")
                    print(f"New balance of ' {to_name} ': ${accountbalance[to_idx]}.")
                    print (f"New balance of ' {to_name} ' : ${accountbalance[to_idx]}.")
                else:
                    print ("Invalid amount of money entered or insufficient funds. :(")
                confirmation = input("Transfer between another two accounts (Yes or No?)").strip().lower()
                if confirmation == 'Yes':
                        print ("***************************************************************************************************")
                elif confirmation == 'No':
                    check = True
                else:
                    print("Invalid option. Please try again later.")
    elif choice == '7': #This if-statement is used to save the account names and its balances to a .json file before you exit the program.
        save_accounts(accountnames, accountbalance)
        print (f"Saved {len(accountnames)} account(s) to {SAVE_FILE}.")
        exit = True
    else: #This is used to catch any Invalid Choices when you try and enter an Invalid Option. To that we say Womp Womp!!!!!!
        print ("Invalid choice. Please try again.")
        
    """
    THIS PROGRAM WAS MADE BY JAMES NEFF AND BRYSON PREECE. UNAUTHORIZED USE OF THIS CODE WILL NOT DO ANYTHING WE ARE BROKE :(, HOWEVER, YOU WILL PROBABLY GET DETENTION FOR PLAGERISM.
    """