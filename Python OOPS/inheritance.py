 ### tAsk no 1
 
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print("Name",self.name)
        print("Age",self.age)
        
class Student(person):
    def __init__(self,name,age, grade):
        self.grade=grade
        super().__init__(name,age)
    def display(self):
            super().display()
            print("grade",self.grade)

S1=Student("Nadia",19,"A")
S1.display()