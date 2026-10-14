import math
inventory = {}
def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))

    if name in inventory:
        print("Product already exists!")
    else:
        inventory[name] = quantity
        print("Product added successfully.")
def update_quantity():
    name = input("Enter product name: ")

    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[name] = quantity
        if inventory[name] == 0:
            del inventory[name]
            print("Product is sold out and removed.")
        else:
            print("Quantity updated successfully.")
    else:
        print("Product not found.")
def highest_stock():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        product = max(inventory, key=inventory.get)
        quantity = inventory[product]

        print("Product with highest stock:", product)
        print("Quantity:", quantity)
def remove_sold_out():
    sold_out = []

    for product, quantity in inventory.items():
        if quantity == 0:
            sold_out.append(product)

    for product in sold_out:
        del inventory[product]

    if sold_out:
        print("Sold-out products removed.")
    else:
        print("No sold-out products found.")
def total_products():
    print("Total unique products:", len(inventory))
def display_inventory():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("\n--- Inventory ---")
        for product, quantity in inventory.items():
            print(product, ":", quantity)
while True:
    print("\n===== INVENTORY SYSTEM =====")
    print("1. Add New Product")
    print("2. Update Quantity")
    print("3. Display Highest Stock")
    print("4. Remove Sold-Out Products")
    print("5. Display Total Unique Products")
    print("6. Display Inventory")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_product()

    elif choice == 2:
        update_quantity()

    elif choice == 3:
        highest_stock()

    elif choice == 4:
        remove_sold_out()

    elif choice == 5:
        total_products()

    elif choice == 6:
        display_inventory()

    elif choice == 7:
        print("Thank you!")
        break
else:
        print("Invalid choice!")