# **String Manipulation**

#    - **Task:** Given the string `s`, use string methods to:
#      - **Capitalize the first letter:** make the first character uppercase and the rest of the string lowercase.
#      - **Convert to uppercase:** change all characters in the string to uppercase.
#      - **Convert to lowercase:** change all characters in the string to lowercase.
#      ```python
#      s:str = "hElLo WoRlD"
#      ```
#    - **Expected Output:**
#      ```
#      Hello world
#      HELLO WORLD
#      hello world
#      ```

name = "hElLo WoRlD"

# Capitalize the first letter
capitalized = name.capitalize()
print(capitalized)

# Convert to uppercase
uppercase = name.upper()
print(uppercase)

# Convert to lowercase
lowercase = name.lower()
print(lowercase)