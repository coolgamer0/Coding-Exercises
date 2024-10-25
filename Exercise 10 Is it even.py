def check_even_odd(number):
    """Determine if the given number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    user_input = input("Please enter a number: ")
    
    try:
        number = int(user_input)
        
        result = check_even_odd(number)
        
        print(result)
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
