import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Starting script...")

# Define the URL of the webpage you want to scrape
url = ''

# Send a request to fetch the content of the webpage
try:
    response = requests.get(url)
    response.raise_for_status()
    print("Webpage fetched successfully.")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    exit()

# Parse the content using BeautifulSoup
try:
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Content parsed with BeautifulSoup.")
except Exception as e:
    print(f"Failed to parse content: {e}")
    exit()

# Find all heading tags (h2)
headings = soup.find_all('h2')
if headings:
    print(f"Found {len(headings)} headings.")
else:
    print("No headings found.")

# Extract the text of each heading and store it in a list
heading_texts = [heading.text.strip() for heading in headings]

# Create a DataFrame from the list
df = pd.DataFrame(heading_texts, columns=['Headings'])

# Save the DataFrame to an Excel file using openpyxl
try:
    df.to_excel('headings.xlsx', engine='openpyxl', index=False)
    print('Headings have been exported to headings.xlsx')
except Exception as e:
    print(f"Failed to export to Excel: {e}")
