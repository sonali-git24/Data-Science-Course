def check_armstrong(num):
    # Convert number to string to find the number of digits (power)
    num_str = str(num)
    power = len(num_str)
    
    # Calculate the sum of digits raised to the power
    total_sum = sum(int(digit) ** power for digit in num_str)
    
    # Return True if total sum matches the original number
    return total_sum == num

# Take input from the user
try:
    user_input = int(input("Enter an integer to check: "))
    
    if check_armstrong(user_input):
        print(f"{user_input} is an Armstrong number.")
    else:
        print(f"{user_input} is NOT an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")