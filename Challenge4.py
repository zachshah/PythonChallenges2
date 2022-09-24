numToEnter=input("Type a number: ")
numList=[]
numAmnt=0
hasAlerted=False
while numToEnter != '' or numAmnt<2:
    if numToEnter.isnumeric()==True:
        numList.append(int(numToEnter))
        numAmnt+=1
    if numAmnt>1 and hasAlerted==False:
        print("You have enough numbers, but feel free to add another(ENTER to stop)")
        hasAlerted=True
    numToEnter=input("Type a number: ")
print(str(numList))
numList.sort()
print(str(numList))
numList.sort(reverse=True)
print(str(numList))
