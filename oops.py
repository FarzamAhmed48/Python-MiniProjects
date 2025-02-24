# This was an example of a basic python class
# class employee:
#     language ="Js,Python"
#     salary ="7 crore"

# farzam = employee()
# farzam.name="Farzam" #this is example of object/instance attributes
# print(farzam.name)

#This was the example of how to execute proper parameters in a class
# class Employee:
#     salary= "7 Crore"
#     language = "JS and python"

#     # def getInfo(self):
#     #     print(f"The language of the employee is {self.language} and salary is {self.salary}")
#     #  Above two line code same functionaltiy can be achieved by using @staticmethod decorator ! it tells the code that the function wont receive any paramters

#     @staticmethod
#     def greet():
#         print(f"HEllo User")

# object= Employee()
# # object.getInfo()
# object.greet()



# class Employee:
#     def __init__(self,salary,name,language):
#         self.salary=salary
#         self.name=name
#         self.language=language

# farzam=Employee("7 crore","Farzam Ahmed","JavaScript & Python")
# print(f"My name is {farzam.name} and my salary is {farzam.salary} and the languages i work on are {farzam.language}")


class Calculator:
    def __init__(self,n):
        self.square=n*n
        self.cube=n*n*n
        self.squareRoot=n**1/2
    
    def get_square(self):
        print(f"The square of the given number is {self.square}")

    def get_squareRoot(self):
        print(f"The square root of the given number is {self.squareRoot}")
    
    def get_cube(self):
        print(f"The cube of the given number is {self.cube}")

number=Calculator(4)

number.get_square()
number.get_squareRoot()
number.get_cube()