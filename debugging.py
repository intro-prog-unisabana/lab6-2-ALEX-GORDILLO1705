def show_inventory(inventory):
    print("\nCurrent Inventory:")
    for fruit, stock in inventory.items():   # ✅ corregido
        print(f"{fruit}: {stock}")
    print()

def add_fruit(inventory):
    fruit = input("Enter the name of the new fruit: ").strip()
    if fruit in inventory:   # ✅ simplificado
        print(f"{fruit} already exists!\n")
    else:
        stock = input(f"Enter stock for {fruit}: ")
        inventory[fruit] = int(stock)   # ✅ corregido (era ==)
        print(f"{fruit} added with stock {stock}.\n")

def update_stock(inventory):
    fruit = input("Enter the name of the fruit to update: ").strip()
    if fruit in inventory:   # ✅ corregido (no .items())
        amount = int(input(f"Enter amount to add to {fruit}'s stock: "))  # ✅ convertir a int
        inventory[fruit] += amount   # ✅ ahora sí funciona
        print(f"{fruit} stock increased by {amount}.\n")
    else:
        print(f"{fruit} is not in inventory. Use option 2 to add it.\n")

def menu():
    print("Options:")
    print("1 - View inventory")
    print("2 - Add new fruit")
    print("3 - Update existing fruit stock")
    print("4 - Exit")

def run_program():
    inventory = {   # ✅ corregido (faltaban comas)
        "apples": 10,
        "bananas": 20,
        "oranges": 15
    }

    print("Welcome to the Fruit Shop!")

    while True:
        menu()
        choice = input("Enter option number: ")

        if choice == "1":
            show_inventory(inventory)
        elif choice == "2":
            add_fruit(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")
    # FREEZE CODE END
