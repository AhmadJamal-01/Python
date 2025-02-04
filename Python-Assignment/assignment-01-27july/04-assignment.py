# **Substring Search**

#    - **Task:** Given the string `s`, use string methods to:
#      - **Find the index of "fox":** get the starting index of the substring "fox". If "fox" is not found, it should return -1.
#      - **Count occurrences of "the":** Use the string's built-in method to count how many times the substring "the" appears in the string.
#      ```python
#      s:str ="the quick brown fox jumps over the lazy dog"
#      ```
#    - **Expected Output:**
#      ```
#      index of 'fox' is 16
#      'the' appears 2 times
    

s = "the quick brown fox jumps over the lazy dog"

index_fox = s.find("fox")
print(f"index of 'fox' is {index_fox}")

count_the = s.count("the")
print(f"'the' appears {count_the} times")



#  Self Practice

# name:str= "Ahmad jamal how are you where you live"

# check_index=name.find("how")
# print(check_index) 

# count_name= name.count("you")
# print(count_name)
