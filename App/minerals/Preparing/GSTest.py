import gspread
import pandas as pd
import sys
import os

"""
from oauth2client.service_account import ServiceAccountCredentials
sheet_url = "https://docs.google.com/spreadsheets/d/1rHAhwijBCovdqnNg8aA90_iuNuRjTUQ47DzISg5fqdc/edit?usp=sharing"
api_key = "AIzaSyC179K1UX2ZGWzsQ8AOD6GvJ6kG3Sea16I"
client = gspread.Client(None, None, api_key)
sheet = client.open_by_url(sheet_url).sheet1
data = sheet.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])
df.set_index(data[0][0], inplace=True)
df = df.apply(pd.to_numeric, errors='ignore')


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/kijud/Git.Projects/minerals/App/minerals/Preparing/myproject-91040-b11158698447.json", scope)
client = gspread.authorize(creds)
spreadsheet = client.open_by_key('1rHAhwijBCovdqnNg8aA90_iuNuRjTUQ47DzISg5fqdc')
sheet = spreadsheet.sheet1

# Загрузка данных из таблицы в DataFrame
data = sheet.get_all_values()
df = pd.DataFrame(data[1:], columns=data[0])
df.set_index(data[0][0], inplace=True)
df = df.apply(pd.to_numeric, errors='ignore')

print(df)
"""



gc = gspread.service_account(filename='C:/Users/kijud/Git.Projects/minerals/App/minerals/Preparing/myproject-91040-b11158698447.json')
sh = gc.open("https://docs.google.com/spreadsheets/d/1rHAhwijBCovdqnNg8aA90_iuNuRjTUQ47DzISg5fqdc/")
print(sh)