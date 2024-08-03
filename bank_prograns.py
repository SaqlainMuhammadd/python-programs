
def show_balance():
    print(f"Your Balance is ${balance: .2f}")

def deposit():
    amount = float(input("Enter amount to be deposited :"))

    if amount < 0:
        print("Enter a valid value")
        return 0
    else:
        return amount

def widthdraw():
    amount = float(input("Enter the Widthdraw amount : "))

    if amount > balance:
        print("Insufficient Balance")
    elif amount < 0:
        print("Amount must be greater then 0")
    else:
        return amount

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
        balance += deposit()
    elif choice == '3':
        balance -= widthdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Enter Valid value")