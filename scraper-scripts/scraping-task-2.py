from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Set up the Selenium WebDriver (make sure chromedriver is installed)
driver = webdriver.Chrome(options = chrome_options)

data = []
total_pages = 5 ## replace this with total number of pages to download

## Looping through the pages:
for i in range(1,total_pages + 1): 

    # Open the webpage
    url_prefix = "http://www.hrarchive.or.kr/theme/basic/list.php?search_content=%EA%B6%8C%EB%A6%AC&make_where=&make_start_date=1990-01-01&make_end_date=2024-12-31&category=100&shape=111&page=" ## Setting up URL prefix
    url_suffix = "&navigation_menu="  # Setting up URL suffix
    page_no = str(i) ## replacing page number
    url = url_prefix + page_no + url_suffix ## ccreating final download url
    driver.get(url) 
    print(i)
    # Locate the table
    table = driver.find_element(By.TAG_NAME, "table")  # Adjust selector as needed

    # Extract table headers
    headers = [header.text for header in table.find_elements(By.TAG_NAME, "th")]

    # Extract table rows
    
    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows[1:]:  # Skip header row
        cells = row.find_elements(By.TAG_NAME, "td")
        data.append([cell.text for cell in cells])

    



# Close the driver
driver.quit()

# Convert to a DataFrame
df = pd.DataFrame(data, columns=headers)

print(df.shape)

df.to_excel('rights-press-release-table.xlsx')
# # Print or save the data
# print(df)