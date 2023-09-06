'''
Задача № 3:Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
используйте его строковое представление.
'''

def only_keys_parameters(**kwargs):
    new_dict = {}
    hashable_types = (str, int, float)

    for key, value in kwargs.items():
        if isinstance(value, hashable_types):
            new_dict[value] = key
        else: ### для нехешируемых аргументов переводим их в строковое представление
            str_value = str(value)
            new_dict[str_value] = key

    return new_dict

# Проверка работы функции
result_dict = only_keys_parameters(key1 = 42, key2 = "Привет всем!", key3 = [1, 2, 3])
print(result_dict)

