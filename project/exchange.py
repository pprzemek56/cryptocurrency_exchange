from database.config import conn


def main():
    while True:
        print("1    Print accounts")
        print("2    Register in")
        print("3    Log in")
        print("0    Exit")

        choice = input("Choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Use digital only!")
            pass

        match choice:
            case 1:
                print_accounts()
            case 2:
                register()
            case 3:
                if log_in():
                    while True:
                        print("1    Print account information")
                        print("2    Print transactions")
                        print("3    Add transaction")
                        print("4    Create csv file of transactions")
                        print("5    Print summary")
                        print("0    Back to main manu")

                        choice = input("Choice: ")
                        try:
                            choice = int(choice)
                        except ValueError:
                            print("Use digital only!")
                            pass

                        match choice:
                            case 1:
                                account_info()
                            case 2:
                                account_transaction()
                            case 3:
                                add_transaction()
                            case 4:
                                transactions_to_csv()
                            case 5:
                                summary()
                            case 0:
                                break
                            case 7:
                                pass
                else:
                    print("Log in error")
            case 0:
                print("Goodbye :)")
                return
            case other:
                pass


# Main menu methods

def print_accounts():
    statement = '''select id, description from accounts'''
    with conn.cursor() as cursor:
        cursor.execute(statement)
        accounts = cursor.fetchall()
        for i, account in enumerate(accounts):
            print(f"{i + 1}.")
            print(f"    ID: {account[0]}")
            print(f"    DESCRIPTION: {account[1]}")



def register():
    with conn.cursor() as cursor:
        try:
            description = input("Pass account description: ")
            balance = float(input("Pass starting balance: "))
        except ValueError:
            print("Error while creating account")
            return
        statement = '''insert into accounts (description, balance)
         VALUES (%s, %s)'''
        cursor.execute(statement, (description, balance))

        conn.commit()


def log_in():
    return True


# Logged user methods

def account_info():
    pass


def account_transaction():
    pass


def add_transaction():
    pass


def transactions_to_csv():
    pass


def summary():
    pass


if __name__ == "__main__":
    main()
