from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up WebDriver (replace with your WebDriver path)
driver = webdriver.Chrome()

try:
    # Navigate to Google
    driver.get("https://www.google.com")
    
    # Maximize the browser window
    driver.maximize_window()

    # Wait for the search bar to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Find the search bar and type the search query (e.g., "laptop")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    

    # Extract search result titles and URLs
    results = driver.find_elements(By.XPATH, "//h3[contains(@class, 'LC20lb')]")

    
    # Print the top 5 results
    print("Top search results:")
    for i in range(min(5, len(results))):
        title = results[i].text
        url = results[i].find_element(By.XPATH, "..").get_attribute("href")
        print(f"{i+1}. {title} - {url}")
finally:
    # Quit the WebDriver
    driver.quit()
