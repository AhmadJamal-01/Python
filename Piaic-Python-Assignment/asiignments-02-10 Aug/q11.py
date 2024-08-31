# Initialize an empty list
user_list = []

# Continuously ask the user to enter values
while True:
    value = input("Enter a value: ")  # Input is already str by default
    if value == "":
        break  # Stop if the user presses enter without typing anything
    user_list.append(str(value))  # Casting to str

# Print the final list
print("Here's the list:", user_list)
