import pandas as pd
from webscraping import done
import csv
import numpy as np  # Import numpy to handle NaN values

# Read the CSV file into a DataFrame
df = pd.read_csv('formlink.csv')

# Extract columns from the DataFrame
listmail = df["Exercism Profile URL"]
Name = df["Name"]
dictionary = {}

# Scrape data and write it to a new CSV file
with open("ranking.csv", "w", newline="") as csvfile:
    rank_csv = csv.DictWriter(csvfile, fieldnames=["Name", "Total"])
    rank_csv.writeheader()
    for i, j in zip(listmail, Name):
        try:
            total = done(i)
            if total is not None:  # Check if total is valid
                dictionary[j] = total
                rank_csv.writerow({"Name": j, "Total": total})
                print(j, total)
            else:
                print(f"Failed to get total for {j}")
        except Exception as e:
            print(e)

# Read the newly created CSV file into a DataFrame
rank = pd.read_csv('ranking.csv')

# Sort the DataFrame by the 'Total' column
sorted_df = rank.sort_values(by="Total", ascending=False)

# Add rank based on the sorted DataFrame
sorted_df['Rank'] = sorted_df['Total'].rank(method='first', ascending=False)
sorted_df['Rank'] = sorted_df['Rank'].fillna(0).astype(int)

# Save the sorted DataFrame to a new CSV file
sorted_df.to_csv('sorted_ranking.csv', index=False)

# Print a message to indicate completion
print("Data updated back to file 'sorted_ranking.csv'")

# Print the sorted DataFrame with rank
print(sorted_df)
