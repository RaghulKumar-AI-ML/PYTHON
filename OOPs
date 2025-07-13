'''CLASSES AND OBJECTS '''

class Player:
    def __init__(self,name,score): #__init__ method: Initializes the  attributes 
        self.name = name 
        """ self = instance of a class(one obj created by the class),
        where objects calling a method or accesing the variables """

        self.score = score 
    
        print("a new player created")

#creating a object...
p1 = Player('raghul',50)
print(p1.name) 




"""ENCAPSULATION
means keeping the data inside the class so that it cant be accessed directly from outside"""


class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance += amount 
    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
account.deposit(3000)
print(account.get_balance())



""" ABSTRACTION 
abstraction means showing only whats needed  by hiding the complexity ,
{Abstraction means hiding unnecessary details from the user and showing only the relevant parts.}"""



class MakeCoffee:
    def coffee_is_ready(self):
        self.__boil_water()
        self.__pour_coffee_powder()
        self.__add_sugar()
        print("your coffee is ready")
    def __boil_water(self):
        print("boiling the water")
    def __pour_coffee_powder(self):
        print("mix the coffee powder in the heat water ")
    def __add_sugar(self):
        print("finally add sugar and stir well")
    
obj=MakeCoffee()
obj.coffee_is_ready()


""" INHERITANCE  
one class(child) can able to access all the properties  and methods of the another class(parent)
"""

class Animal:
    def eat(self):
        print('eat food')
    def sleep(self):
       print('sleeps peacefulyy')
    
       
    
class Dog(Animal):
    def bark(self):
        print(" bark at strangers")

obj = Dog()
obj.eat()
obj.sleep()
obj.bark()



"""
POLYMORPHISM[one name , many forms]
same method or function name but different behavior depending about the object or context
 “Poly” = many, “morph” = forms


"""       

"""  Types of Polymorphism in Python

1.Method Overriding (Runtime Polymorphism) -- one child class will override due to change in behavior 
"""

class Animal:
    def sound(self):
        print("animal sound...")

class Dog(Animal):
    def sound(self):
        print("wooah")

class Cat(Animal):
    def sound(self):
        print("meowwhh")

dog = Dog()
cat = Cat()

def make_sound(animal):
    animal.sound()

make_sound(dog)  # wooah
make_sound(cat)  # meowwhh


"""2. Method Overloading (Not native in Python)
Same method name with different number of parameters.
[ Python doesn't support real method overloading directly, but we can simulate it.]
"""


class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))       # 5
print(calc.add(5, 10))   # 15
print(calc.add(1, 2, 3)) # 6
