class Bun :
    def __init__(self,name, price2):
        self.contents = name
        self.price = price2
        self.total = 0

    def sell(self):
        self.total += self.price
        print(self.contents +"붕어빵이 판매되었습니다.")



cream_bun = Bun("슈크림", 1000)
print(cream_bun.contents)

cream_bun.sell()
cream_bun.sell()
cream_bun.sell()
cream_bun.sell()

print(cream_bun.total)