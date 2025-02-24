class Employee:
    a=1

    @classmethod
    def show(self):
        print(f"The name is {self.a}")
    
    @property
    def name (self):
        return f"{self.fName} {self.lName}"
    
    @name.setter
    def name(self,value):
        self.fName=value.split(" ")[0]
        self.lName=value.split(" ")[1]
    
e=Employee()
e.name="Farzam Ahmed"
print(e.name)