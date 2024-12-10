# Работа со словарями:
my_dict = {'Сергей' : 1984, 'Евгения' : 1985, 'Никита' : 2016}
print(my_dict)
print(my_dict['Никита'])
print(my_dict.get('Максим'))
my_dict.update({'Максим' : 2020,
                'Анастасия' : 2000})
Deleted_value = my_dict.pop('Анастасия')
print(Deleted_value)
print(my_dict)
# Работа с множествами:
my_set = {1,2,3,1,2,1,4,7, 'Яблоко', 42.314, 'Яблоко'}
print(my_set)
my_set.add('Банан')
my_set.add(5)
my_set.discard(7)
print(my_set)
