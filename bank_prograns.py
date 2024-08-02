def show_balance():
    pass

def deposit():
    pass

def widthdraw():
    pass

balance = 0
is_running = True

while is_running:
    print("Banking Programs")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Widthdraw")
    print("4. Exit")

    choice = input("Enter the choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        widthdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Enter Valid value")