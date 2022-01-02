
# Program to Sort Python Dictionaries by Key or Value
d = {2:90, 6:30, 8:80, 6:60}
for i in sorted(d.keys()):
    print(i , end=" ")
print()
# Program to find sum of all items in a dictionary

def returnsum(dict):
    sum = 0
    for i in dict.values():
        sum = sum + i
        return sum
d = {'a':10, 'b':100,'c':1000}
print("sum :" , returnsum(d))