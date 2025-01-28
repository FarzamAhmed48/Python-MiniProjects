# # print("Hello Wolrd")

# # a=input("Enter 1st Number: ")
# # b=input("Enter 2nd Number: ")
# # print("NUMBER 1: ",a)
# # print("NUMBER 2: ",b)
# # print("SUM: ",int(a) +int(b))


# di = {
#     "my":400,
#     "name":300,
#     "is":200,
#     "python":100
# }
# print(di)
# print(type(di))
# print(di["my"])

# inp=int(input("Enter a number: "))
# for i in range(1,inp+1):
#     # rem=inp%i
#     # print("*",""*rem,end="")
#     # print("*"*(inp-1))
#     if(i==1 or i==inp):
#         print("*"*inp)
#     else:
#         print("*",end="")
#         print(" "*(inp-2),end="")
#         print("*")
#     # print(" " * (inp-i),end="")
#     # print("*"*(i))
#     # print("")



num=int(input("Enter a number: "))
for i in range (10,0):
    print(f"{num} * {i} = {num*i}")