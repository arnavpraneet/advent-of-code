import csv
import pandas as pd

# Read and process the numbers.txt file
with open('numbers.txt', 'r') as file:
    stripped = (line.strip() for line in file)
    lines = (line.split() for line in stripped if line)
    with open('numbers.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('first', 'second'))
        writer.writerows(lines)

# Read the CSV file into a DataFrame
df = pd.read_csv("numbers.csv")
print("Initial DataFrame:")
print(df)

# Convert columns to numeric types
df['first'] = pd.to_numeric(df['first'])
df['second'] = pd.to_numeric(df['second'])
print("DataFrame after converting to numeric types:")
print(df)

# Sort the DataFrame
sorted_df = df.sort_values(by=['first', 'second'], ascending=True)
sorted_df.to_csv('numbers_sorted.csv', index=False)
print("Sorted DataFrame:")
print(sorted_df)

# Calculate the difference and save to output.csv
sorted_df['difference'] = sorted_df['first'] - sorted_df['second']
sorted_df.to_csv('output.csv', index=False)
print("DataFrame with difference column:")
print(sorted_df)

# Read the output.csv and print the sum of the differences
df2 = pd.read_csv('output.csv')
print("Final DataFrame from output.csv:")
print(df2)
print("Sum of differences:")
print(df2['difference'].sum())