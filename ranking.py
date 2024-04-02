import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('form_data.csv')

# Sort DataFrame by score (assuming 'Score' column exists)
df = df.sort_values(by='Score', ascending=False)


# Add rank column
df['Rank'] = range(1, len(df) + 1)

# Print the DataFrame
print(df)
