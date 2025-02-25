class complexVectors:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __add__(self,other):
        return complexVectors(self.x +other.x, self.y+other.y, self.z+other.z)
    
    def __mul__   (self,other):
        return complexVectors(self.x *other.x, self.y*other.y, self.z*other.z)
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"

c1=complexVectors(1,2,3)
c2=complexVectors(4,5,6)
c3=complexVectors(7,8,9)

print("Sum of c1 and c2:", c1 + c2)
print("Multiplication of c1 and c2:", c1 * c2)
print("Sum of c1 and c3:", c1 + c3)
print("Multiplication of c1 and c3:", c1 * c3)