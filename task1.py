# Function to calculate the factorial of a given number
def factorial(num):
    # Initialize sum variable to 1 (since factorial of 0 is 1)
    sum = 1

    # Multiply each number from 1 to num to calculate factorial
    for i in range(1, num+1):
        sum = sum * i

    # Create a formatted string with the result
    final_string = "Factorial of " + str(num) + " is : " + str(sum)

    return final_string

# Get user input
inp = int(input("Enter a number: "))

# Call the factorial function and print the result
print(factorial(inp))