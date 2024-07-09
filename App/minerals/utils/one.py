import pandas as pd
import os

def get_vitamins_input(input_vitamins) -> list:
    # = input("Впишите через запятую, какие витамины и микроэлементы вы планируете принимать: ")
    vitamins_list = [input_vitamins.strip().lower() for input_vitamins in input_vitamins.split(',')]
    #vitamins_list = input_vitamins.split(',')
    return vitamins_list


def filter_table(vitamins_list):
    file_name = "../DataBase/vitamin_compatibility.csv"
    file_path = os.path.join(os.path.dirname(__file__), file_name) 
    df = pd.read_csv(file_path, index_col=0)
    filtered_df=df.loc[vitamins_list, vitamins_list] 
    
    return filtered_df
    
    return filtered_df

def print_table(filtered_df):
    print("Таблица совместимости ваших витаминов:")
    print(filtered_df)