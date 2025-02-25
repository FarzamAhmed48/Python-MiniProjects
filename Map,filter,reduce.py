from functools import reduce
l=[1,2,3,4,5]

# square=lambda x:x*x
# sqList=map(square,l)
# print(list(sqList))


# def evenNo(n):
#     if(n%2==0):
#         return False
#     return True
# only_odd= filter(evenNo,l)

# print(list(only_odd))

def sum(x,y):
    return x+y
mul=lambda x,y :x*y
listSum=reduce(sum,l)
listMul=reduce(mul,l)
print(listSum)
print(listMul)