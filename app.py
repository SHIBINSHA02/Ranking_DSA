
import streamlit as st
import pandas as pd
import os

# Check if the sorted ranking data file exists
if os.path.exists('sorted_ranking.csv'):
    # Load the sorted ranking data
    sorted_df = pd.read_csv('sorted_ranking.csv')

    # Set the title of the app
    st.title("Exercism Profile Rankings")

    # Display the sorted DataFrame
    st.write("Here are the rankings based on total scores:")
    st.dataframe(sorted_df)

    # Optionally, you can add more features like filtering or searching
    name_filter = st.text_input("Filter by Name:")
    if name_filter:
        filtered_df = sorted_df[sorted_df['Name'].str.contains(name_filter, case=False)]
        st.dataframe(filtered_df)
else:
    st.error("The sorted ranking file does not exist. Please run the ranking script first.")