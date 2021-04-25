# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например,
# print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().


def int_func(str_arg: str):
    res = str_arg.split(' ')
    for i in range(len(res)):
        res[i] = res[i].capitalize()
    return ' '.join(res)


print(int_func(input('Введите текст: ')))
