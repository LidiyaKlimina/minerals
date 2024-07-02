from App.minerals.utils.one import get_vitamins_input, load_compatibility_data, filter_compatibility_data, \
    print_compatibility_table


def main():
    vitamins_list = get_vitamins_input()
    compatibility_data = load_compatibility_data()
    filtered_data = filter_compatibility_data(vitamins_list, compatibility_data)
    print_compatibility_table(vitamins_list, filtered_data)

if __name__ == "__main__":
    main()
