import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

def get_vitamins_input(input_vitamins) -> list:
    # = input("Впишите через запятую, какие витамины и микроэлементы вы планируете принимать: ")
    vitamins_list = [input_vitamins.strip().lower() for input_vitamins in input_vitamins.split(',')]

    return vitamins_list


def open_table_from_google():
    sheet_url = "https://docs.google.com/spreadsheets/d/1rHAhwijBCovdqnNg8aA90_iuNuRjTUQ47DzISg5fqdc/edit?usp=sharing"
    api_key = "AIzaSyC179K1UX2ZGWzsQ8AOD6GvJ6kG3Sea16I"
    client = gspread.Client(None, None, api_key)
    sheet = client.open_by_url(sheet_url).sheet1
    data = sheet.get_all_values()
    df = pd.DataFrame(data[1:], columns=data[0])
    df.set_index(data[0][0], inplace=True)
    df = df.apply(pd.to_numeric, errors='ignore')

    # scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    # creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/kijud/Git.Projects/minerals/App/minerals/Preparing/myproject-91040-b11158698447.json", scope)
    # client = gspread.authorize(creds)
    # spreadsheet = client.open_by_url('1rHAhwijBCovdqnNg8aA90_iuNuRjTUQ47DzISg5fqdc')
    # sheet = spreadsheet.sheet1

    # # Загрузка данных из таблицы в DataFrame
    # data = sheet.get_all_values()
    # df = pd.DataFrame(data[1:], columns=data[0])

    return df

def filter_table(vitamins_list, df):
    #df = pd.read_csv('C:/Users/kijud/Git.Projects/minerals/App/minerals/DataBase/vitamin_compatibility.csv', index_col=0)
    # filtered_df = df.loc[df['Витамины'].isin(vitamins), ['Витамины'] + vitamins]
    # filtered_df = filtered_df.set_index('Витамины')
    filtered_df=df.loc[vitamins_list, vitamins_list] 
    
    return filtered_df

def print_table(filtered_df):
    print("Таблица совместимости ваших витаминов:")
    print(filtered_df)


def main():
    input_vitamins= input("Перечислите через запятую какие витамины вы планируете принимать: ")
    vitamins_list= get_vitamins_input(input_vitamins) # Разделяем строку на витамины
    df=open_table_from_google()
    filtered_df= filter_table(vitamins_list, df)
    print_table(filtered_df)

if __name__ == "__main__":
    main()