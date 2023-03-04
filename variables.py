# Сотрудники - employees
name = 'Alex'      # имя сотрудника
age = 36           # возраст сотрудника
exp = 10           # стаж работы
use_fact = 1.2     # коэффициент полезного действия
is_engineer = True # является ли инженерным составом

emp = [name, age, exp, use_fact, is_engineer]
for i in range(len(emp)):
    print(type(emp[i]))