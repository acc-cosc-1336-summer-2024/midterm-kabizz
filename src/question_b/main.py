#add import
import question_b

while True:
    try:
        age = int(input('Enter your age: '))
        if age < 0 or age > 125:#Validates ages between 0 and 125
                raise ValueError
        c = question_b.get_person_category(age)
        print('Your age is',age, "You are a(n)" ,c,)
        choice = input("Enter '1' to try again or '2' to Exit: ")
        if choice == '1':
            continue  # Restart the loop to try again
        elif choice == '2':
            print("Exiting...")
            break  # Exit the loop and end the function
        else:
            print("Invalid choice. Please select again.")
    except ValueError:
            print("Invalid input. Please enter a valid age.")
