from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (using Chrome here, ensure ChromeDriver is installed)
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")
    print("Opened Google")

    # Find the search box
    search_box = driver.find_element(By.NAME, "q")

    # Type "Selenium Python" in the search box and press Enter
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    print("Search performed")

    # Wait for results to load
    time.sleep(2)

    # Get search result titles
    results = driver.find_elements(By.XPATH, "//h3")

    print("Search Results:")
    for index, result in enumerate(results[:5], start=1):  # Print the first 5 results
        print(f"{index}. {result.text}")

finally:
    # Close the browser
    driver.quit()
    print("Browser closed")
