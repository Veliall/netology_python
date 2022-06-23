import os

FILE_NAME = 'recipes.txt'
BASE_PATH = os.getcwd()
DIRECTORY = 'task3'
FILE_1 = '1.txt'
FILE_2 = '2.txt'
FILE_3 = '3.txt'


# Задание 1
def read_file(file: str) -> dict:
    with open(file) as f:
        result = {}
        for line in f:
            dish_name = line.strip()
            ingredients = []
            for item in range(int(f.readline())):
                ingredient = f.readline().strip().split('|')
                ingredients.append(
                    {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]})
            result[dish_name] = ingredients
            f.readline()
    return result


# Задание 2
def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    result = {}
    cook_book = read_file(FILE_NAME)
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            count = int(ingredient['quantity']) * person_count
            result.setdefault(name, {'measure': ingredient['measure'], 'quantity': 0})['quantity'] += count
    return result


# Задание 3
def write_some_files_in_one(files: list):
    data = get_data_for_write(files)
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
    with open('result.txt', 'a') as f:
        for file in sorted_data:
            f.write(file + '\n')
            f.write(str(data.get(file)[0]) + '\n')
            for line in data.get(file)[1]:
                f.write(line)
            f.write('\n')


def get_data_for_write(files):
    result = {}
    for file in files:
        path = os.path.join(BASE_PATH, DIRECTORY, file)
        with open(path) as f:
            lines = f.readlines()
            result[file] = (len(lines), lines)
    return result


# print(read_file('recipes.txt'))
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
write_some_files_in_one([FILE_1, FILE_2, FILE_3])
