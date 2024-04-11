import pandas as pd
from webscraping import done
import csv

# Read the CSV file into a DataFrame
df = pd.read_csv('formlink.csv')

# Extract columns from the DataFrame
listmail = df["Exercism Profile URL"]
Name = df["Name"]
dictionary = {}

# Scrape data and write it to a new CSV file
with open("ranking.csv", "w", newline="") as csvfile:
    rank_csv = csv.DictWriter(csvfile, fieldnames=["Name", "Total", "Rank"])
    rank_csv.writeheader()
    for i, j in zip(listmail, Name):
        try:
            total = done(i)
            dictionary[j] = total
            rank_csv.writerow({"Name": j, "Total": total})
            print(j, total)
        except Exception as e:
            print(e)

# Read the newly created CSV file into a DataFrame
rank = pd.read_csv('ranking.csv')

# Sort the DataFrame by the 'Total' column
sorted_df = rank.sort_values(by="Total", ascending=False)

# Add rank based on the sorted DataFrame
sorted_df['Rank'] = sorted_df['Total'].rank(ascending=False, method='min').astype('Int64')

# Save the sorted DataFrame to a new CSV file
sorted_df.to_csv('sorted_ranking.csv', index=False)

# Print a message to indicate completion
print("Data updated back to file 'sorted_ranking.csv'")

# Print the sorted DataFrame with rank
print(sorted_df)
