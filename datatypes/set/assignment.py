# Program to iterate over a Set in python
a = set("computerprogramming")
for val in a:
    print(val)
# Program to find Maximum and Minimum in a Set
def max_min(sets):
	return (max(sets), min(sets))
s = set([8, 1, 24, 1, 5, 3])
print(max_min(s))
# Program to Check if two list have at-least one element common
def common_ele(a,b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set))>0:
        return(True)
    return(False)
a = [3,5,6,7,8]
b = [3,30,22,44,66]
print(common_ele(a,b))
# Program to convert Set to string
s = {'a', 'b', 'c', 'd'}
print(s)
print(type(s))
print(len(s))

s = str(s)
print(s)
print(type(s))
print(len(s))
# Program to convert Set into Tuple and Tuple into Set
s = {1 , 2, 3 ,4}
s = tuple(s)
print(s)
print(type(s))
print(len(s))

s = set(s)
print(s)
print(type(s))
print(len(s))
