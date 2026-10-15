from array import *

masiv = array('i', [0] * 7)

print("Введіть 7 цілих чисел:")
for i in range(7):
    masiv[i] = int(input("Елемент " + str(i+1) + ": "))

print("\nДодатні дільники кожного елемента:")
for num in masiv:
    if num == 0:
        print("Для числа 0 дільниками є всі числа, крім 0")
        continue

    val = abs(num)
    divisors = []

    for div in range(1, val + 1):
        if val % div == 0:
            divisors.append(str(div))

    print("Для числа", num, ":", ", ".join(divisors))