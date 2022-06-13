class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def pa(self):
        print("Age = " + str(self.age))
    def pn(self):
        print("Name = " + self.name)


a = Student("Sai vishnu", 18)
a.pn()
a.pa()

