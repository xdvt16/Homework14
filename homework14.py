def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


# Разное количество аргументов
print_params(False)
print_params(False, 54)
print_params(False, 54, "Mars")
print()

# Вызов функции без аргументов
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])


# Создаём список и словарь
values_list = [False, "Game", 12]
values_dict = {"a": bool, "b": 'Bomb', "c": 123}
print()

# Передаём список и словарь в функцию "print_params", используя распаковку (* для списка и ** для словаря)
print_params(*values_list)
print_params(**values_dict)
print()

# Создаём список values_list_2 с двумя элементами разных типов
values_list_2 = ["New York", False]
print_params(*values_list_2, 42)
# Работает как надо!