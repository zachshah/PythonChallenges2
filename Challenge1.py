import math
num=input("type an integer: ")
while num.isnumeric==False:
    num=input("type an integer")
variableNum=int(num)
if variableNum==0:
    variableNum=1
totalFactorial=variableNum
while variableNum>1:
    variableNum-=1
    totalFactorial*=variableNum
print(str(num)+" factorial is "+str(totalFactorial))
print("python thinks "+str(num)+"! is "+str(math.factorial(int(num))))
