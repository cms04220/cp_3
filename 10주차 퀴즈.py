import random

results = []
while len(results) < 6:
   number = random.randint(1,45)
   if number in results:
       print("results 안에 number이 있으므로, results를 제거하고 출력했습니다.")
   else:
       results.append(number)


print("생성된 로또 번호는",(results),"입니다.")