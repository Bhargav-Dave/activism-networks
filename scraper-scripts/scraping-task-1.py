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

for i in range(1,558):

    # Open the webpage
    url_prefix = "http://www.hrarchive.or.kr/theme/basic/list.php?search_content=%EC%9D%B8%EA%B6%8C&make_where=&make_start_date=&make_end_date=&category=&shape=&page="
    url_suffix = "&navigation_menu="  # Replace with the actual URL
    page_no = str(i)
    url = url_prefix + page_no + url_suffix
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

df.to_excel('human-rights-table.xlsx')
# # Print or save the data
# print(df)