import csv

# Convert numbers.txt to numbers.csv
with open('numbers.txt', 'r') as file:
    stripped = (line.strip() for line in file)
    lines = (line.split("   ") for line in stripped if line)
    with open('numbers.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('first', 'second'))
        writer.writerows(lines)

import pandas as pd

# Read numbers.csv
df = pd.read_csv("numbers.csv")

# Sort 'first' and 'second' columns independently
df['first'] = df['first'].sort_values(ascending=True).values
df['second'] = df['second'].sort_values(ascending=True).values

# Save sorted data to numbers_sorted.csv
df.to_csv('numbers_sorted.csv', index=False)

# Read numbers_sorted.csv and calculate differences
df['difference'] = df['first'] - df['second']
df.to_csv('output.csv', index=False)

# Sum the differences
df2 = pd.read_csv('output.csv')
print(df2['difference'].sum())
