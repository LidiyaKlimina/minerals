from minerals.utils.one import get_vitamins_input, load_compatibility_data, filter_compatibility_data, \
    print_compatibility_table


def main():
    # Получаем ввод от пользователя
    vitamins_input = input("Перечислите через запятую какие витамины вы планируете принимать: ")
    # Разделяем строку на витамины
    vitamins_list = get_vitamins_input(vitamins_input)
    compatibility_data = load_compatibility_data()
    filtered_data = filter_compatibility_data(vitamins_list, compatibility_data)
    print_compatibility_table(vitamins_list, filtered_data)

if __name__ == "__main__":
    main()
