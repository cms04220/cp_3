import random

results = []
while len(results) < 6:
   number = random.randint(1,45)
   if number in results:
       print("문장안에 넘머가 있으므로, 문장에 추가하지 않습니다.")
   else:
       results.append(number)


print(results)
