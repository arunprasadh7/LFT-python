# 3 File handling

with open('myfile.txt') as file:
    print(file.read())

print(file.closed)  # returns bool value

# writing in a file

text = 'This text will be written inside the file. Any old file data will be deleted.'
with open('myfile2.txt', 'w') as f:
    f.write(text)

# appending a file - new text will be appended to the end and existing text will be unaltered

newtxt = 'This is newly added text and will be added to the end of the existing text. Previous file data is unaltered.'
with open('myfile3.txt', 'a') as f3:
    f3.write(newtxt)


# assignment

# 1 reading the file
with open('assignmentfile.txt') as ass:
    text = ass.read()
    print(text)

# 2 Replacing cows with duck and moo with quack
ntxt = """Old MacDonald had a farm
ee i ee i o
And on his farm he had some duck
Ee i ee i oh
With a quack-quack here
And a quack-quack there
Here a quack, there a quack
Everywhere a quack-quack"""

#	string functions to replace words in text
duck = text.replace('cow','duck')
# print(duck)
quack = duck.replace('moo','quack')
# print(quack)

#appending the altered text
with open('assignmentfile.txt','a') as af:
	af.write(quack)