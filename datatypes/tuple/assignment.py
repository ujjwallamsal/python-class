# Program to Find the size of a Tuple in Python
tuple1 = (1 , "a" , 2 , "c")
print("the size of tuple is : " , len(tuple1)) 
# the size of tuple is :  4

# Program to find Sum of tuple elements

tuple1 = (2,3,7,1,9)
tuple2 = sum(tuple1)
print(tuple2)
# Program to test if elements inside a tuple are distinct or not
t1 = (1,5,3,6,7,8)
res = len(set(t1))== len(t1)
print("is tuple dustinct?: " + str(res))