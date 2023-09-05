import Password


def main():
    vault = Password.Vault()
    configs = {
        "is_letter": True,
        "is_digits": True,
        "is_special_chars": True,
        "length": 14
        }

    while True:
        print("Please choose item\n \
            1) add new item\n \
            2) list all item\n \
            3) get item\n \
            4) get password\n \
            5) renew password\n \
            6) update item\n \
            7) delete item\n \
            exit")
        ans = input()
        match ans:
            case '1':
                print("input password length")
                configs['length'] = input()
                print("which input item type")
                print("#userlogin\n#passcode")

                vault.new_item_console(input(), configs)
            case '2':
                vault.print_all_name()
            case '3':
                vault.print_item_console() 
            case '4':
                vault.print_password_console()
            case '5':
                vault.renew_password_console(configs)
            case '6':
                vault.update_item_console()
            case '7':
                vault.delete_item_console()
            case 'exit':
                vault.save_json()
                break
            case 'exit now':
                break
    print("all items has been saved. Exiting program....")

if __name__ == "__main__":
    main()


