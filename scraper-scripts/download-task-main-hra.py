## This is the main script that implements a for loop in order to download files from the hra website. 
## Note that the files that are downloaded have to be saved to a specific folder
## In order to use this script, follow the following steps -- 
## Firstly, do a keyword search with the keyword you want
## Next, once you have applied all the filters, reach the page which shows the table of filtered entries
## Chech the total number of pages this table spans across and then add the number of pages to the "total_pages"
## Then add the url till "page=" to the url prefix
## Add the desired folder location and then run the script

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument("--allow-running-insecure-content")  # Allow insecure content
chrome_options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://www.hrarchive.or.kr")  # Replace example.com with your site's domain
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Academics\Research-Assistantship\downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
# Start WebDriver
driver = webdriver.Chrome(options=chrome_options)

total_pages = 6 ## replace this with total number of pages to download
row_num = 1
## Looping through the pages:
for i in range(1,total_pages + 1): 

    # Open the webpage
    url_prefix = "http://www.hrarchive.or.kr/theme/basic/list.php?search_content=%EA%B6%8C%EB%A6%AC&make_where=&make_start_date=1990-01-01&make_end_date=2024-12-31&category=100&shape=117&page=" ## Setting up URL prefix
    url_suffix = "&navigation_menu="  # Setting up URL suffix
    page_no = str(i) ## replacing page number
    url = url_prefix + page_no + url_suffix ## ccreating final download url
    driver.get(url) 
    print(i)
    # Locate the table
    table = driver.find_element(By.TAG_NAME, "table")  # Adjust selector as needed

    # Extract table rows
    
    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows[1:]:  # Skip header row
        metadata_link = row.find_element(By.TAG_NAME, "a")
        metadata_link.click()
        time.sleep(2) # verifying the page loading

        # Locate the table

        metadata_table = driver.find_element(By.TAG_NAME, "table")  # Adjust selector as needed

        # Extract table rows

        download_header = metadata_table.find_element(By.XPATH, "//th[contains(text(),'다운로드')]")
        download_row = download_header.find_element(By.XPATH, "..")
        download_cell = download_row.find_element(By.TAG_NAME, "td")
        dowload_links = download_cell.find_elements(By.TAG_NAME, "a")
        for link in dowload_links:
            link.click()
            time.sleep(5)  # Adjust based on file size
            
        

        print("Download timer finished, currently on page " + str(i) + " and row " + str(row_num))

        # Wait for the file to download before closing the browser (adjust sleep time if needed)

        row_num = row_num + 1

        driver.back()
        time.sleep(2)

driver.quit()