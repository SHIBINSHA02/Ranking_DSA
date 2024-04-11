import requests
from bs4 import BeautifulSoup
from hidden.data import url 

def done(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        try:
            reputation_element = soup.find('div', class_='c-primary-reputation')

            # Extract the reputation value
            reputation_value = reputation_element.find('span').text.strip()
            if reputation_element:
                return reputation_value
            else:
                print("Element not found.")
        except Exception as e:  # Catching all exceptions
            print("An error occurred:", e)
    else:
        print("Failed to fetch URL:", response.status_code)
