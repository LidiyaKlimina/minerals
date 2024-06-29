import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

#окно 1. Инпут через запятую что будем принимать
print ('Впиши через запятую, какие витамины и микроэлементы ты планируешь принимать')
user_input_minerals = input()

# Блок где собираем таблицу из вписанных элементов.
def get_vitamin_list(user_input_minerals):
    """
    Функция, которая разделяет строку витаминов, введенную пользователем.
    """
    vitamins = [vitamin.strip() for vitamin in user_input.split(',')]
    return vitamins

def filter_vitamin_compatibility(vitamins, compatibility_df):
    """
    Функция, которая фильтрует таблицу совместимости, чтобы оставить только витамины из списка.
    """
    filtered_df = compatibility_df.loc[vitamins, vitamins]
    return filtered_df

def main():
    # Настройка доступа к Google Sheets
    sheet_url = "https://docs.google.com/spreadsheets/d/1M4n9tNLiUZc1WbURTeco8voJ8Eq1_NYDzHbcwgPXJGQ/edit?usp=sharing"
    
    # Загрузка данных из Google Sheets в DataFrame
    data = sheet.get_all_values()
    compatibility_df = pd.DataFrame(data[1:], columns=data[0])
    compatibility_df.set_index(data[0][0], inplace=True)

    # Конвертация значений в числовой формат (если необходимо)
    compatibility_df = compatibility_df.apply(pd.to_numeric, errors='ignore')
    
    # Разделяем строку на витамины
    vitamins = get_vitamin_list(user_input_minerals)

    # Фильтруем таблицу совместимости
    filtered_compatibility_df = filter_vitamin_compatibility(vitamins, compatibility_df)

    #Выводим окно 2. Таблица совместимости
    print("Таблица совместимости указанных витаминов:")
    print(filtered_compatibility_df)
    print('Помните!  Принимать добавки рекомендуется только после сдачи анализов и консультации с вашим лечащим врачом. Высокие дозы некоторых нутриентов могут вызвать ухудшение самочувствия. Благодаря правильной комбинации компонентов вы сможете улучшить как общий тонус организма, так и работу всех систем и органов.')