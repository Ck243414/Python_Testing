# Dictionary Revision
Marks = {
    "CK":100,
    "SS":90,
    "UPS":22,
    "AG":46
}
# print(Marks[0]) Error
print(Marks["CK"]) # Key - Value pairs
# Unordered, mutable, indexed

print(Marks.keys())
print(Marks.items())
print(Marks.values())
Marks.update({"CK":99,"AA":57})
print(Marks)
print(len(Marks))
print(Marks.get("CK")) #null if not found 
print(Marks["CK"]) #error if not found

# Sets -> Elements not repeated
s = {1,2,3,4,5}
D = {} #Empty dictionary 
e = set() # this makes an empty set 
print(type(e)) 
s.add(6)
print(s)
s.add(4)
print(s) # unordered, unindexed, no way to change items in sets, cant contain duplicate values
s.remove(6)
print(s)
s.pop() #Pops random element
s1 = {1,2,3,4}
s2 = {2,4,6}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)

# Important concept
print(1 == 1.0) # Same 

d = {}
a = input("enter something")
b = input("enter something else")
d.update({a:b})

# Lists cant be inside a set 

