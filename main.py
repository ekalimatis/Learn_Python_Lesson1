# переменые
# 1
name = 'Eva'
print(name)
# простые типы данных
# 1
a = 2
b = 0.5
print(a + b)
# 2
name = input('Мое имя:')
print('Привет,', name, '!')
# 3
v = int(input('Введите число от 1 до 10'))
print(v + 10)
# 4
print(float('1'))
print(float('2.5'))
print(bool(1))
print(bool(''))
print(bool(0))
# списки
# 1
num = [3, 5, 7, 9, 10.5]
print(num)
num.append('Python')
print(num)
print(len(num))
print(num[1], num[-1], num[1:4])
num.remove('Python')
print(num)
a={"city": "Москва", "temperature": "5"}
print(a["city"])
print(a.get("country", 'Россия'))
a["date"]="27.05.2019"
print(a)

