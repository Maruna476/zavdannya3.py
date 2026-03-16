a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))


max_num = max(a, b, c)
min_num = min(a, b, c)

print("Найбільше число:", max_num)
print("Найменше число:", min_num)


if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print("Хоча б одне число є парним")
else:
    print("Парних чисел немає")


condition = a > b and b < c
print("Результат складної умови:", condition)


num = int(input("Введіть число для перевірки чи воно просте: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Число є простим")
else:
    print("Число не є простим")