class Employee:
    company = "Folio3"
    def __init__(self):
        print("Constructor of Employee class")
    
class Developer(Employee):
    Salary="200 crore"
    def __init__(self):
        pass

class last(Developer):
    name="Farzam Ahmed"
    def myself(self):
        print(f"My name is {self.name} and the company where i do work is {self.company} paying me {self.Salary} for my serivces")


func = last()
func.myself()