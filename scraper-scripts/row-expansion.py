import pandas as pd

df = pd.read_excel("initial-data/rights-table.xlsx") # reading the data

col_name = '생산처'
for index, row in df.iterrows():
    # print(row[col_name])
    df.at[index, col_name] = str(row[col_name]).split(",")
    # print(row[col_name])
    
df_final = df.explode(col_name).reset_index(drop=True)
df_final.drop(df_final.columns[0], axis=1, inplace=True)
print(df.shape)
print(df_final.shape)
df_final.to_excel('rights-table-updated.xlsx')