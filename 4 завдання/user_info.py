name = input("ім'я: ")
year = int(input("рік народження: "))
city = input(" місто: ")

age = 2026 - year

print("Привіт", name)
print(" вік:", age)

if age < 12:
    print("Дитина")
elif age < 18:
    print("Підліток")
elif age < 60:
    print("Дорослий")
else:
    print("Літня людина")

if city == "Київ":
    print("Ви живете у столиці")
else:
    print("Це не столиця")