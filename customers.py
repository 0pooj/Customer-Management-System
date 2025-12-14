import json

CUSTOMERS_FILE = 'customers.json'
customers = []

def load_customers():
    global customers
    try:
        with open(CUSTOMERS_FILE, 'r') as f:
            customers = json.load(f)
        print(f"✅ Loaded {len(customers)} customers from file.")
    except FileNotFoundError:
        print("ℹ️ Customer data file not found. Starting with an empty list.")
    except json.JSONDecodeError:
        print("❌ Error reading data from file. Starting with an empty list.")

def save_customers():
    with open(CUSTOMERS_FILE, 'w') as f:
        json.dump(customers, f, indent=4)
    print("💾 Customer data saved to file.")

def show_menu():
    print("\n--- Customer Management System ---")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Search Customer")
    print("4. Delete Customer")
    print("5. Exit and Save")

def add_customer():
    global customers
    
    name = input("Customer Name: ")
    phone = input("Phone Number: ")
    email = input("Email Address: ")

    customer = {
        "name": name,
        "phone": phone,
        "email": email
    }

    customers.append(customer)
    print("✅ Customer added successfully")

def show_customers():
    if not customers:
        print("❌ No customers found")
        return

    print("\n📋 Customer List:")
    for index, customer in enumerate(customers, start=1):
        print(f"{index}. Name: {customer['name']}, Phone: {customer['phone']}, Email: {customer['email']}")

def search_customer():
    search_name = input("Enter customer name to search: ")

    found = False
    for customer in customers:
        if customer["name"] == search_name:
            print("✅ Customer found:")
            print(f"Name: {customer['name']}, Phone: {customer['phone']}, Email: {customer['email']}")
            found = True

    if not found:
        print("❌ Customer not found")

def delete_customer():
    global customers
    
    if not customers:
        print("❌ No customers to delete")
        return

    search_name = input("Enter customer name to delete: ")

    initial_count = len(customers)
    
    customers = [customer for customer in customers if customer["name"] != search_name] 

    if len(customers) < initial_count:
        print(f"✅ Customer {search_name} deleted successfully")
    else:
        print("❌ Customer not found")

load_customers() 

while True:
    show_menu()
    choice = input("Select a number: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        show_customers()
    elif choice == "3":
        search_customer()
    elif choice == "4":
        delete_customer()
    elif choice == "5":
        save_customers()
        print("👋 Exiting the program")
        break
    else:
        print("❌ Invalid choice")
