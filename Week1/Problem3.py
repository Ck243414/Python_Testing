# String Practice

# String slicing
name = "Chaitanya"
temp = name[0:4] # starting index to end index -1
temp1 = name[-5:-1] # negative-slicing
temp2 = name[-5:] # negative-slicing till end 
length = len(name)
print(temp)
print(temp1)
print(temp2)
print(name)
print(length)

# String skipping
temp4 = name[1:6:2] # take string from 1 to 6-1 and every 2 
print(temp4) # cHaItAnya" ->hia o/p
print(name.startswith("Cha"))
print(name.endswith("ay"))
print(name.capitalize()) #capitalizes only the first letter of the first word
print(name.count("a"))
print(name.find("t"))

text = "hello how are you hello ?"
text1 = text.replace("hello","bye")
print(text1)

# \n newline
# \t Tab 
# \" read as double quote in the string 

# two ways of doing same thing -> string and fstring
user = input("Enter name of the user ")
print("Good Morning",user)
print(f"Good Morning {user}")

# String Chaining 
text1 = '''Hello how are you 
i am fine 
how are you
good afternoon'''

print(text1.replace("how","what").replace("are","were").replace("you","we"))
#content in text1 was not changed as strings are immutable
