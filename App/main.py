from minerals.utils.one import get_vitamins_input, filter_table, print_table

def main():
    input_vitamins= input("Перечислите через запятую какие витамины вы планируете принимать: ")
    vitamins_list= get_vitamins_input(input_vitamins) # Разделяем строку на витамины
    filtered_df= filter_table(vitamins_list)
    print_table(filtered_df)

if __name__ == "__main__":
    main()