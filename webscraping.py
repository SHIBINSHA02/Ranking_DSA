import requests
from bs4 import BeautifulSoup
# from hidden.data import url  # Commented out as it's not used

def done(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        try:
            reputation_element = soup.find('div', class_='c-primary-reputation')

            # Check if the element is found before accessing it
            if reputation_element:
                reputation_value = reputation_element.find('span').text.strip()
                return reputation_value
            else:
                print("Element not found.")
                return None  # Return None if the element is not found
        except Exception as e:  # Catching all exceptions
            print("An error occurred:", e)
            return None  # Return None on error
    else:
        print("Failed to fetch URL:", response.status_code)
        return None  # Return None if the request fails
