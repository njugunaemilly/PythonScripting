import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://kmpdc.go.ke/Registers/General_Practitioners.php"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}
# Make a GET request to the website  using defined variable
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the data
    table = soup.find('table')

    # Extract data from the table and store it in a DataFrame
    data = []
    headers = [th.text.strip() for th in table.find_all('th')]
    for row in table.find_all('tr')[1:]:  # Skip the header row
        data.append([td.text.strip() for td in row.find_all('td')])

    df = pd.DataFrame(data, columns=headers)

    # Save the DataFrame to an Excel file
    df.to_excel("practitioners_data.xlsx", index=False)
    print("Data scraped and saved to practitioners_data.xlsx")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
