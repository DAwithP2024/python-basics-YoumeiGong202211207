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
    return '@' in email

def display_categories():
    print("\nAvailable Categories:")
    for idx, category in enumerate(products.keys(), 1):
        print(f"{idx}. {category}")

def display_products(products_list):
    print("\nAvailable Products:")
    for idx, (product, price) in enumerate(products_list.items(), 1):
        print(f"{idx}. {product} - ${price:.2f}")

def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list.items(), key=lambda x: x[1], reverse=(sort_order == 2))
    print("\nSorted Products:")
    for idx, (product, price) in enumerate(sorted_products, 1):
        print(f"{idx}. {product} - ${price:.2f}")

def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

def display_cart(cart):
    print("\nYour Cart:")
    for product, quantity in cart:
        print(f"{product} - Quantity: {quantity}")

def generate_receipt(name, email, cart, total_cost, address):
    print("\nReceipt:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Delivery Address: {address}")
    print("Products Purchased:")
    for product, quantity in cart:
        print(f"{product} - Quantity: {quantity}")
    print(f"Total Cost: ${total_cost:.2f}")
    print("Your order will be delivered in 3 days. Payment will be charged after delivery is successful.")

def main():
    # User input for name
    while True:
        name = input("Please enter your full name (first and last): ")
        if validate_name(name):
            break
        else:
            print("Invalid name. Please enter a valid name.")

    # User input for email
    while True:
        email = input("Please enter your email address: ")
        if validate_email(email):
            break
        else:
            print("Invalid email. Please enter a valid email.")

    cart = []
    while True:
        display_categories()
        category_choice = int(input("Select a category by number: "))
        
        if 1 <= category_choice <= len(products):
            selected_category = list(products.keys())[category_choice - 1]
            display_products(products[selected_category])
            while True:
                print("\nOptions:")
                print('''\n1. Select a product to buy
                      2. Sort the products according to the price
                      3. Go back to the category selection
                      4. Finish shoppong''')
                option = int(input("Choose an option: "))

                if option == 1:
                    product_choice = int(input("Select a product by number: "))
                    if 1 <= product_choice <= len(products[selected_category]):
                        selected_product = list(products[selected_category].keys())[product_choice - 1]
                        quantity = int(input("Enter quantity: "))
                        add_to_cart(cart, selected_product, quantity)
                        print(f"Added {quantity} of {selected_product} to cart.")
                    else:
                        print("Invalid product selection.")
                
                elif option == 2:
                    print("Sort by:")
                    print("1. Ascending")
                    print("2. Descending")
                    sort_order = int(input("Choose an option: "))
                    display_sorted_products(products[selected_category], sort_order)
                
                elif option == 3:
                    break  # Go back to category selection
                
                elif option == 4:
                    if cart:
                        display_cart(cart)
                        total_cost = sum(products[selected_category][product] * quantity for product, quantity in cart)
                        address = input("Enter your delivery address: ")
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day!")
                    return  # Exit the main function
                
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid category selection. Please try again.")

if __name__ == "__main__":
    main()
