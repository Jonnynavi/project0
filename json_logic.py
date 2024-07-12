import json

def json_create_an_account(account):
    with open('accounts.json', 'r+') as file:
        data = json.load(file)
        data['accounts'].append(account)
        file.seek(0)
        file.write(json.dumps(data, default=lambda o: o.__dict__,indent=3))

def json_get_accounts():
    with open('accounts.json', 'r') as file:
        data = json.load(file)
        return data

def json_get_account_info(id):
    with open('accounts.json', 'r') as file:
        data = json.load(file)
        accounts = data['accounts']
        for x in accounts:
            if(x['account_number'] == id):
                return x
            
def json_update_balance(id, balance):
    data = json_get_accounts()
    with open('accounts.json', 'w') as file:
        for account in data['accounts']:
            if account['account_number'] == id:
                account['balance'] +=  int(balance)
                print(f"your new balance is ${account['balance']}\n")

        json.dump(data, file ,indent=3)


def json_delete_account(id):
    data = json_get_accounts()
    with open('accounts.json','w') as file:
        accounts = [x for x in data['accounts'] if int(x['account_number']) != id]
        data['accounts'] = accounts
        json.dump(data, file, indent=3)

def json_update_account(id, option, updated_data):
    data = json_get_accounts()
    with open('accounts.json', 'w') as file:
        for account in data['accounts']:
            if account['account_number'] == id:
                personal_info = account['personal_info']
                match option:
                    case "First Name":
                        personal_info['first_name'] = updated_data
                        print(f"Your first name is now {personal_info['first_name'].title()}.")
                    case "Last Name":
                        personal_info['last_name'] = updated_data
                        print(f"Your last name is now {personal_info['last_name'].title()}.")

                    case "Age":
                        personal_info['age'] = updated_data
                        print(f"Your age is now {personal_info['age'].title()}.")

        json.dump(data, file ,indent=3)
        
def json_generate_id():
    #Im gonna to save all ids in list and get the max and add 1 to it 
    with open('accounts.json', 'r') as file:

        data = json.load(file)
        accounts = data['accounts']
        ids = [x['account_number'] for x in accounts if 'account_number' in x]
        if not ids:
            id = 1
        else:
            id = max(ids) + 1

        return id
    
