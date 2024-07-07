file = open('vitamin_compatibility.csv', 'r')
print(file)


# def get_vitamins_input(input_vitamins) -> list:
#     # = input("Впишите через запятую, какие витамины и микроэлементы вы планируете принимать: ")
#     #vitamins_list = [input_vitamins.strip().lower() for input_vitamins in input_vitamins.split(',')]
#     vitamins_list = input_vitamins.split(',') 
#     return vitamins_list

# def load_compatibility_data(file_name='C:/Users/kijud/Git.Projects/minerals/App/vitamin_compatibility.csv'):
#     """
#     Функция для загрузки данных совместимости из CSV-файла.
#     """
#     compatibility_data = {}
#     headers = []
#     try:
#         with open(file_name, mode='r', encoding='utf-8') as file:
#             reader = csv.reader(file)
#             headers = next(reader)[1:]  # Пропускаем первый элемент (название строк)
#             headers = [header.lower().strip() for header in headers]
#             print("Заголовки:", headers)  # Отладочный вывод
            
#             for row in reader:
#                 vitamin = row[0].lower().strip()
#                 compatibility_data[vitamin] = {headers[i]: row[i+1].lower().strip() for i in range(len(headers))}
#                 print(f"Загрузка данных для {vitamin}: {compatibility_data[vitamin]}")  # Отладочный вывод
#     except FileNotFoundError:
#         print(f"Файл '{file_name}' не найден.")
#     except Exception as e:
#         print(f"Ошибка при чтении файла '{file_name}': {e}")
    
#     return headers, compatibility_data

# def filter_compatibility_data(vitamins_list, compatibility_data):
#     """
#     Функция для фильтрации данных совместимости по введенным пользователям витаминам.
#     """
#     filtered_data = {}
#     for vitamin in vitamins_list:
#         if vitamin in compatibility_data:
#             filtered_data[vitamin] = {k: v for k, v in compatibility_data[vitamin].items() if k in vitamins_list}
#         else:
#             print(f"Витамин '{vitamin}' не найден в данных совместимости.")  # Отладочный вывод
    
#     print("Отфильтрованные данные:", filtered_data)  # Отладочный вывод
#     return filtered_data

# def print_compatibility_table(vitamins_list, filtered_data):
#     """
#     Функция для вывода таблицы совместимости.
#     """
#     print("Таблица совместимости ваших витаминов:")
#     header = f"{'':<10}" + ''.join([f"{vitamin.upper():<10}" for vitamin in vitamins_list])
#     print(header)
    
#     for vitamin in vitamins_list:
#         row = f"{vitamin.upper():<10}" + ''.join([f"{filtered_data[vitamin].get(v, ''):<10}" for v in vitamins_list])
#         print(row)

# def main():
#     vitamins_list = get_vitamins_input()
#     headers, compatibility_data = load_compatibility_data()
#     filtered_data = filter_compatibility_data(vitamins_list, compatibility_data)
    
#     if filtered_data:
#         print_compatibility_table(vitamins_list, filtered_data)
#     else:
#         print("Не найдено данных совместимости для введенных витаминов.")

# if __name__ == "__main__":
#     main()
