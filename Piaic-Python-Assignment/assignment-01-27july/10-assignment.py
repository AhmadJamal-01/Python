# **Round floating-point numbers**

#     - **Task:** Given a floating-point number `value`
#       - Round `value` to the nearest integer.
#       - Round `value` to two decimal places.
#       ```python
#       value:float = 12.34567
#       ```
#     - **Expected Output:**
#       ```
#       Rounded to nearest integer: 12
#       Rounded to two decimal places: 12.35


value = 12.34567


rounded_integer = round(value)
print(f"Rounded to nearest integer: {rounded_integer}")

rounded_two_decimals = round(value, 2)
print(f"Rounded to two decimal places: {rounded_two_decimals}")
