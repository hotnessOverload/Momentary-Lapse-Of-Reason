# На вход программы поступают n <= 1000 натуральных чисел. Необходимо определить количество пар элементов набора (k), сумма элементов которых нечётна, произведение делится на 13, а номера чисел в последовательности отличаются менее, чем на 5. Напишите эффективную по времени и по памяти программу для решения этой задачи.
d = 5
n = int(input("nums"))
queue = []
k = k26 = k13 = even = odd = 0 # k26 - четное число, делящееся на 13, k13 - нечетное, делящееся на 13.
for i in range(d):
  x = int(input("x"))
  queue.append(x)
  if x % 13 == 0:
    if x % 2 == 0:
      k, k26, even = k+odd, k26+1, even+1
    else:
      k, k13, odd = k+even, k13+1, odd+1
  elif x % 2 == 0:
    k, even = k+k13, even+1
  else:
    k, odd = k+k26, odd+1
for i in range(d,n):
  # элемент удаляется из очереди
  if queue[i % d] % 13 == 0:
    if queue[i % d] % 2 == 0:
      k26, even = k26-1, even-1
    else:
      k13, odd = k13-1, odd-1
  elif queue[i % d] % 2 == 0:
    even -= 1
  else:
    odd -= 1
  # вводим элемент
  x = int(input("x"))
  if x % 13 == 0:
    if x % 2 == 0:
      k += odd
      k26, even = k26+1, even+1
    else:
      k += even
      k13, odd = k13+1, odd+1
  elif x % 2 == 0:
    k, even = k+k13, even+1
  else:
    k, odd = k+k26, odd+1
  queue[i % d] = x
print(k)


