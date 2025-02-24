class Employee:
    company = "Folio3"
    def __init__(self):
        print("Constructor of Employee class")
    
class Developer(Employee):
    Salary="200 crore"
    def __init__(self):
        print("Constructor of Developer Class")

class last(Developer):
    name="Farzam Ahmed"
    def __init__(self):
        super().__init__()

    def myself(self):
        print(f"My name is {self.name} and the company where i do work is {self.company} paying me {self.Salary} for my serivces")


func = last()
func.myself()