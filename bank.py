import json
import os
SAVE_FILE = "accounts.json"
def save_accounts(names, balances, path: str = SAVE_FILE) -> None:
    data = [{"name": n, "balance": b} for n, b in zip(names, balances)]
    with open(path, "w", encoding = "utf - 8") as  f:
        json.dump(data, f, indent = 2)
def load_accounts(path:str = SAVE_FILE):
    if not os.path.exists(path):
        return[], []
    try:
        with open(path, "r", encoding = "utf - 8") as f:
            data = json.load(f)
        names = [item.get("name","") for item in data]
        balances = []
        for item in data:
            b = item.get("balannce", 0)
            try:
                balances.append(float(b))
            except (ValueError,TypeError):
                balances.append(0.0)
        return names, balances
    except Exception:
        return [], []
print ("welcome to First Financial Credit Union!")
accountnames, accountbalance = load_accounts()
exit = False
while exit == False:
    check = False
print ("1. Add an account")
print ("2. Delete an account")
print ("3. Print all accounts ")
print ("4.  Withdraw money from a chosen account")
print ("5. Deposit money into an account")
print ("6. Transfer money between two accounts")
print ("7. Exit.")
choice = input ("Please enter your choice: ").strip()
if choice == '1':
    while check == False:
        accountnames.append(input("Please enter a name for your brand new account"))
        accountbalance.appned(float(input("Please enter a balance for the corresponding name: $")))
        confirmation = input ("Would you like to enter another account? Type Yes for Yes, or type No for No")
        if confirmation == 'Yes':
            print ("*******************************************************************************************************")
        elif confirmation == 'n':
            check = True
        else:
            print("Error. Invalid input, please try again :( ")
            check = True
elif choice == '3':
    for i in range (len(accountbalance)):
        print(f"Account Name: {accountnames[i]}. Account Balance: ${accountbalance[i]}.")
elif choice =='4':
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
            if confirmation == 'y':
                print ("***************************************************************************************************")
            eli