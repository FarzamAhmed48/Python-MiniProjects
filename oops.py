# This was an example of a basic python class
# class employee:
#     language ="Js,Python"
#     salary ="7 crore"

# farzam = employee()
# farzam.name="Farzam" #this is example of object/instance attributes
# print(farzam.name)

#This was the example of how to execute proper parameters in a class
class Employee:
    salary= "7 Crore"
    language = "JS and python"

    def getInfo(self):
        print(f"The language of the employee is {self.language} and salary is {self.salary}")

object= Employee()
object.getInfo()