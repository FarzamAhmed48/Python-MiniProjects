# class twoDVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f"The vector sum for 2d Vectors {self.i}i + {self.j}j")

# class threeDVector(twoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
    
#     def show(self):
#         print(f"The vector sum for 3d Vectors {self.i}i + {self.j}j + {self.k}k")
# a=twoDVector(1,2)
# a.show()
# b=threeDVector(3,4,5)
# b.show()



class Employee:
    salary=234
    increment=40

    @property
    def salaryAfterIncrement(self):
        return (self.salary +self.salary *(self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,value):
        self.increment=((value/self.salary)-1)*100

e=Employee()
e.salaryAfterIncrement=280
print(e.increment)