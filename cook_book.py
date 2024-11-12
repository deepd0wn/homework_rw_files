with open('cook_book.txt', 'r', encoding='UTF-8') as f:
    cook_book = {}
    str_list = []
    blank_str = []
    for id, line in enumerate(f):
        if len(line) == 1:
            blank_str.append(id)
        str_list.append(line.strip())

    idx = 0
    for id in blank_str:
        cook_book[str_list[idx]] = []
        j = idx + 2
        while j != id:
            ing_list = str_list[j].split(' | ')
            ing_dict = {'ingredient_name': ing_list[0], 'quantity': int(ing_list[1]), 'measure': ing_list[2]}
            cook_book[str_list[idx]].append(ing_dict)
            j += 1
        idx = id + 1


# print(cook_book)


dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

def get_shop_list_by_dishes(dishes, person_count):
    ing_dict = {}
    for dish in dishes:
        print(cook_book[dish])

get_shop_list_by_dishes(dishes, person_count)

{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}