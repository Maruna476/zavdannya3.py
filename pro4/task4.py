a = 5
b = 8
c = 3

print("Числа:", a, b, c)
print("Найбільше:", max(a, b, c))
print("Найменше:", min(a, b, c))


if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print("Є хоча б одне парне число")
else:
    print("Парних чисел немає")


if a > b and b < c:
    print(True)
else:
    print(False)


num = 7
prime = True

for i in range(2, num):
    if num % i == 0:
        prime = False

if prime:
    print("Число просте")
else:
    print("Число не просте")