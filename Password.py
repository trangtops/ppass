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
                self.vault.append(UserLogin().new_console(configs))
            case "passcode":

                self.vault.append(Passcode().new_console(configs))
            case _:
                logging.error("invalid item type")
                


    def print_all_items(self):
        total_item = len(self.vault)
        print(self.vault)
        for i in range(total_item):
            print("item #{}".format(i+1))
            print("{}: {}".format(self.vault[i].name, self.vault[i].type))
            print()

    def print_all_name(self):
        total_item = len(self.vault)
        for i in range(total_item):
            print("item #{}: {}".format(i+1, self.vault[i]['name']))
             
    def print_password_console(self):
        self.print_all_items()
        print("select which item: ", end='')
        try:
            print(self.vault[int(input())-1].password)
        except Exception as e:
            logging.debug(e)
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
        save_list = []
        for i in self.vault:
            save_list.append(i.export_json())
            
        with open(self.vault_file_name, 'w') as f:
            json.dump(save_list, f, indent=6)
        
    def load_json(self):
        with open(self.vault_file_name, 'r') as f:
            item_list = json.load(f)
        for i in item_list:
            match i['type']:
                case 'userlogin':
                    self.vault.append(UserLogin().load_item(i))
                case 'passcode':
                    self.vault.append(Passcode().load_item(i))


class Password:
    def __init__(self):
        self.item = {}
        self.password = ''
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

    def export_json(self):
        return self.__dict__
        
    def generate_password(self, configs):
        '''
        try:
            length = int(password_length)
            if length < 1:
                raise
        except:
        
        print("invalid length, use default value")
        '''
        try:
            length = int(configs['length'])
        except Exception as e:
            logging.debug(e)
            logging.error('input password length is invalld')
            raise

        if configs["is_letter"]:
            letters = string.ascii_letters
        if configs["is_digits"]:
            digits = string.digits
        if configs["is_special_chars"]:
            special_chars = string.punctuation
        alphabet = letters + digits + special_chars
          
        for i in range(length):
            self.password += ''.join(secrets.choice(alphabet)) 

class UserLogin(Password):
    def __init__(self):
        super().__init__()
        self.type = "userlogin"

    def new_console(self, configs):
        print("input item name: ", end='')
        self.name = input()
        print("input username: ", end='')
        self.username = input()
        self.generate_password(configs)
        return self
       
    def load_item(self, item):
        self.name = item['name']
        self.username = item['username']
        self.password = item['password']
        return self

class Passcode(Password):
    def __init__(self):
        super().__init__()
        self.type = "passcode"

    def new_console(self, configs):
        print("input item name: ", end='')
        self.name = input()
        self.generate_password(configs)
        return self
    
    def load_item(self, item):
        self.name = item['name']
        self.passowrd = item['password']
        return self



