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
print ("welcome to First Financial Credit Union!")
print ("What would you like to do today?")
print ("1. Depositing money into an individual account")
print ("2. Withdrawing money into an individual account")
print ("3. Transfering money between 2 accounts")
print ("4. List all of the accounts and balances")
print ("5. Add a new account")
print ("6. Delete a new account")
print ("Please select the number that corresponds to the action you want to do")
accountnames = []
accountbalances = []
check = False
while check == False:
