#задание 1

with open('python_text.txt', 'w') as fr:
    while True:
        line = input('Введите текст: ')
        if line == '':
            break
    fr.write(line +'\n')

#задание 2

my_file = open('python_file_1.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('python_file_1.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('python_file_1.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f' Количество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('python_file_1.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()

#задание 3


with open('job_list.txt', 'r') as fr:
    sal = []
    lines = fr.readlines()
    for line in lines:
        name, salary = line.split(' - ')
        sal.append(int(salary))
        if int(salary) < 20000:
           print(line, end='')
print('\nСредняя зарплата: ', sum(sal) / len(sal))

#задание 4

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('python_file_2.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('python_file_2_1.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)


#задание 5

def summary():
    try:
        with open('python_file_3.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода-вывода')
summary()

#задание 6

with open('python_file_4.txt', 'r') as init_f:
    def sum_hours(string_hours):
        list_loc = string_hours.split()
        sum_loc = 0
        for el_l in list_loc:
            list_split = el_l.split('(')
            if list_split[0].isdigit():
                sum_loc += int(list_split[0])
        return sum_loc
    

file_name = 'python_file_4.txt'
list_lesson = []
list_h = []
with open(file_name) as f_obj:
    for line in f_obj:
        list_mid = line.split(':')
        list_lesson.append(list_mid[0])
        list_h.append(list_mid[1])

dict_out = {}
for n in range(len(list_lesson)):
    dict_out[list_lesson[n]] = sum_hours(list_h[n])

print(f'Словарь - {dict_out}')

#задание 7

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('python_file_5.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('python_file_5.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')