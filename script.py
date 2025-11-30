# Import packages
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod 

class Mining(ABC):
    def __init__(self, name): 
        self.name = name
    @abstractmethod
    def tax_rate(self): 
        pass

class Employee(Mining):
    def __init__(self, name, salary, signing_bonus, status, position):
        super().__init__(name)
        if salary < 0:
            raise ValueError("Can't go below zero.")
        else:
            self.salary = salary
        self.status = status
        self.position = position
        self.signing_bonus = signing_bonus
    def monthly_salary(self):
        return self.salary/12
    def getsalary(self):
        if hasattr(self, "_raise"):
            return self.salary + (self.salary * self._raise)
        else:
            return self.salary
    def setraisepercentage(self, amount):
        self._raise = amount
    def tax_rate(self):
        return self.salary * 0.25

Bob_Jones = Employee("Bob Jones", 50000, 500, "Full_Time", "Associate")
print("Name:", Bob_Jones.name)
print("Position:", Bob_Jones.position)
print("Salary:", Bob_Jones.salary)
print("Monthly salary:", Bob_Jones.monthly_salary())
print("Tax:", Bob_Jones.tax_rate())
Bob_Jones.setraisepercentage(0.10) # 10% raise
print("Bob's raise:", Bob_Jones.getsalary())

class Client(Mining):
    minimum = 300
    def __init__(self, name, surcharge):
        super().__init__(name)
        if surcharge < 0:
            raise ValueError("Can't go below zero.")
        else:
            self.surcharge = surcharge
    def total(self):
        return self.surcharge + Client.minimum
    def tax_rate(self):
        return self.surcharge * 0.13

Mike_Wallace = Client('Mike Wallace', 500)
print("Name:", Mike_Wallace.name)
print("Minimum payment:", Mike_Wallace.minimum)
print("Payment:", Mike_Wallace.surcharge)
print("Tax:", Mike_Wallace.tax_rate())
print("Total:", Mike_Wallace.total())

class Materials:    
    def __init__(self, type, price):        
        self.type = type
        if price < 0:
            raise ValueError("Can't go below zero.")
        else:
            self.price = price
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    def setdiscount(self, amount):
        self._discount = amount 
    def __repr__(self):
        material_type_repr = """
        Material:
            Type: {type}
            Price: {price}
        """.format(type = self.type, \
                   price = self.price)
        return material_type_repr

Gold = Materials("Gold", 7.54)
Silver = Materials("Silver", 3.82)
Diamond = Materials("Diamond", 4.50)
Ruby = Materials("Ruby", 3.20)

print(Gold) 
print(Gold.type) 
print(Gold.getprice()) 

Silver.setdiscount(0.25)
print(Silver.getprice())

class Manufacturing:
    Manufacturing_type = ("Aesthetic", "Energy")
    __manufacturing_list = None
    @classmethod
    def getmanufacturingtypes(cls):
        return cls.Manufacturing_type
    def setTitle(self, newtitle):
        self.title = newtitle
    def __init__(self, title, type):
        self.title = title
        if (not type in Manufacturing.Manufacturing_type):
            raise ValueError(f"{type} is not a valid manufacturing type") 
        else:
            self.type = type
    @staticmethod
    def getmanufacturinglist():
        if Manufacturing.__manufacturing_list == None:
            Manufacturing.__manufacturing_list = []
        return Manufacturing.__manufacturing_list

print("Manufacturing types: ", Manufacturing.getmanufacturingtypes())
m1 = Manufacturing("Title 1", "Aesthetic")
m2 = Manufacturing("Title 1", "Energy")
Manu = Manufacturing.getmanufacturinglist()
Manu.append(m1)
Manu.append(m2)
print(Manu)

class Utility:
    def __init__(self, cost):
        if cost < 0:
            raise ValueError("Can't go below zero.")
        else:
            self.cost = cost
    def tax_rate(self):
        return self.cost * 0.13

utility_prices = {
    "Electricity": 40,
    "Hydro": 20,
    "Internet": 10
}

Lights = Utility(utility_prices["Electricity"])
print("Lights", Lights.cost)
print("Tax:", Lights.tax_rate())

class Operation:
    def __init__(self, quantity):
        if quantity < 0:
            raise ValueError("Can't go below zero.")
        else:
            self.quantity = quantity

class Diamond_Operation(Operation):
    def __init__(self, quantity, ID):
        super().__init__(quantity)
        self.ID = ID

diamond = 0

while diamond == 0:
    print("digging...")
    diamond = np.random.randint(0, 2)

diamond = Diamond_Operation(np.random.randint(1, 8), "001")
print("Found", diamond.quantity, "Diamond!")
print("ID:", diamond.ID)

class Gold_Operation(Operation):
    def __init__(self, quantity, shine): # Shine is rated from 1 to 10
        super().__init__(quantity)
        if shine < 0 or shine > 10:
            raise ValueError("Can't get past the ratings limit.")
        else:
            self.shine = shine
    def __ge__(self, standard):
        print("__ge__() is called, if it's within or above standard value")
        return (self.quantity >= standard.quantity) and \
                (self.shine >= standard.shine)

week = [0]
for x in range(7):
    mined = week[-1]
    obtain = np.random.randint(0, 2)

    if obtain == 1:
        mined = mined + 1
    else:
        mined = mined

    week.append(mined)


gold = Gold_Operation(week[-1], 3)
print("Amount of gold mined this week:", gold.quantity)

gold1 = Gold_Operation(35,3)
standard_value = Gold_Operation(22,2)
print(gold1 >= standard_value)

plt.plot(week)
plt.xlabel("Day")
plt.ylabel("Amount")
plt.title("Amount of gold mined this week")
plt.show()
