maxball = 70
n = int(input("nums"))
res = {7:[], 8:[], 9:[], 10:[], 11:[]}
for i in range(n):
    fam, name, cls, ball = input("Введите ваши данные").split()
    cls = int(cls); ball = int(ball)
    res[cls].append(ball)

total = []
for i in range(7,12):
    total = total + res[i]
total.sort(reverse = True)

n25 = len(total) // 4
if total[n25-1] == total[n25]:
    if total[n25] > maxball // 2:
        best = [x for x in total if x >= total[n25]]
    else:
        best = [x for x in total if x > total[n25]]
else:
    best = total[0:n25]
print(best[-1])
for i in range(7,12):
    print(len([x for x in res[i] if x >= best[-1]]), end = " ")

