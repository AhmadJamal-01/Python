# **String Stripping and Justifying**

#    - **Task:** Given the string `s`, use string methods to:
#      - **Remove leading/trailing spaces:** remove all leading and trailing whitespace characters from the string.
#      - **Left justify with '\*':** left justify the string within a field of width 20, using `*` as the fill character.
#      - **Right justify with '\*':** right justify the string within a field of width 20, using `*` as the fill character.
#      ```python
#      s:str ="   Python is fun!   "
#      ```
#    - **Expected Output:**
#      ```
#      Python is fun!
#      Python is fun!*****
#      *****Python is fun!

s = "   Python is fun!   "


stripped = s.strip()
print(stripped)

left_justified = stripped.ljust(20, '*')
print(left_justified)

right_justified = stripped.rjust(20, '*')
print(right_justified)
