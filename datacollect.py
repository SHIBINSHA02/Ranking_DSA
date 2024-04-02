# Assuming you've already got the Google Form link stored somewhere accessible
google_form_link = input("Enter the link:")

import csv
from bs4 import BeautifulSoup
import requests

# Fetch the webpage content
response = requests.get(google_form_link)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Now you can work with the parsed HTML content using BeautifulSoup to extract the data you need
# For example:
# Find all input elements with the class "quantumWizTextinputPaperinputInput"
inputs = soup.find_all("input", class_="quantumWizTextinputPaperinputInput")

# Process the inputs, maybe write them to a CSV file
with open("form_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for input_element in inputs:
        writer.writerow([input_element.get("name", ""), input_element.get("value", "")])

