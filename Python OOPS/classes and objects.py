#practice task :
##Task no#01:
class Studentprofilesystem:
    def __init__(self,name,age ):
        self.name=name
        self.age=age
    def show_data(self):
        print("Student_Name",self.name)
        print("Age",self.age)
s1=Studentprofilesystem("nadia",19)
s1.show_data()

#Task 2:
class car_information_system:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def display(self):
        print("Car brand",self.brand)
        print("Car model",self.model)
        print("Car year",self.year)
c1=car_information_system("Toyota","Corolla",2025)
c1.display()

#Task number 3
class EmployeeSalarySystem:
    def __init__(self,name,sallary):
        self.name=name
        self.sallary=sallary
    def display(self):
        return self.sallary*12

e1=EmployeeSalarySystem("Nadia",70000)
annual=e1.display()
print("Annual salary",annual)
        
        
class EmployeeSalarySystem:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def calculate_annual_salary(self):
        return self.salary * 12
    def display(self):
        print("Employee:", self.name)
        print("Annual Salary:", self.calculate_annual_salary())
name = input("Enter employee name: ")
salary = int(input("Enter monthly salary: "))
e1 = EmployeeSalarySystem(name, salary)
e1.display()


# Task 04:
class librarybook:
    def __init__(self, book,available):
        self.book=book
        self.available=available
    def display(self):
        print("Book",self.book)
        print("Availablity: ",self.available)
book=input("Enter the Book Name; ")
available=input("yes/No :")
l1=librarybook(book,available)
l1.display()



#Task 5:
class Atm_Simulation:
    def __init__(self,initialbalance):
        self.initialbalance=initialbalance
    def withdraw_balance(self,amount):
        if amount> self.initialbalance:
            print("Insufficient balance")
        else:
         remainingbalance=self.initialbalance-amount
         print("Withdraw Successfully",remainingbalance)
        
withdraw_amount=int(input("Enter Withdraw balance: "))
initialbalance=int(input("Enter the balance:"))

w1=Atm_Simulation(initialbalance)

w1.withdraw_balance(withdraw_amount)


# Task 6:
class Hospital_patient_System:
    def __init__(self, patientName,Disease,Doctor):
        self.patientName=patientName
        self.Disease=Disease
        self.Doctor=Doctor
    def Store_data(self):
        print(f"{self.patientName}is treated for{self.Disease}by{self.Doctor}")
patientName=input("Enter the patient name:")
Disease=input("Enter the disease")
Doctor=input("Enter the Doctor: ")
h1=Hospital_patient_System(patientName,Disease,Doctor)
h1.store_data()
    
    
## Task 7:
class HospitalPatientSystem:

    def __init__(self, patient_name, disease, doctor):
        self.patient_name = patient_name
        self.disease = disease
        self.doctor = doctor
    def display(self):
        print(f"{self.patient_name} is treated for {self.disease} by {self.doctor}")
patients = []
n = int(input("Enter number of patients: "))
for i in range(n):
    print(f"\nEnter data for patient {i+1}")
    name = input("Enter patient name: ")
    disease = input("Enter disease: ")
    doctor = input("Enter doctor: ")
    #object 
    patient = HospitalPatientSystem(name, disease, doctor)
    patients.append(patient)
print("\n--- Patient Records ---")
for patient in patients:
    #object and method call
    patient.display()
       
       
 
        
### Task number 8:
class user_authentication_system:
    def __init__(self, username, password):
        self.username=username
        self.password=password
    def display(self,loginusername,loginpassword):
     if self.username==loginusername and self.password==loginpassword:
         print("Login Successful!")
     else:
         print("Login failed!")
Username=input("Enter the username: ")
Password=input("enter the password:")

c1=user_authentication_system(Username,Password)

loginusername=input("Enter the username: ")
loginpassword=input("enter the password:")

c1.display(loginusername,loginpassword)

        
        
        
        

### Task number 8:
class user_authentication_system:
    def __init__(self, username, password):
        self.username=username
        self.password=password
    def display(self,loginusername,loginpassword):
     if self.username==loginusername and self.password==loginpassword:
         print("Login Successful!")
     else:
         print("Login failed!")
c1=user_authentication_system("nadia",1234)
loginusername=input("Enter the username: ")
loginpassword=input("enter the password:")

c1.display(loginusername,loginpassword)

#Task 9:

class TextAnalyzer:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        return len(self.text.split())

    def longest_word(self):
        words = self.text.split()
        return max(words, key=len) if words else ""

    def char_count(self):
        return sum(1 for char in self.text if char != " ")

    def vowel_count(self):
        return sum(1 for char in self.text.lower() if char in "aeiou")

    def digit_count(self):
        return sum(1 for char in self.text if char.isdigit())

    def analyze(self):
        print("Total Words:", self.word_count())
        print("Total Characters (no spaces):", self.char_count())
        print("Vowels:", self.vowel_count())
        print("Digits:", self.digit_count())
        print("Longest Word:", self.longest_word())


 #### tASk 10
 
 
class StudentReportCard:
    def __init__(self, student_name, student_marks):
        self.student_name = student_name
        self.student_marks = student_marks

    def total_marks(self):
        return sum(self.student_marks)

    def average_marks(self):
        return self.total_marks() / len(self.student_marks)

    def grade(self):
        avg = self.average_marks()
        if 90 <= avg <= 100:
            return "A"
        elif 75 <= avg < 90:
            return "B"
        elif 50 <= avg < 75:
            return "C"
        else:
            return "F"

    def print_report(self):
        print(f"Student: {self.student_name}")
        print(f"Total Marks: {self.total_marks()}")
        print(f"Average Marks: {self.average_marks():.2f}")
        print(f"Grade: {self.grade()}")
              
name = input("Enter student name: ")
marks = [int(input(f"Enter marks for subject {i}: ")) for i in range(1, 4)]

student1 = StudentReportCard(name, marks)
student1.print_report()
        
        



## Task 11

class Bank_Account_System:
    def __init__(self,name, account_no,balance):
        self.name=name
        self.account_no=account_no
        self.balance=balance
    

    def deposit(self, amount):
     if amount > 0:
        self.balance += amount
        print(f"Deposited: {amount}")
     else:
        print("Deposit amount must be positive")
        
        
    def withdraw_balance(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print(f"Withdraw Successfully,{amount}")
            print(f"remaining balance: {self.balance}")
        else:
            print("Insufficient Balance")
        
    def check_balance(self):
        print(f"Current Balance: {self.balance}")
        return self.balance
    
    
    def print_summary(self):
        print("\n--- Account Summary ---")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_no}")
        print(f"Balance: {self.balance}")
        print("-----------------------\n")

    
name=input("Enter the Name:")
account_no=input("Enter Account number: ")
balance=int(input("Enter balance: "))


account1=Bank_Account_System(name,account_no,balance)
account1.deposit(4000)
account1.withdraw_balance(3000)
account1.check_balance()
account1.print_summary()

