immutable_var = 1, 1.5, 'Python'
print(immutable_var)
# Кортеж сам по себе является не изменяемым, можно изменять только некоторые изменяемые типы внутри самого кортежа, или список внутри самого кортежа.
# Кортеж не поддерживает замену значений по элементам.
# immutable_var[1] = 2  - пример неудачной попытки  изменения второй переменной в кортеже.
mutable_list = [1, 1.5, 'Python']
mutable_list[1] = 2
mutable_list.append('Новый_обьект')
print(mutable_list)