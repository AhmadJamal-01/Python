# name : str = 'Muhammad Qasim'
# fname : str = "Muhammad Aslam"
# education : str = "Master in Data Science"
# age : int = 30

# card : str = "PIAIC Student Card\nStudent Name: " + name + "\nAge:" + str(age)

# print(card)


name : str = 'Muhammad Qasim'
fname : str = "Muhammad Aslam"
education : str = "Master in Data Science"
age : int = 30


card : str = f"""
PIAIC Student Card
Student Name : {name}
Father's Name: {fname}
Age: {age}
Education : {education}
"""

print(card)