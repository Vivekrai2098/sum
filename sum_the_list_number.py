listy = []
def repeate():
    x = eval(input("enter the value"))
    s = listy.append(x)
    y = input("do you want continude..?")
    if y == "y":
        repeate()
    else:
        print("thanks for using")
repeate()
print(listy,"\n","*"*33)
sum=0
for i in listy:
    sum+=i
print("the total value of your list is:==",sum)