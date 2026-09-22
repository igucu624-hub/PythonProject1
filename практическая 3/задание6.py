student = {} # Создали словарь
name = input(" Ваше имя : ")
age_str = input(" Ваш возраст : ")
sub_str = input(" Любимые предметы : ")

student = {
    'name': name,
    'age': int(age_str),
    'sub': sub_str}


print('=' * 30)
print('АНКЕТА СТУДЕНТА')
print('=' * 30)
print(f'Имя: {student['name']}')
print(f'Возраст: {student['age']}')
print(f'Любимые предметы: {student['sub']}')
print('=' * 30)