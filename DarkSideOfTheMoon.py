# На вход программы поступает последовательность из n натуральных целых чисел. Jпределить, можно ли записать все значащие цифры шестнадцатеричной записи этих чисел так, чтобы полученная строка было симметричной  (читалась одинаково как слева направо, так и справа налево).  Если невозможно, то программа должна вывести на экран число 0, а если возможно, то вывести число 1.
count = [0]*16
n = int(input())
for i in range(n):
  x = int(input("x"))
  while x > 0:
    count[x % 16] += 1
    x //= 16

i = 0
check = 0
while i <= 15 and check < 2:
  check += count[i] % 2
  i += 1

print(int(check < 2))