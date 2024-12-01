import csv
import pandas as pd
from collections import Counter

with open('numbers.txt', 'r') as file:
    stripped = (line.strip() for line in file)
    lines = (line.split("   ") for line in stripped if line)
    with open('numbers.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('first', 'second'))
        writer.writerows(lines)



df = pd.read_csv("numbers.csv")
df['first'] = df['first'].sort_values(ascending=False)
df.to_csv('numbers_sorted.csv', index=False)

data = pd.read_csv('numbers_sorted.csv')

df1 = pd.DataFrame(data,
                   columns=['first', 'second'])

df1['difference'] = (df1['second'] - df1['first'])
df1.to_csv('output.csv', index=False)


df2=pd.read_csv('output.csv')
print(df2['difference'].sum())