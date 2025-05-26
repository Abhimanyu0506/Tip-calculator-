def advanced_tip_calculator():
    try:
        print("Welcome to the Advanced Tip Calculator!")

        bill_amount = float(input("Enter the total bill amount (₹): "))
        people_count = int(input("How many people are splitting the bill? "))

        print("\nChoose a tip percentage:")
        print("1. 10%")
        print("2. 12%")
        print("3. 15%")
        print("4. Custom")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            tip_percentage = 10
        elif choice == '2':
            tip_percentage = 12
        elif choice == '3':
            tip_percentage = 15
        elif choice == '4':
            tip_percentage = float(input("Enter your custom tip percentage: "))
        else:
            print("Invalid choice. Defaulting to 10%.")
            tip_percentage = 10

        tip_amount = (tip_percentage / 100) * bill_amount
        total_amount = bill_amount + tip_amount
        amount_per_person = total_amount / people_count

        print("\n------ Bill Summary ------")
        print(f"Total Bill: ₹{bill_amount:.2f}")
        print(f"Tip ({tip_percentage}%): ₹{tip_amount:.2f}")
        print(f"Total Amount (Bill + Tip): ₹{total_amount:.2f}")
        print(f"Each Person Pays: ₹{amount_per_person:.2f}")
        print("--------------------------")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except ZeroDivisionError:
        print("Number of people cannot be zero.")

advanced_tip_calculator()