import pandas as pd

df = pd.read_csv('C:/Users/kijud/Git.Projects/minerals/App/vitamin_compatibility.csv', index_col=0)
#filtered_df=df[['d', 'k', 'fe']]  
filtered_df=df.loc[['d', 'k', 'fe'],['d', 'k', 'fe']] 
print(filtered_df)
# df.head()
