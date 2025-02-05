#mypy for type checking
#mypy filename.py (for error checking)
name: str = 'Helo Ahmad Jamal'
print(name)

#if you want use ' in chracter then you use around "
message:str = "PIAIC Student Card \nFather's Name"
print(message)

#convert any special chracter in simple chracter, place\ before chracter
messages:str='Piaic Student Card\n father\'s Name'

names:str = "Ahmad Jamal"
fname:str = "Afzaal Hussain"
education:str ="Master in Data Science"
age:int = 30

card:str ="Piaic Student Card\n Student Name:" + names
print(card) 

#Define Multiline String """ """ """"

# cards:str = """
# Piaic Student Card
# Student Name : {name}
# Father's Name: {fname}
# Age: {age}
# Education : {education}
# """
# print (cards)


