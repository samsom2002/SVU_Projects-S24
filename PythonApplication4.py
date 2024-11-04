def calculate_final_bill(local_sms, international_sms, local_call_time, international_call_time):
    # Calculate local SMS cost
    if local_sms <= 5:
        local_sms_cost = local_sms * 50
    else:
        local_sms_cost = 5 * 50 + (local_sms - 5) * 35

    # Calculate international SMS cost
    international_sms_cost = international_sms * 100

    # Calculate local call cost
    if local_call_time <= 5:
        local_call_cost = local_call_time * 30
    elif local_call_time <= 10:
        local_call_cost = 5 * 30
    else:
        local_call_cost = 5 * 30 + (local_call_time - 10) * 25

    # Calculate international call cost
    international_call_cost = international_call_time * 200

    # Calculate total final bill
    final_bill = local_sms_cost + international_sms_cost + local_call_cost + international_call_cost
    return final_bill

def add_customer_data(customers):
    while True:
        # Collect customer data
        name = input("Enter Name: ")
        phone_number = input("Enter Phone Number: ")
        local_sms = int(input("Enter number of local SMS: "))
        international_sms = int(input("Enter number of international SMS: "))
        local_call_time = float(input("Enter time spent on local calls (in minutes): "))
        international_call_time = float(input("Enter time spent on international calls (in minutes): "))

        # Calculate the final bill
        final_bill = calculate_final_bill(local_sms, international_sms, local_call_time, international_call_time)

        # Store customer data in the dictionary
        customers[phone_number] = {
            "Name": name,
            "Local SMS": local_sms,
            "International SMS": international_sms,
            "Local Call Time": local_call_time,
            "International Call Time": international_call_time,
            "Final Bill": final_bill
        }

        # Ask if the user wants to add another customer
        another = input("Do you want to add another customer? (yes/no): ").strip().lower()
        if another != 'yes':
            break

def find_bill_by_phone(customers, phone_number):
    # Find the bill by phone number
    if phone_number in customers:
        return customers[phone_number]["Final Bill"]
    else:
        return "Phone number not found."

def find_highest_bill(customers):
    # Find the phone number with the highest bill
    highest_bill = 0
    highest_bill_phone = None
    for phone_number, data in customers.items():
        if data["Final Bill"] > highest_bill:
            highest_bill = data["Final Bill"]
            highest_bill_phone = phone_number
    return highest_bill_phone, highest_bill

def find_name_with_highest_bill(customers):
    # Find the name with the highest bill
    highest_bill_phone, highest_bill = find_highest_bill(customers)
    if highest_bill_phone:
        return customers[highest_bill_phone]["Name"], highest_bill
    else:
        return None, 0

def sort_customers_by_bill(customers):
    # Sort customers by their final bill in descending order
    sorted_customers = sorted(customers.items(), key=lambda item: item[1]["Final Bill"], reverse=True)
    sorted_names = [data["Name"] for phone, data in sorted_customers]
    return sorted_names

def find_top_three_highest_bills(customers):
    # Find the top three highest bills and sort the names in ascending order
    sorted_customers = sorted(customers.items(), key=lambda item: item[1]["Final Bill"], reverse=True)[:3]
    sorted_names = sorted([data["Name"] for phone, data in sorted_customers])
    return sorted_names

def edit_customer_by_name(customers, name):
    # Edit customer information by name
    for phone_number, data in customers.items():
        if data["Name"].lower() == name.lower():
            print(f"Editing customer: {data['Name']}")
            new_phone_number = input("Enter new Phone Number: ")
            data["Local SMS"] = int(input("Enter new number of local SMS: "))
            data["International SMS"] = int(input("Enter new number of international SMS: "))
            data["Local Call Time"] = float(input("Enter new time spent on local calls (in minutes): "))
            data["International Call Time"] = float(input("Enter new time spent on international calls (in minutes): "))
            data["Final Bill"] = calculate_final_bill(data["Local SMS"], data["International SMS"], data["Local Call Time"], data["International Call Time"])
            
            # Update the dictionary with the new phone number
            customers[new_phone_number] = customers.pop(phone_number)
            print("Customer information updated successfully.")
            return
    print("Customer not found.")

def main():
    customers = {}
    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Add customer data")
        print("2. Find bill by phone number")
        print("3. Find phone number with highest bill")
        print("4. Find name with highest bill")
        print("5. Sort customers by highest bill")
        print("6. Find top three highest bills sorted by name")
        print("7. Edit customer information by name")
        print("8. Exit")
        choice = input("Enter your choice: ")

        # Execute the chosen option
        if choice == '1':
            add_customer_data(customers)
        elif choice == '2':
            phone_number_to_find = input("Enter the phone number to find the bill: ")
            bill = find_bill_by_phone(customers, phone_number_to_find)
            print(f"The final bill for phone number {phone_number_to_find} is: {bill}")
        elif choice == '3':
            highest_bill_phone, highest_bill = find_highest_bill(customers)
            print(f"The phone number with the highest bill is {highest_bill_phone} with a bill of {highest_bill}")
        elif choice == '4':
            name_with_highest_bill, highest_bill_amount = find_name_with_highest_bill(customers)
            print(f"The name with the highest bill is {name_with_highest_bill} with a bill of {highest_bill_amount}")
        elif choice == '5':
            sorted_names = sort_customers_by_bill(customers)
            print("Customers sorted by highest bill:")
            for name in sorted_names:
                print(name)
        elif choice == '6':
            top_three_names = find_top_three_highest_bills(customers)
            print("Top three highest bills sorted by name:")
            for name in top_three_names:
                print(name)
        elif choice == '7':
            name_to_edit = input("Enter the name of the customer to edit: ")
            edit_customer_by_name(customers, name_to_edit)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()