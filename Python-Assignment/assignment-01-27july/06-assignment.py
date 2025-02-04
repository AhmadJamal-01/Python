# **String Splitting and Joining**
#    - **Task:** Given the string `s`, use string methods to:
#      - **Split into a list:** break the string into a list of substrings based on the delimiter `,`.
#      - **Join with spaces:** combine the list of substrings back into a single string, with each element separated by a space.
#      ```python
#      s:str ="apple,banana,cherry,dates"
#      ```
#    - **Expected Output:**
#      ```
#      ["apple", "banana", "cherry", "dates"]
#      apple banana cherry dates

s = "apple,banana,cherry,dates"


split_list = s.split(",")
print(split_list)


joined_string = " ".join(split_list)
print(joined_string)
