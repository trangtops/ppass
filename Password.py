import string
import secrets
import json
import logging

class Vault:
    def __init__(self):
        self.vault = []
        self.vault_file_name = 'mpt555'

        self.load_json()
    
    def new_item_console(self, item_type, configs):
        match item_type:
            case "userlogin":
                self.vault.append(UserLogin(configs))
            case "passcode":

                self.vault.append(Passcode(configs))
            case _:
                logging.error("invalid item type")
                


    def print_all_items(self):
        total_item = len(self.vault)
        for i in range(total_item):
            print("item #{}".format(i+1))
            for j in self.vault[i]:
                print("{}: {}".format(j.name, j.type))
                print()

    def print_all_name(self):
        total_item = len(self.vault)
        for i in range(total_item):
            print("item #{}: {}".format(i+1, self.vault[i]['name']))
             
    def print_password_console(self):
        self.print_all_items()
        print("select which item: ", end='')
        try:
            print(self.vault[int(input())-1]['password'])
        except:
            logging.error("invalid item number")

    def delete_item_console(self):
        self.print_all_items()
        print("select which item: ", end='')
        ans = input()
        print("are you sure[y/n]: ", end='')
        is_confirm = input()
        if is_confirm == 'y':
            try:
                del self.vault[int(ans)-1]
            except:
                print('cannot perform item delete')
    
    def renew_password_console(self):
        self.print_all_name()
        print("select which item: ", end='')
        try:
            self.vault[int(input())-1].password = self.generate_password()
        except Exception as e:
            print("cannot update password: {}".format(e)) 

    def save_json(self):
        
        with open(self.vault_file_name, 'w') as f:
            json.dump(self.vault, f, indent=6)
        
    def load_json(self):
        with open(self.vault_file_name, 'r') as f:
            item_list = json.load(f)
        for i in item_list:
            match i['type']:
                case 'userlogin':
                    self.vault.append(UserLogin().load_item(i))

class Password:
    def __init__(self):
        self.item = {}
        self.type = ""
   
    def load_config(config):
        self.letters = ''
        self.digits = ''
        self.special_chars = ''
        self.password = ''
        if configs["is_letter"]:
            self.letters = string.ascii_letters
        if configs["is_digits"]:
            self.digits = string.digits
        if configs["is_special_chars"]:
            self.special_chars = string.punctuation
        self.alphabet = self.letters + self.digits + self.special_chars

        try:
            self.password_length = int(configs["password_length"])
        except Exception as e:
            print("error: {}".format(e))

    def load_item(self):
        pass

    def get_item(self):
        return self

    def generate_password(self):
        '''
        try:
            length = int(password_length)
            if length < 1:
                raise
        except:
        
        print("invalid length, use default value")
        '''
        length = self.password_length

        for i in range(length):
            self.password += ''.join(secrets.choice(self.alphabet)) 
        return self.password

class UserLogin(Password):
    def __init__(self):
        super().__init__(configs)
        self.type = "userlogin"
        self.new_console()

    def new_console(self):
        print("input item name: ", end='')
        self.name = input()
        print("input username: ", end='')
        self.username = input()
        self.password = self.generate_password()
       
    def load_item(self, item):
        self.name = item['name']
        self.username = item['username']
        self.password = item['password']

class Passcode(Password):
    def __init__(self):
        super().__init__(configs)
        self.type = "passcode"
        self.new_console()

    def new_console(self):
        print("input item name: ", end='')
        self.name = input()
        self.password = self.generate_password()
    
    def load_item(self, item):
        self.name = item['name']
        self.passowrd = item['password']



