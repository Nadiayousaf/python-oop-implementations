class Bank_Account_System:
    def __init__(self,name, account_no,balance):
        self.__name=name
        self.__account_no=account_no
        self.__balance=balance
        
        
        # Getter for name
    def get_name(self):
        return self.__name

    # Getter for account number
    def get_account_no(self):
        return self.__account_no

        
    def deposit(self, amount):
     if amount > 0:
        self.__balance += amount
        print(f"Deposited: {amount}")
     else:
        print("Deposit amount must be positive")
        
        
    def withdraw_balance(self,amount):
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            print(f"Withdraw Successfully,{amount}")
            print(f"remaining balance: {self.__balance}")
        else:
            print("Insufficient Balance")
        
    def check_balance(self):
        print(f"Current Balance: {self.__balance}")
        return self.__balance
    
    
    def print_summary(self):
        print("\n--- Account Summary ---")
        print(f"Account Holder: {self.get_name()}")
        print(f"Account Number: {self.get_account_no()}")
        print(f"Balance: {self.__balance}")
        print("-----------------------\n")

    
name=input("Enter the Name:")
account_no=input("Enter Account number: ")
balance=int(input("Enter balance: "))


account1=Bank_Account_System(name,account_no,balance)
account1.deposit(4000)
account1.withdraw_balance(3000)
account1.check_balance()
account1.print_summary()





