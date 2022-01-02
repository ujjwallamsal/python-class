class cssstudent:
    stream = "cse"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
a = cssstudent("student1" , 1)
b = cssstudent("student2" , 2)
print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)

print(cssstudent.stream)
print(a.stream)
print(b.stream)
cssstudent.stream="mech"
print(b.stream)
print(a.stream)