# Inventory Management System

inventory = {}


def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: ₹"))
    quantity = int(input("Enter Quantity: "))

    inventory[product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    print("\nProduct added successfully!")


def view_products():
    if not inventory:
        print("\nNo products available.")
        return

    print("\n INVENTORY ")

    for product_id, product in inventory.items():
        print(f"""
Product ID : {product_id}
Name       : {product['name']}
Price      : ₹{product['price']}
Quantity   : {product['quantity']}
-------------------------------""")


def search_product():
    product_id = input("Enter Product ID to search: ")

    if product_id in inventory:
        product = inventory[product_id]

        print("\nProduct Found!")
        print("Product ID :", product_id)
        print("Name       :", product["name"])
        print("Price      : ₹", product["price"])
        print("Quantity   :", product["quantity"])
    else:
        print("\nProduct not found.")


def update_quantity():
    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        quantity = int(input("Enter new quantity: "))
        inventory[product_id]["quantity"] = quantity

        print("\nQuantity updated successfully!")
    else:
        print("\nProduct not found.")


def delete_product():
    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        del inventory[product_id]
        print("\nProduct deleted successfully!")
    else:
        print("\nProduct not found.")


def low_stock():
    found = False

    print("\n LOW STOCK PRODUCTS ")

    for product_id, product in inventory.items():

        if product["quantity"] <= 5:
            print(
                f"{product_id} - {product['name']} "
                f"(Only {product['quantity']} left)"
            )
            found = True

    if not found:
        print("No low-stock products.")


def main():

    while True:

        print("""

      #INVENTORY MANAGEMENT SYSTEM


1. Add Product
2. View Products
3. Search Product
4. Update Quantity
5. Delete Product
6. Low Stock Alert
7. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_quantity()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            low_stock()

        elif choice == "7":
            print("\nThank you for using Inventory Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()