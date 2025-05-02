#Python Basic Calculator

print("Welcome to the Basic Calculator")
print("You can perform the following operations:")

operator = input("Enter an Operator(+ - * /):")
first_number = float(input("Enter First Number : "))
second_number = float(input("Enter Second Number : "))

if operator == "+" : 
   print("Total Sum is:", first_number + second_number)


elif operator == "-" : 
   print("Total Subtraction is:", first_number - second_number)

elif operator == "*" : 
    print("Total Multiplication is:", first_number * second_number)
    
elif operator == "/" : 
    if second_number == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("Total Division is:", first_number / second_number)

elif operator == "%" : 
    print("Total Modulus is:", first_number % second_number)

else: 
    print(f"Invalid operator: {operator}. Please use +, -, *, /, or %.")
#End of the code