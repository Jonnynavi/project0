import random
import json_logic
from PersonalInfo import PersonalInfo
from Account import Account


def create_a_account():
    print("Please enter the correct information")
    first_name = input("first name: ")
    last_name = input("last name: ")
    age = input("age: ")
    person = PersonalInfo(first_name, last_name, age)
    account_number = json_logic.json_generate_id()
    new_account = Account(account_number,person)
    json_logic.json_create_an_account(new_account)
    print(f"Congrats on opening your new account {first_name} {last_name}. Your account number is {account_number}.")

def deposit():
    id = check_if_id_exist()
    if not id:
        print("Account does not exist")
        return
    
    deposit_amount = int(input("Please Enter the total amount you would like to deposit. \n"))
    json_logic.json_update_balance(id, deposit_amount)

def withdraw():
    id = check_if_id_exist()
    if not id:
        print("Account does not exist")
        return
    
    withdraw_amount = int(input("Please enter the amount you want to withdraw. \n"))
    json_logic.json_update_balance(id,withdraw_amount * -1)

def get_balance():
    id = check_if_id_exist()
    if not id:
        print("Account does not exist")
        return
    
    account = json_logic.json_get_account_info(id)
    print(f"your current balance is ${account['balance']}")

def delete_account():
    id = check_if_id_exist()
    if not id:
        print("Account does not exist")
        return
    
    json_logic.json_delete_account(id)

def modify_account():
    id = check_if_id_exist()
    if not id:
        print("Account does not exist")
        return
    
    print("What would you like to modify?\n")
    options = ["First Name","Last Name", "Age"]
    for x in range(len(options)):
        print(f"{x+1}. {options[x]}")
    print("press any other key to go back to the main menu")

    selection = int(input())
    if selection < 0 or selection > 4:
        return
    
    update = input("what would you like to change it to?\n")
    json_logic.json_update_account(id,options[selection-1],update)
    
def check_if_id_exist():
    id = int(input("please enter your id\n"))
    account = json_logic.json_get_account_info(id)
    if account is None:
        return False
    else:
        return id



            



