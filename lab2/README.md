## Лабораторная работа №2: Сортировка вставками, выбором и пузырьковая

## Студентка ИТМО, Азизова Наида Элимизовна | 464939

## Вариант 2

### Навигация
- [ ] [Задача 1 - Сортировка слиянием ](task1)
- [ ] [Задача 3 - Число инверсий ](task3)
- [ ] [Задача 4 - Бинарный поиск ](task4)
- [ ] [Задача 5 - Представитель большинства ](task5)
- [ ] [Задача 7 - Поиск максимального подмассива за линейное время ](task7)
## Описание
Лабораторная работа посвящена сортировке слиянием и в целом методу декомпозиции (Разделяй и властвуй)

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/naidaazizova/algosi.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd algosi
   ```
3. **Запуск всех задач**

   ```bash
   for script in lab2/*/src/*.py; do PYTHONPATH=$(pwd) python3 "$script"; done
   ```

4. **Запуск всех тестов задач**

   ```bash
   for script in lab2/*/tests/*.py; do PYTHONPATH=$(pwd) python3 "$script"; done
   ```