from CatTest import Cat

r = Cat("Bars", "M", 3)

print(f"Имя кота: {r.name}")
print(f"Пол кота: {r.sex}")
print(f"Возраст кота: {r.age}")

print()

print(r.get_name())
print(r.get_sex())
print(r.get_age())



