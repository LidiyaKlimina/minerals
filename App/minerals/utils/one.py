import pandas as pd

def get_vitamins_input(input_vitamins) -> list:
    # = input("Впишите через запятую, какие витамины и микроэлементы вы планируете принимать: ")
    #vitamins_list = [input_vitamins.strip().lower() for input_vitamins in input_vitamins.split(',')]
    vitamins_list = input_vitamins.split(',')
    return vitamins_list


def filter_table(vitamins_list):
    df = pd.read_csv('C:/Users/kijud/Git.Projects/minerals/App/vitamin_compatibility.csv', index_col=0) 
    filtered_df=df.loc[vitamins_list, vitamins_list] 
    print("Таблица совместимости ваших витаминов:")
    print(filtered_df)

    return filtered_df