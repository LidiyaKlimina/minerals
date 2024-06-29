import pandas as pd

# Функция, которая разделяет строку витаминов, введенную пользователем.
def get_vitamin_list(user_input):
    vitamins = [vitamin.strip() for vitamin in user_input.split(',')]
    return vitamins

# Функция, которая фильтрует таблицу совместимости, чтобы оставить только витамины из списка.
def filter_vitamin_compatibility(vitamins, compatibility_df):
    filtered_df = compatibility_df.loc[vitamins, vitamins]
    return filtered_df

def main():
    # Получаем ввод от пользователя
    user_input = input("Перечислите через запятую какие витамины вы планируете принимать: ")
    
    # Разделяем строку на витамины
    vitamins = get_vitamin_list(user_input)
    
    # Загружаем таблицу совместимости витаминов из Excel файла
    compatibility_df = pd.read_excel('/vitamin_compatibility.xlsx', index_col=0)
    
    # Фильтруем таблицу совместимости
    filtered_compatibility_df = filter_vitamin_compatibility(vitamins, compatibility_df)
    
    # Выводим таблицу совместимости
    print("Таблица совместимости указанных витаминов:")
    print(filtered_compatibility_df)
    print('Помните!  Принимать добавки рекомендуется только после сдачи анализов и консультации с вашим лечащим врачом. Высокие дозы некоторых нутриентов могут вызвать ухудшение самочувствия. Благодаря правильной комбинации компонентов вы сможете улучшить как общий тонус организма, так и работу всех систем и органов.')

# Запускаем основную функцию
if __name__ == "__main__":
    main()
    
    