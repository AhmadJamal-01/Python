def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    # Prompt user for their name and favorite numbers with type casting
    name = input("Enter your name: ")
    num1 = int(input("Enter your first favorite number: "))  # Casting input to int
    num2 = int(input("Enter your second favorite number: "))  # Casting input to int
    num3 = int(input("Enter your third favorite number: "))  # Casting input to int

    # Greet the user
    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    # Store the numbers in a list
    favorite_numbers = [num1, num2, num3]

    # Determine if each number is even or odd and store the results in a list of tuples
    even_odd_list = [(int(num), "even" if int(num) % 2 == 0 else "odd") for num in favorite_numbers]  # Casting to int

    # Print whether each number is even or odd
    for num, even_odd in even_odd_list:
        print(f"The number {num} is {even_odd}.")

    # Create and print tuples containing the number and its square
    for num in favorite_numbers:
        square_tuple = (int(num), int(num) ** 2)  # Casting to int
        print(f"The number {num} and its square: {square_tuple}")

    # Calculate the sum of the numbers with type casting
    total_sum = int(sum(favorite_numbers))  # Casting sum to int
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

    # Check if the sum is a prime number and print a message
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number.")

# Run the program
if __name__ == "__main__":
    main()
