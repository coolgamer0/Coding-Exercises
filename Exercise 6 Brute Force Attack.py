correct_password = "12345"

while True: 
    user_input = input("Please enter the password: ")
    
    if user_input == correct_password:
        print("Password accepted! Access granted.")
        break  # Exit the loop if the password is correct
    else:
        print("Incorrect password. Please try again.")
