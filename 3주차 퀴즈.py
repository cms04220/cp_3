환율= {"달러": 1320, "엔": 950, "위안": 182}

money= [13, 200, 13]
z = money[0] * 환율["달러"]
x = money[1] * 환율["엔"]
y = money[2] * 환율["위안"]

a = "철수가 가지고 있는 돈의 원화 가치는"
b = (z+x+y)
c = "원 입니다"

print(a, b, c)