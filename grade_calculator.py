def calculate_grade():
    name = input("Enter student's name: ")
    
    try:
        mark1 = float(input("Enter marks for Subject 1: "))
        mark2 = float(input("Enter marks for Subject 2: "))
        mark3 = float(input("Enter marks for Subject 3: "))
        
        # Check for invalid (negative) marks
        if mark1 < 0 or mark2 < 0 or mark3 < 0:
            print("Invalid marks")
            return

        average = (mark1 + mark2 + mark3) / 3
        print("-" * 30)
        print(f"Name   : {name}")
        print(f"Average: {average:.1f}")

        if average >= 75:
            print("Grade  : A")
        elif average >= 60:
            print("Grade  : B")
        elif average >= 40:
            print("Grade  : C")
        else:
            print("Status : Fail")
        print("-" * 30)
            
    except ValueError:
        print("Error: Please enter valid numerical marks.")

if __name__ == "__main__":
    calculate_grade()
