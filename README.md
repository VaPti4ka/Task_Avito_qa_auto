## Задание: github.com/avito-tech/qa-into-CoE-trainee-task

# Комментарии по заданию
## 1) Файл TestcaseStructure.json
Файл TestcaseStructure.json имеет ошибки по формату .json

Решение: оставить два файла 
* TestcaseStructure.json - для проверки на обработку ошибки
* TestcaseStructure_reformat.json - для проверки работоспособности программы

## 2) Трактовка пункта "Доп. информация"
Пункт 2: 
"Если у параметра с id из Values.json, в массиве values нет объекта с id равным value,
то считаем, что такого значения нет и оставляем поле value **пустым**." 
Описание не совпадает с предоставленным файлом StructureWithValues.json, который предоставляется как
образец корректного выполнения задачи.
## Задание выполняется так, чтобы итоговый результат совпадал с файлом StructureWithValues.json
Тогда при ненахождении соответствующего id в values будет подставляться значение title из первого вложенного элемента 


# Комментарии по решению
##1) Исходные данные лежат в data_files/original
В setting.json: testcase_1 -> оригинальный файл с заданием, testcase_2 -> исправленный
##2) Результат в data_files/created

[]: https://github.com/avito-tech/qa-into-CoE-trainee-task