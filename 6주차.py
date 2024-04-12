a = int(input("몇 단까지 출력할까요?:"))

for x in range(1,a+1):
    print("------","[",x,"단","]","------")

    for y in range(1,20):
         print(x,"*",y,"=",x*y)
