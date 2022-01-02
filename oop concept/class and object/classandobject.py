#  class and object
# defining a class
class car:
    pass

# declaring a object
class car:
    a = "bmw"
    b = "mercedes"
def fun (self):
    print("this is a " , self.a)  #bmw
    print("this is a " , self.b)  #mercedes
obj1=car()
print(obj1.a) #bmw
fun(obj1)

# __init__ method
class person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("hello, my name is ujjwal")
p = person("ujjwal")
p.say_hi()

# class variables and instance variables
class Vehicle:
    vehicle_type = 'Car'
    def __init__(self, company, color):
        self.company = company
        self.color = color
# Objects of Vehicle class
obj1 = Vehicle('BMW', 'Black')
obj2 = Vehicle('Audi', 'White')
print('obj1 details:')
print('obj1 is a', obj1.vehicle_type) #obj1 is a Car
print('Company: ', obj1.company) #Company:  BMW
print('Color: ', obj1.color) #Color:  Black
print('\nobj2 details:')
print('obj2 is a', obj2.vehicle_type)  #obj2 is a Car
print('Company: ', obj2.company) #Company:  Audi
print('Color: ', obj2.color)  #Color:  White
print("\nAccessing class variable using class name") #Accessing class variable using class name
print(Vehicle.vehicle_type) #Car

# Defining instance variable using the normal method
class Vehicle:
    # Class Variable
    vehicle_type = 'Car'
# The init method or constructor
    def __init__(self, company):
        self.company = company
# Adds an instance variable
    def setColor(self, color):
        self.color = color
# Retrieves instance variable
    def getColor(self):
        return self.color
# Driver Code
Obj1 = Vehicle("BMW")
Obj1.setColor("brown")
print(Obj1.getColor()) #brown