# Encapsulation
# Public members / Public Access Modifier
class developer:
    def __init__(self , name , age):
        self.developername=name
        self.developerage = age
    def displayage(self):
        print("age: " , self.developerage) #age : 20
obj= developer("ujjwal" , 20)
print("name: " , obj.developername) #name:ujjwal
obj.displayage()  

# Protected members/ Protected Access Modifier
class student:
    _name= "ujjwal"
    _roll = 98
    _branch = "head"
    def __init__(self , name , roll, branch):
        self.name= name
        self.roll = roll
        self .branch = branch
    def _displayrollandbranch(self):
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)
class developer:
    def __init__(self, name, roll, branch):
        student.__init__(self, name, roll, branch)
    def displayDetails(self):
        print("Name: ", self._name)
        self._displayrollandbranch()
obj = developer("ujjwal" , 6325, "python programming")
obj.displayDetails()
