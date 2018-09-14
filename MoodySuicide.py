s = sorted(input().split('.')[0], reverse=True)

middle = ""
res = ""
while len(s) > 0:
    n = s.count(s[0])
    if n % 2 == 0:
        wing = s[0] * (n // 2)
        res = wing + res
    else:
        if middle != "": break
        middle = s[0] * n
    s[0:n] = []

if len(s) > 0:
    print("Нет")
else:
    res = res + middle + res[::-1]
    print("Да")
    print(res)