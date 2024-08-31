def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    name = input("Enter your name: ")
    num1 = int(input("Enter your first favorite number: ")) 
    num2 = int(input("Enter your second favorite number: ")) 
    num3 = int(input("Enter your third favorite number: ")) 

    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    favorite_numbers = [num1, num2, num3]

    #Check number status even or odd
    even_odd_list = [(int(num), "even" if int(num) % 2 == 0 else "odd") for num in favorite_numbers]  # Casting to int

    for num, even_odd in even_odd_list:
        print(f"The number {num} is {even_odd}.")

    #number its square
    for num in favorite_numbers:
        square_tuple = (int(num), int(num) ** 2) 
        print(f"The number {num} and its square: {square_tuple}")

    # Total Number Sum
    total_sum = int(sum(favorite_numbers))
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

    # Check prime number
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number.")

if __name__ == "__main__":
    main()
