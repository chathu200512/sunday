def calculate_budget():
    try:
        total_budget = float(input("Enter your total monthly budget: "))
        total_expenses = 0
        
        while True:
            entry = input("Enter an expense amount (or type 'done' to finish): ").lower()
            if entry == 'done':
                break
            
            try:
                expense = float(entry)
                total_expenses += expense
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")

        remaining_balance = total_budget - total_expenses
        
        print("-" * 30)
        print(f"Total Budget: {total_budget:.2f}")
        print(f"Total Expenses: {total_expenses:.2f}")
        print(f"Remaining Balance: {remaining_balance:.2f}")
        print("-" * 30)
        
        if remaining_balance < 0:
            print("Warning: You have exceeded your budget!")
        elif remaining_balance < 500:
            print("Warning: Low Funds")
            
    except ValueError:
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_budget()
