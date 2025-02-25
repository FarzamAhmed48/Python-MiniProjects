class Nummber:
    def __init__(self,n):
        self.n=n
    
    def __add__(self,other):
        print(f"The value of self.n is {self.n}")
        print(f"The value of other.n is {other.n}")

        return Nummber(self.n+other.n)
n=Nummber(1)
m=Nummber(2)
o=Nummber(8)
# resun+m+o)
print((n+m+o).n)