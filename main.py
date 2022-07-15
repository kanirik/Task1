# Task1
a = "text"
b = 2
c = [1, 2]
d = {1: 'Vanya'}
print(a, b, c, d)

try:
    number = int(input('Введите число'))
    print('Вы ввели число: {}'.format(number))
except ValueError:
    print('Не число')

try:
    string = str(input('Введите строку'))
    print('Вы ввели строку: {}'.format(string))
except ValueError:
    print('Не строка')

# Task2
try:
    timeSec = int(input("Введите время в секундах"))
    print('чч:мм:сс {}'.format(str(timeSec // 60 // 60) + ":" + str(timeSec // 60 % 60) + ":" + str(timeSec % 60)))
except ValueError:
    print('Неверный тип данных')

# Task3 Нужно взять число от 0 до 9 или и на большем должно работать?
try:
    number = str(input('Введите число от 0 до 9:'))
    newNumber = 0
    newNumber = int(number * 3) + int(number * 2) + int(number)
    print('Новое число: {}'.format(newNumber))
except ValueError:
    print('Вы ввели не число')

# Task4
try:
    number = int(input('Введите целое число'))
    res = 0
    while number != 0:
        res = max(res, number % 10)
        number //= 10
    print('maxNumber:', res)

except ValueError:
    print('Вы ввели нецелое число')

# Task5
costs = int(input('Введите издержки'))
revenue = int(input('Введите выручка'))
if(revenue-costs) > 0:
    print("It is profit!")
    costEff = (revenue - costs) / revenue
    print("Рентабильность:", costEff)
    countPerson = int(input('Введите число сотрудников'))
    revenueOnPerson = (revenue - costs) / countPerson
    print('Прибыль на сотрудника', revenueOnPerson)
else:
    print("It is loss!")

# Task6
a = int(input('Введите a'))
b = int(input('Введите b'))
day = 1
while(a-b) <= 0:
    day += 1
    a = a + 0.1 * a

print("Число дней", day)
