import re

# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email.strip()))

def display_categories():
    print("Select a category:")
    for index, category in enumerate(products.keys()):
        print(f"{index + 1}. {category}")
    try:
        category_index = int(input()) - 1
        if 0 <= category_index < len(products):
            return category_index
    except ValueError:
        return None
    return None

def display_products(products_list):
    print("\nAvailable Products:")
    for idx, (product, price) in enumerate(products_list, 1):
        print(f"{idx}. {product} - ${price:.2f}")

def display_sorted_products(products_list, order):
    return sorted(products_list, key=lambda x: x[1], reverse=(order == "desc"))

def add_to_cart(cart, product, quantity):
    product_name, product_price = product
    cart.append((product_name, product_price, quantity))

def display_cart(cart):
    total_cost = 0
    for item in cart:
        name, price, quantity = item
        total_cost += price * quantity
        print(f"{name} - ${price} x {quantity} = ${price * quantity}")
    print(f"Total cost: ${total_cost:.2f}")

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for item in cart:
        quantity, product_name, price = item[2], item[0], item[1]
        print(f"{quantity} x {product_name} - ${price} = ${price * quantity:.2f}")
    print(f"Total: ${total_cost:.2f}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")

def main():
    while True:
        name = input("Please enter your full name (first and last): ")
        if validate_name(name):
            break
        else:
            print("Invalid name. Please enter a valid name.")

    while True:
        email = input("Please enter your email address: ")
        if validate_email(email):
            break
        else:
            print("Invalid email. Please enter a valid email.")

    cart = []
    total_cost = 0

    while True:
        category_index = display_categories()
        if category_index is not None:
            selected_category = list(products.keys())[category_index]
            products_list = products[selected_category]

            while True:
                display_products(products_list)
                print("\nOptions:")
                print("1. Select a product to buy")
                print("2. Sort the products according to price")
                print("3. Go back to the category selection")
                print("4. Finish shopping")

                option = int(input("Select an option: "))
                
                if option == 1:  # Select a product to buy
                    product_choice = int(input("Enter the product number to buy: "))
                    if 1 <= product_choice <= len(products_list):
                        product_name, product_price = products_list[product_choice - 1]
                        quantity = int(input(f"Enter the quantity for {product_name}: "))
                        add_to_cart(cart, (product_name, product_price), quantity)
                        total_cost += product_price * quantity
                        print(f"{quantity} of {product_name} added to cart.")
                    else:
                        print("Invalid product number. Please try again.")

                elif option == 2:  # Sort products by price
                    sort_order = int(input("Sort by price: 1. Ascending 2. Descending: "))
                    if sort_order == 1:
                        sorted_products = display_sorted_products(products_list, "asc")
                        display_products(sorted_products)
                    elif sort_order == 2:
                        sorted_products = display_sorted_products(products_list, "desc")
                        display_products(sorted_products)
                    else:
                        print("Invalid option. Please try again.")

                elif option == 3:  # Go back to category selection
                    break

                elif option == 4:  # Finish shopping
                    if cart:
                        display_cart(cart)
                        print(f"Total Cost: ${total_cost:.2f}")
                        address = input("Please enter your delivery address: ")
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    return  # Exit the main function

                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid category number. Please try again.")

if __name__ == "__main__":
    main()













