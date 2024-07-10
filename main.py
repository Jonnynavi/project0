from Account import Account
from options import *

def main() :

    option_list = ["New Account", "Deposit", "Withdraw","Get Balance", "Close Account", "Modify Account"]
    print("Welcome to Bank of Navi. Please select (1-9) for what you would want to do today")

    while True:

        print("\nMain Menu")
        print("--------------------------------------------------------------------")

        num = 1
        for option in option_list:
            print(f"{num}. {option}")
            num+=1
        print("press any other key to Quit")
        try:
            selection = int(input())
        except ValueError:
            selection = 0
        match selection:
            case 1:
                create_a_account()
            case 2:
                deposit()
            case 3:
                withdraw()
            case 4:
                get_balance()
            case 5:
                delete_account()
            case 6:
                modify_account()
            case 0: 
                break

main()