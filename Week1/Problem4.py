# Lists and Tuples Revision
# lists are mutable -> can be changed (Basically array)
# list functions change that list whereas in string, after string function executed, new string generated
# tuple is immutable
# tuple slicing
tuple = (1,2,3,4,5)
temp = tuple[1:4]
print(temp)
a,b,c,d,e = tuple #unpacking of a tuple
print(a,b,c,d,e) #cant have no. of variables less than the length of the tuple -> must be equal

L1=[]
while(True):
    f = input("Enter a fruit: ")
    L1.append(f)
    if len(L1) == 5:
        break
print(L1)