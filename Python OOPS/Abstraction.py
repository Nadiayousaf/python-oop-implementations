
from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Child Classes
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class JazzCash(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using JazzCash")


class EasyPaisa(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using EasyPaisa")


# Usage
p1 = CreditCard()
p2 = JazzCash()
p3 = EasyPaisa()

p1.pay(1000)
p2.pay(500)
p3.pay(200)