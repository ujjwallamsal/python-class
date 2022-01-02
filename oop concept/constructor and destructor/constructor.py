# Constructors
# types of constructor
# 1. default constructor:
# 2.parameterized constructor:

# default constructor
class SimpleClass:
    def __init__(self):
        self.name = "Hello Object"
    def print_name(self):
        print(self.name)
obj1 = SimpleClass()
obj1.print_name() #hello object

# parameterized constructor
class Addition:
    first = 0
    second = 0
    answer = 0
# parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s
    def display(self):
        print("First number = " + str(self.first)) #First number = 1000
        print("Second number = " + str(self.second)) #Second number = 2000
        print("Addition of two numbers = " + str(self.answer))  #Addition of two numbers = 3000
    def calculate(self):
        self.answer = self.first + self.second
obj = Addition(1000, 2000)
obj.calculate()
obj.display()

# Destructors
class Employee:
    # Initializing
    def __init__(self):
        print('Employee created.') #Employee created.
# Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.') #Destructor called, Employee deleted.
obj = Employee()
del obj 


class Employee:
    # Initializing
    def __init__(self):
        print('Employee created')
# Calling destructor
    def __del__(self):
        print("Destructor called")
    def Create_obj():
        print('Making Object...')
        obj = Employee()
        print('function end...')
        return obj
print('Calling Create_obj() function...')
obj = Create_obj()
del obj
# del obj
# print('Program End...')

