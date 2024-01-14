from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



def configure_firefox_options():
    firefox_options = Options()
    #firefox_options.headless = True
    # Set download directory
    download_directory = '~/Documents/ws/machine_learning/scrapper_chess_data/'
    firefox_options.set_preference("browser.download.folderList", 2)
    firefox_options.set_preference("browser.download.dir", download_directory)
    firefox_options.set_preference("browser.download.useDownloadDir", True)
    firefox_options.set_preference("browser.download.viewableInternally.enabledTypes", "")
    firefox_options.set_preference("browser.download.manager.showWhenStarting", False)

    return firefox_options

def download_data(driver):
    # Find and click the checkbox
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'archive-games-check-all'))
    )
    checkbox.click()

    # Find and click the download button
    download_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'archive-games-download-button'))
    )
    download_button.click()

    # Wait for download to complete (you may need to adjust the time based on your network speed)
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ui_pagination-item-component'))
        )
    except TimeoutException:
        print("Download timed out.")

def navigate_to_next_page(driver):
    # Find and click the "Next Page" button
    next_page_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='ui_pagination-item-component' and @aria-label='Next Page']"))
    )
    next_page_button.click()

# Set up the Firefox WebDriver with configured options
firefox_options = configure_firefox_options()
driver = webdriver.Firefox(options=firefox_options)
# gecko_driver_path = '/usr/bin/firefox'
# driver = webdriver.Firefox(executable_path=gecko_driver_path)



# Replace 'number_of_pages' with the total number of pages you want to download
number_of_pages = 84


# Visit the login page
driver.get("https://www.chess.com/login")



print("Please manually login to chess.com. After logging in, press Enter.")
input()

# Wait for the user to manually login
print("Waiting for login to complete... (you may adjust the time based on your login speed)")
WebDriverWait(driver, 3).until(
    EC.url_contains("chess.com/home")
)

# Replace 'your_archive_url' with the URL of the archive page you want to start from
archive_url = 'https://www.chess.com/games/archive?gameOwner=my_game&gameType=live&endDate%5Bdate%5D=01/15/2024&startDate%5Bdate%5D=01/01/2022&timeSort=desc&gameTypes%5B0%5D=lightning&gameTypes%5B1%5D=bullet&gameTypes%5B2%5D=blitz&gameTypes%5B3%5D=standard&gameTypes%5B4%5D=liveChess960&gameTypes%5B5%5D=bughouse&gameTypes%5B6%5D=threecheck&gameTypes%5B7%5D=crazyhouse&gameTypes%5B8%5D=kingofthehill&gameTypes%5B9%5D=rapid&gameTypes%5B10%5D=oddschess&page=1'
driver.get(archive_url)


# Loop through pages and download data
for page_number in range(number_of_pages):
    download_data(driver)
    navigate_to_next_page(driver)

# Close the browser when done
driver.quit()
