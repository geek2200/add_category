import pandas as pd


df = pd.read_csv('final2.csv', sep='¬', encoding='utf-16', engine='python')

df2 = df.loc[df['num_writing'].notnull()]
index_list = df2.index.tolist()
max_list = df['data_user_id'].count()
df3 = pd.DataFrame(columns=['category'], index=[0])
print(df3)
for k in range(0, 2000):
    df3.append(pd.Series([k], index=df3.columns), ignore_index=True)
print(df3)
# for i in range(0, len(index_list)):



