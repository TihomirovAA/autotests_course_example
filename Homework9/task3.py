# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
max_price_list = []
with open("test_file/task_3.txt", 'r', encoding='utf-8') as file:

    with_moment_price = 0
    for line in file.readlines():
        try:
            with_moment_price += int(line)
        except ValueError:
            max_price_list.append(with_moment_price)
            with_moment_price = 0
max_price_list = sorted(max_price_list, reverse=True)
three_most_expensive_purchases = sum(max_price_list[:3])



assert three_most_expensive_purchases == 202346