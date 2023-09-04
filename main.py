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
            3) get password\n \
            exit")
        ans = input()
        match ans:
            case '1':
                print("input password length")
                configs['password_length'] = input()
                print("which input item type")
                print("#userlogin\n#passcode")

                vault.new_item_console(input(), configs)
            case '2':
                vault.print_all_items()
            case '3':
                vault.print_password_console()
            case 'exit':
                vault.save_json()
                break
            case 'exit now':
                break
    print("all items has been saved. Exiting program....")

if __name__ == "__main__":
    main()


