def dash(input_username):
    while True:
        print("Welcome",input_username,"!!!")
        inp=int(input('''What  would you like to do?
1.     ....
2.     ......
3.     ......'''))
        if inp==1:
            pass
        elif inp==2:
            pass
        elif inp==3:
            pass
        ch=input("Would you like to continue operations? (Y)")
        if ch.lower()!='y':
            break
        else:
            continue
    # Function to read employee accounts from file
def read_employee_accounts():
    employee_accounts = {}
    with open("employee_accounts.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            employee_accounts[username] = password
    return employee_accounts

# Function to write employee accounts to file
def write_employee_accounts(employee_accounts):
    with open("employee_accounts.txt", "w+") as file:
        for username, password in employee_accounts.items():
            file.write(f"{username},{password}\n")

# Function to perform employee login
def login():
    # Read employee accounts from file
    employee_accounts = read_employee_accounts()

    # Get employee input
    global input_username
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    # Check if credentials match
    if input_username in employee_accounts and employee_accounts[input_username] == input_password:
        print("Login successful!")
        employee_dashboard()
    else:
        print("Invalid username or password.")
        return False

# Function to perform employee registration
def register():
    # Read employee accounts from file
    employee_accounts = read_employee_accounts()

    # Get employee input
    new_username = input("Enter a new username: ")
    new_password = input("Enter a new password: ")

    # Check if username already exists
    if new_username in employee_accounts:
        print("Username already exists. Please choose a different username.")
        return

    # Add new employee to accounts
    employee_accounts[new_username] = new_password

    # Write updated employee accounts to file
    write_employee_accounts(employee_accounts)

    print("Registration successful!")
    employee_dashboard()

# Employee dashboard
def employee_dashboard():
    # Check employee login
    dash(input_username)
    # ...

# Main program loop
def main():
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

        print()

        # If login is successful, proceed to the employee dashboard
        if choice == "1":
            employee_dashboard()

if(__name__ == "__main__"):
    main()