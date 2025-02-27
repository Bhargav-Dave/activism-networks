
## This script tests whether or not it is possible to download files from the HRA website (http://www.hrarchive.or.kr)
## It is then looped in the main download task file that does the actual downloading


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

# Open the webpage
driver.get("http://www.hrarchive.or.kr/theme/basic/list.php?search_content=%EC%9D%B8%EA%B6%8C&make_where=&make_start_date=&make_end_date=&category=&shape=&detail_url=board_list&no=24094&page=1&develop_mode=") # Need to loop through

time.sleep(2) # verifying the page loading

# Locate the table

table = driver.find_element(By.TAG_NAME, "table")  # Adjust selector as needed

# Extract table rows

download_header = table.find_element(By.XPATH, "//th[contains(text(),'다운로드')]")
download_row = download_header.find_element(By.XPATH, "..")
download_button = download_row.find_element(By.TAG_NAME, "td")
download_button.click()

print("Download started!")

# Wait for the file to download before closing the browser (adjust sleep time if needed)

time.sleep(2)  # Adjust based on file size



# Close the driver
driver.quit()

