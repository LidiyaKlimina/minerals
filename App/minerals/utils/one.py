import csv

def get_vitamins_input(vitamins_input) -> list:
    """
    Функция для ввода списка витаминов от пользователя.
    """
     # = input("Впишите через запятую, какие витамины и микроэлементы вы планируете принимать: ")
    vitamins_list = [vitamin.strip().lower() for vitamin in vitamins_input.split(',')]
    return vitamins_list

def load_compatibility_data():
    """
    Функция для загрузки данных совместимости из CSV-файла.
    """
    compatibility_data = {}
    with open('C:/Users/kijud/Git.Projects/minerals/App/vitamin_compatibility.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)[1:]  # Пропускаем первый элемент (пустой или заголовок 'Vitamins')
        headers = [header.lower() for header in headers]
        for row in reader:
            vitamin = row[0].lower()
            compatibility_data[vitamin] = {headers[i]: row[i+1] for i in range(len(headers))}
    return headers, compatibility_data
    

def filter_compatibility_data(vitamins_list, compatibility_data):
    """
    Функция для фильтрации данных совместимости по введенным пользователям витаминам.
    """
    filtered_data = {}
    for vitamin in vitamins_list:
        if vitamin in compatibility_data:
            filtered_data[vitamin] = compatibility_data[vitamin]
    return filtered_data
    

def print_compatibility_table(vitamins_list, filtered_data):
    """
    Функция для вывода таблицы совместимости.
    """
    print("Таблица совместимости ваших витаминов:")
    print(f"{'':<10}" + ''.join([f"{vitamin.upper():<10}" for vitamin in vitamins_list]))
    for vitamin in vitamins_list:
        print(f"{vitamin.upper():<10}" + ''.join([f"{filtered_data[vitamin].get(v, ''):<10}" for v in vitamins_list]))
