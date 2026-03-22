## tAsk 2:
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display_basic_info(self):
        print("Name", self.name)
        print("Age", self.age)
        
class Student(person):
    def __init__(self, name,age,marks,rollno):
        super().__init__(name,age)
        self.marks=marks
        self.rollno=rollno
        
    def total_marks(self):
         return sum(self.marks)
        
    def average_marks(self):
        return self.total_marks()/len(self.marks)
        
    def get_grade(self):
        avg=self.average_marks()
        if avg >=80:
            return "A"
        elif avg >=60:
            return "B"
        elif avg>=40:
            return "C"
        else:
            return ("F")
        
    def is_passed(self):
         return "Failed" if self.get_grade() == "F" else "Passed"
    
    def display(self):
        super().display_basic_info()
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)
        print("Total:", self.total_marks())
        print("Average:", self.average_marks())
        print("Grade:", self.get_grade())
        print("Status:", self.is_passed())



    def table_row(self):
        return f"{self.name:<10} | {self.age:<3} | {self.rollno:<3} | {self.marks} | {self.total_marks():<2} | {self.average_marks():<2.1f} | {self.get_grade():<1} | {self.is_passed():<6}"


# Create objects
student1 = Student("Nadia", 19, [70, 80, 90], 63)
student2 = Student("Ahmad", 12, [80, 90, 95], 50)
student3 = Student("Mansha", 14, [80, 65, 40], 55)

print("Name       | Age | Roll | Marks           | Total | Avg   | Gr | Status")
print("-" * 75)

# Print each student row
print(student1.table_row())
print(student2.table_row())
print(student3.table_row())



''''Student1=Student("Nadia",19,[70,80,90],63)
Student2=Student("Ahmad",12,[80,90,95],50)
Student3=Student("Mansha",14,[80,65,40],55)
Student1.display()
Student2.display()
Student3.display()'''


'''students = [
    Student("Nadia", 19, [70,80,90], 63),
    Student("Ahmad", 12, [80,90,95], 50),
    Student("Mansha", 14, [80,65,40], 55)
]

for s in students:
    s.display()'''

    

        