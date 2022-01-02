class Person(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
class Employee(Person):
    def isEmployee(self):
        return True
emp = Person("ujjwal") # An Object of Person
print(emp.getName(), emp.isEmployee()) #ujjwal false
emp = Employee("Coursly") # An Object of Employee
print(emp.getName(), emp.isEmployee()) #coursely true

# Subclassing (Calling constructor of parent class)
class Person():
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class Employee( Person ):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idnumber)

a = Employee('ujjwal', 8860548, 5000340, "python basic")
a.display() #8860548

#types of inheritance
# 1.single inheritance
# 2.multiple inheritance
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername) #Father : Father
        print("Mother :", self.mothername)  #Mother : Mother
s1 = Son()
s1.fathername = "Father"
s1.mothername = "Mother"
s1.parents()

# 3. Multilevel Inheritance
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)
class Son(Father):
    def __init__(self,sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
    def print_name(self):
        print('Grandfather name :', self.grandfathername) #Grandfather name : Grandfather1
        print("Father name :", self.fathername) #Father name : Father1
        print("Father name :", self.fathername) #Son name : Son1
        print("Son name :", self.sonname) #Son name : Son1
s1 = Son('Son1', 'Father1', 'Grandfather1')
print(s1.grandfathername)
s1.print_name()

# 4. Hierarchical Inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
object1 = Child1()
object2 = Child2()
object1.func1() #This function is in parent class.
object1.func2() #This function is in child 1.
object2.func1() #his function is in parent class
object2.func3()  #This function is in child 2.


# 5. hybrid inheritance
class School:
    def func1(self):
        print("This function is in school.")
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
# Driver's code
object = Student3()
object.func1() #This function is in school.
object.func2() #This function is in student 1.